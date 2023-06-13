### Work_104功能說明
將104人力銀行上使用關鍵字搜索結果，包含公司資訊、職缺名稱、聯絡資訊、所需技能等結果
以Excel逐筆呈現，並比對所需相關技能(1=有，0=無)。

### Work_104使用方式

※	以下使用步驟:

1.	

2.	synonym_dic = 比對相關技能的同義字（例如AI=artificial intelligence=人工智慧，則寫成"AI": ["artificial intelligence","人工智慧"]），英文不分大小寫，不同技能需換行輸入。

3.	output_filename = 設定輸出的檔案名稱。

4.	以上設定完後，執行 crawl_np_104.py 或 dist/crawler_np_104.exe，等到出現 Processes all done. 代表資料抓取完畢。

5.	到 output 資料夾內查看 output_104.csv、output_104.excel 爬取結果；包含公司資訊、職缺名稱、聯絡資訊、技能比對(1=有，0=無)等詳細資料。
### 網頁輸入範例
![folder](https://github.com/marx1992620/work_104/blob/main/demo/web.png)
   #### 1.搜尋技能同義詞範例
![folder](https://github.com/marx1992620/work_104/blob/main/demo/synonym.png)
### 網頁輸出範例
![folder](https://github.com/marx1992620/work_104/blob/main/demo/output_table.png)
### 檔案輸出範例
   #### 1.資料夾畫面
![folder](https://github.com/marx1992620/work_104/blob/main/demo/folder.png)
   #### 2.output資料夾畫面
![output_dir](https://github.com/marx1992620/work_104/blob/main/demo/output_dir.png)
   #### 3.程式執行畫面
![processing](https://github.com/marx1992620/work_104/blob/main/demo/processing.png)
   #### 4.Excel畫面
![excel](https://github.com/marx1992620/work_104/blob/main/demo/output_file.png)
