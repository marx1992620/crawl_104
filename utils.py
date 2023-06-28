# -*- coding:utf-8 -*-
import os
import numpy as np
from crawler_np_104 import App
import traceback


def setting(area):
    area_dic = {"不拘":"","台北市":"6001001000","新北市":"6001002000","宜蘭縣":"6001003000","基隆市":"6001004000","桃園市":"6001005000","新竹縣市":"6001006000","苗栗縣":"6001007000","台中市":"6001008000","彰化縣":"6001010000","南投縣":"6001011000","雲林縣":"6001012000","嘉義縣市":"6001013000","台南市":"6001014000","高雄市":"6001016000","屏東縣":"6001018000","台東縣":"6001019000","花蓮縣":"6001020000","澎湖縣":"6001021000","金門縣":"6001022000","連江縣":"6001023000"}
    area_code = ""
    if "不拘" in area:
        area_code = ""
    elif len(area) > 0 and type(area) == type(list()):
        for a in area:
            if area_dic[a]:
                if len(area_code)>0:
                    area_code += "," + area_dic[a]
                else:
                    area_code += "&area=" + area_dic[a]

    return area_code


def skill_synonym(skills):
    App.config["job_skills"] = list(skills["synonym_dic"].keys())
    for key in App.config["job_skills"]:
        if key not in App.config["synonym_dic"]:
            App.config["synonym_dic"][key]=[key.lower()]
    for skill_column in App.config["synonym_dic"]:
        if skill_column not in App.config["job_skills"]:
            App.config["job_skills"].append(skill_column)


def main(job_keyword,max_pages,area,skills):
    App.area_code = setting(area)
    App.config["job_keyword"] = job_keyword
    App.config["max_rows"] = max_pages * 60
    App.config["max_pages"] = max_pages
    App.config["output_filename"] = "output_104"

    if skills != None:
        App.config["synonym_dic"] = skills["synonym_dic"]
        skill_synonym(skills)    
    if "job_skills" in App.config:
        App.data_np = np.array([['company', 'job_name', 'job_area', 'job_salary', 'job_content', 'job_exp', 'job_require_major', 'job_welfare', 'job_contact', 'URL'] + App.config["job_skills"]])
    else:
        App.data_np = np.array([['company', 'job_name', 'job_area', 'job_salary', 'job_content', 'job_exp', 'job_require_major', 'job_welfare', 'job_contact', 'URL']])

    print("start crawling 104 website")
    App.crawl_url()
    print("start crawling content")
    App.crawl_thread()
    # 將 NumPy 陣列寫入 Excel 工作表
    for data in App.data_np:
        try:
            App.ws.append(data.tolist())
        except:
            traceback.print_exc()
            print(data)

    # 儲存 Excel 活頁簿至檔案
    App.wb.save(os.path.join('output',fr'{App.config["output_filename"]}.xlsx'))
    App.wb.save(os.path.join('output',fr'{App.config["output_filename"]}.csv'))
    print(f"crawled total jobs: {len(App.data_np)-1}")
    print(os.path.join('output',fr'{App.config["output_filename"]}.csv'))
    print("Processes all done.")
    return App.data_np
