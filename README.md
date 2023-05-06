### Work_104功能說明
將104人力銀行上使用關鍵字搜索結果，包含公司資訊、職缺名稱、聯絡資訊、所需技能等結果
以Excel逐筆呈現，並比對所需相關技能(1=有，0=無)。

### Work_104使用方式

※	以下步驟為 104_config.json 的設定及維護方式:

1.	job_keyword = 在104上搜尋職缺的關鍵字。
    max_pages = 要抓取的搜尋結果頁數。
    job_skills = 設定要比對的職缺技能，設定的技能呈現在 Excel 各職缺欄位。

2.	synonym_dic = 比對相關技能的同義字（例如AI=artificial intelligence=人工智慧，則寫成"AI": ["artificial intelligence","人工智慧"]），且英文以小寫做比對，不同技能需換行輸入。

3.	output_filename = 設定輸出的檔案名稱。

4.	以上設定完後，執行 crawl_np_104.py，等到出現 Processes all done. 代表資料抓取完畢。

5.	到 output 資料夾內查看 output_104.csv、output_104.excel 爬取結果；包含公司資訊、職缺名稱、聯絡資訊、技能比對(1=有，0=無)等詳細資料。

### 輸出範例
#### 資料夾畫面
![dataframe](https://github.com/marx1992620/work_104/blob/main/demo/folder.png)
#### output資料夾畫面
![word count](https://github.com/marx1992620/work_104/blob/main/demo/output_dir.png)
#### Excel畫面
![excel](https://github.com/marx1992620/work_104/blob/main/demo/output_file.png)
