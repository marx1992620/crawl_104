### 目的
將104人力銀行上使用關鍵字搜索結果，包含公司資訊、職缺名稱、聯絡資訊、所需技能等結果
以Excel逐筆呈現，並比對所需相關技能(1=有，0=無)。

### 操作說明

※	以下使用步驟:

1.	執行 exe.py 前安裝所需 requirements.txt 或執行 dist/exe.exe，執行成功開啟網頁 http://127.0.0.1:8880

2. 於網頁輸入職缺關鍵字、選擇工作地點(最多三個，可不選)、輸入爬蟲的網頁數，上傳已編輯好的技能同義詞字典synonym.json(僅接受json檔，若無可跳過)

3.	請參考synonym.json格式，synonym_dic中填寫欲搜尋的技能及其同義詞（例如AI同義詞有artificial intelligence=人工智慧，則寫成"AI": ["artificial intelligence","人工智慧"]），英文不分大小寫，不同技能需換行輸入。

4.	程式出現 Processes all done. 代表資料抓取完畢。輸出檔案於 output資料夾: output_104.csv、output_104.xlsx，並於網頁呈現結果。

5.	爬取結果；包含公司名稱、職缺名稱、工作地點、待遇、工作內容、工作經驗、學歷要求、福利、各技能比對(1=有，0=無)、技能配對總數(match_skills)等詳細資料。
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
