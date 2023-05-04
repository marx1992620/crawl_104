### Work104功能說明
將104人力銀行上使用關鍵字搜索結果，包含公司資訊、職缺名稱、聯絡資訊、所需技能等結果
以Excel逐筆呈現，並將相關技能個別小計在Excel。

### Work104使用方式

※	以下步驟中文字檔維護方式：英文不分大小寫，不同技能需換行輸入。

1.	將班級內所有可在104上做關鍵字搜尋的技能維護至 104_config.json 文字檔內。

2.	並將同義字（例如AI=artificial intelligence=人工智慧）維護至 104_config.json 內，以半形逗號分隔。

3.	且在config \ 104_config.json文字檔內，將要呈現在爬取結果Excel上的技能逐筆維護。

4.	config \ 104_config.json 則是設定檔案的輸出方式。設定方式如下：
job_keyword=設定成要做為在104上搜尋的關鍵字。
max_pages=要抓取的搜尋結果頁數。

5.	以上設定完後，點選crawl_104.exe，等到出現
[Computing the amount of each skill...]
Processes all done. 代表資料抓取完畢。

6.	到output資料夾內查看 104_output.csv、104_output.excel 爬取結果；包含公司資訊、職缺名稱、聯絡資訊、技能個別小計數量(1=有，0=無)等詳細資料。

<!-- ### 輸出範例 -->
<!-- #### 資料夾畫面 -->
<!-- ![dataframe](https://github.com/uuboyscy/work104/blob/master/output-folder.png) -->
<!-- #### Excel畫面 -->
<!-- ![excel](https://github.com/uuboyscy/work104/blob/master/output-dataframe.png) -->
<!-- #### Word count -->
<!-- ![word count](https://github.com/uuboyscy/work104/blob/master/output-wordcount.png) -->
