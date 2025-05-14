from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import os
import io
from uuid import uuid4

app = FastAPI()

# 儲存檔案的資料夾
APACHE_UPLOAD_FOLDER_BRAND = "../../brand_image"
APACHE_UPLOAD_FOLDER_CASE = "../../case_image"
APACHE_UPLOAD_FOLDER_PRODUCT = "../../product_image"

os.makedirs(APACHE_UPLOAD_FOLDER_BRAND, exist_ok=True)
os.makedirs(APACHE_UPLOAD_FOLDER_CASE, exist_ok=True)
os.makedirs(APACHE_UPLOAD_FOLDER_PRODUCT, exist_ok=True)

# 設定最大允許的寬度與高度
MAX_WIDTH = 1920
MAX_HEIGH = 1200
QUALITY = 80

@app.post("/upload/brand")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(("png", "jpg", "jpeg")):
        return JSONResponse(content={
            "message": "不支援的檔案格式！"
        }, status_code=400)
    # 讀取上傳的圖片
    image = Image.open(io.BytesIO(await file.read()))

    # 獲取原始大小
    original_size = image.size  # width / height

    # 生成為一檔案名
    unique_filename = f"{uuid4().hex}.jpg"
    file_path = os.path.join(APACHE_UPLOAD_FOLDER_BRAND, unique_filename)

    # 儲存壓縮後的照片
    image.save(file_path, format="JPEG", quality=QUALITY)

    # 返回圖片URL
    file_url = f"https://img.shyen.com.tw:447/brand_image/{unique_filename}"
    return JSONResponse(content={
        "message": "圖片上傳成功",
        "fileUrl": file_url,
        "originalSize": original_size,
        "newSize": image.size
    }, status_code=200)

@app.post("/upload/case")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(("png", "jpg", "jpeg")):
        return JSONResponse(content={
            "message": "不支援的檔案格式！"
        }, status_code=400)
    # 讀取上傳的圖片
    image = Image.open(io.BytesIO(await file.read()))

    # 獲取原始大小
    original_size = image.size  # width / height

    # 生成為一檔案名
    unique_filename = f"{uuid4().hex}.jpg"
    file_path = os.path.join(APACHE_UPLOAD_FOLDER_CASE, unique_filename)

    # 儲存壓縮後的照片
    image.save(file_path, format="JPEG", quality=QUALITY)

    # 返回圖片URL
    file_url = f"https://img.shyen.com.tw:447/case_image/{unique_filename}"
    return JSONResponse(content={
        "message": "圖片上傳成功",
        "fileUrl": file_url,
        "originalSize": original_size,
        "newSize": image.size
    }, status_code=200)

@app.post("/upload/product")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(("png", "jpg", "jpeg")):
        return JSONResponse(content={
            "message": "不支援的檔案格式！"
        }, status_code=400)
    # 讀取上傳的圖片
    image = Image.open(io.BytesIO(await file.read()))

    # 獲取原始大小
    original_size = image.size  # width / height

    # 生成為一檔案名
    unique_filename = f"{uuid4().hex}.jpg"
    file_path = os.path.join(APACHE_UPLOAD_FOLDER_PRODUCT, unique_filename)

    # 儲存壓縮後的照片
    image.save(file_path, format="JPEG", quality=QUALITY)

    # 返回圖片URL
    file_url = f"https://img.shyen.com.tw:447/product_image/{unique_filename}"
    return JSONResponse(content={
        "message": "圖片上傳成功",
        "fileUrl": file_url,
        "originalSize": original_size,
        "newSize": image.size
    }, status_code=200)