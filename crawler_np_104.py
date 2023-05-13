import requests
import json
import os
import time
import random
import threading
from bs4 import BeautifulSoup
from queue import Queue
# from multiprocessing.dummy import Pool
import numpy as np
import openpyxl
import re

config = {}
data_np = ""
url_Queue = Queue()
pages_Queue = Queue()
headers_Queue = Queue()
times_Queue = Queue()
# 建立 Excel 活頁簿
wb = openpyxl.Workbook()
# 取得作用中的工作表
ws = wb.active
# # 設定工作表名稱
ws.title = "104_jobs"
area_dic = {"台北市":"6001001000","新北市":"6001002000","宜蘭縣":"6001003000","基隆市":"6001004000","桃園市":"6001005000","新竹縣市":"6001006000","苗栗縣":"6001007000","台中市":"6001008000","彰化縣":"6001010000","南投縣":"6001011000","雲林縣":"6001012000","嘉義縣市":"6001013000","台南市":"6001014000","高雄市":"6001016000","屏東縣":"6001018000","台東縣":"6001019000","花蓮縣":"6001020000","澎湖縣":"6001021000","金門縣":"6001022000","連江縣":"6001023000"}
keyword, area_code = "",""

def setting():
    global data_np, config, keyword, area_code
    if not os.path.exists('./output'):
        os.mkdir('./output')

    # 讀取104_config
    if not os.path.exists(r'./104_config.json'):
        return
    try:
        with open(r'./104_config.json', 'r', encoding='utf-8') as f:
            config = json.loads(f.read())
        print("------------------config------------------")
        print(config)
    except Exception as e:
        print(f"read config occurs exception as: {str(e)}")

    config["max_rows"] = int(config["max_pages"]) * 60
    for tt in range(int(config["max_rows"])):
        times_Queue.put(tt) # 建立編號Queue

    for key in config["job_skills"]:
        if key not in config["synonym_dic"]:
            config["synonym_dic"][key]=[key.lower()]
    for skill_column in config["synonym_dic"]:
        if skill_column not in config["job_skills"]:
            config["job_skills"].append(skill_column)

    keyword, area = config["job_keyword"], config["job_area"] # 搜尋相關職缺 地點
    area_code = ""
    if len(area) > 0 and type(area) == type(list()):
        for a in area:
            if area_dic[a]:
                if len(area_code)>0:
                    area_code += "," + area_dic[a]
                else:
                    area_code += "&area=" + area_dic[a]
    # 建立 NumPy 陣列
    data_np = np.array([['company', 'job_name', 'job_area', 'job_content', 'job_exp', 'job_require', 'job_welfare', 'job_contact', 'URL'] + config["job_skills"]])


def map_skill(job_skills):
    column = [0 for _ in range(len(config["job_skills"]))]
    for each_job_skill in job_skills:
        pos = -1
        for skill_key in config["job_skills"]:
            pos += 1
            if skill_key == "R":
                match = re.search(r"\WR\W",each_job_skill.lower())
                if match:
                    column[pos] = 1
                    continue
            else:                           
                for sk in config["synonym_dic"][skill_key]: # 從同義字字典匹配技能項
                    if sk.lower() in each_job_skill.lower():
                        column[pos] = 1
                        break
    return column


def crawl_url():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    for n in range(1, int(config["max_pages"])): # 設定爬頁數
        url = f'https://www.104.com.tw/jobs/search/?ro=0&keyword={keyword}{area_code}&order=1&asc=0&page={n}&mode=s&jobsource=2018indexpoc'
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        page = soup.select('div[id="js-job-content"]')[0].select('h2[class="b-tit"] a')
        pages_Queue.put(page)

def crawl_content(url,headers):
    global data_np
    for _ in range(2):
        try:
            res = requests.get(url=url, headers=headers)
            continue
        except:
            time.sleep(3)
    soup = BeautifulSoup(res.text,'html.parser')
    json_data = json.loads(soup.text) # 資料轉dict格式
    job_name = json_data['data']['header']['jobName']
    company = json_data['data']['header']['custName']
    job_area = json_data['data']['jobDetail']['addressRegion'] + json_data['data']['jobDetail']['addressDetail'] 
    job_contact = '聯絡人:' + json_data['data']['contact']['hrName'] + 'email:' + json_data['data']['contact']['email']
    job_require = "接受身分:" + "、".join([i['description'] for i in json_data['data']['condition']['acceptRole']['role']])
    job_welfare = json_data['data']['welfare']['welfare']
    job_content = json_data['data']['jobDetail']['jobDescription']
    job_exp = "工作經驗:" + json_data['data']['condition']['workExp']
    job_skills = [i['description'].replace('\t','').replace(' ','') for i in json_data['data']['condition']['specialty']]
    job_skills += [i.replace('\t','').replace(' ','')  for i in json_data['data']['condition']['other'].split("\n")]
    job_skills += [i.replace('\t','').replace(' ','')  for i in json_data['data']['jobDetail']['jobDescription'].split("\n")]
    job_url = url.replace("ajax/content/","")
    
    column = map_skill(job_skills) # 搜索所需技能
    print(company,job_name,job_area)
    row = np.array([company, job_name, job_area, job_content, job_exp, job_require, job_welfare, job_contact, job_url] + column)
    data_np = np.vstack([data_np,row])
    time.sleep(random.randint(3,5)) # 每爬完一頁休息3-5秒


def crawl_thread():
    while pages_Queue.empty() is False:
        page = pages_Queue.get()
        for i in range(len(page)): # 從頁面得到每筆職缺url
            j = 'https:' + page[i]['href']
            header = {'Referer': 'https://www.104.com.tw/job/' + j[27:32]}
            headers_Queue.put(header) # 對應每個url的headers放進Queue
            url = 'https://www.104.com.tw/job/ajax/content/'+ j[27:32]
            url_Queue.put(url) # 每個職缺的url放進Queue
    threads = []
    for t in range(8): # 建執行緒
        t = thread_class("t"+str(t))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()# 主線程必須等到所有threads執行完畢才繼續執行

class thread_class(threading.Thread): # python繼承
    def __init__(self, name): # 接受name參數
        threading.Thread.__init__(self) # initialize class
        self.name = name # 每條thread的名子
    def run(self): # thread啟動後執行函數
        while url_Queue.empty() is False:  # 檢查url_Queue不為空的話，獲取URL後parse
            url = url_Queue.get() # 從Queue依序取出url
            headers = headers_Queue.get() # 從Queue依序取出headers
            crawl_content(url,headers)

if __name__ == '__main__':
    tStart = time.time() # 起始時間
    setting()
    print("start crawling 104 website")
    crawl_url()
    print("start crawling content")
    crawl_thread()
    # 將 NumPy 陣列寫入 Excel 工作表
    for data in data_np:
        ws.append(data.tolist())
    # 儲存 Excel 活頁簿至檔案
    wb.save(os.path.join('output',fr'{config["output_filename"]}.xlsx'))
    wb.save(os.path.join('output',fr'{config["output_filename"]}.csv'))
    tEnd = time.time() # 結束時間
    print('Cost %d seconds' % (tEnd - tStart)) # 完成花費時間
    print(f"crawled total jobs: {len(data_np)-1}")
    print("Processes all done.")
    wait = input()
