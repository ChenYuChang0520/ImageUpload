# 圖片上傳API

- 參考chatgpt：https://chatgpt.com/share/67aee287-3cc0-8004-84d8-da37f73dd107

## 結構說明

- 這隻小程式分別有三個部分
  - API
  - Server
  - Web
- API
  - 可在任何可執行python3的環境，執行此API，並透過此API呼叫Server的API，將圖片上傳至Web Server
  - 套件安裝：pip3 install fastapi uvicorn python-multipart requests
  - API啟動：uvicorn app:app --host 0.0.0.0 --port 9000
  - 啟動後可以透過瀏覽器開啟http://127.0.0.1:9000/docs ，開啟網頁後快速測試API
- Server
  - 用於將API上傳的圖片，轉存到Web Server的中介軟體
  - 開發時使用的是Apache2，OS為Ubuntu
  - 套件安裝：pip3 install pillow fastapi uvicorn python-multipart
  - 預設圖片大小是1920 x 1200 (16:10)，品質：80
  - API啟動：sudo uvicorn app:app --host 0.0.0.0 --port 445
  - Linux環境推薦使用Screen，讓terminal的session分離，中斷後還是可以繼續執行API
- Web
  - 當時測試時是用原生的js開發的，還沒有進行測試，好像都會被catch error，但實際都是有上傳成功的
## 使用注意

- API > app.py
  - Line8：請根據實際Image Server的IP位址修改，後面/upload是呼叫該API，不用改
- Server > app.py
  - Line11：請根據實際程式擺放位置，調整對應要儲存圖片的路徑，如果是存在web server裡，要注意權限問題
