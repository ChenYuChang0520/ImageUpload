from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# Image Server URL
IMAGE_Server_URL = "http://192.168.1.135:445/upload"


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # 驗證檔案格式
    if not file.filename.endswith(("png", "jpg", "jpeg", "gif")):
        return JSONResponse(content={
            "message": "不支援的檔案格式！"
        }, status_code=400)
    # 將檔案轉發到 Image Server
    try:
        files = {
            "file": (file.filename, file.file, file.content_type)
        }
        response = requests.post(IMAGE_Server_URL, files=files)

        # 檢查 Image Server 回應
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content={
                "message": "檔案上傳成功！",
                "fileUrl": data.get("fileUrl"),
                "originalSize": data.get("originalSize"),
                "newSize": data.get("newSize")

            }, status_code=200)
        else:
            return JSONResponse(content={
                "message": "上傳至Image Server 失敗！"
            }, status_code=response.status_code)
    except Exception as e:
        return JSONResponse(content={
            "message": f"上傳失敗：{str(e)}"
        }, status_code=500)
