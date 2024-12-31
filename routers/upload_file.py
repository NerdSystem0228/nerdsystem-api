from fastapi import APIRouter, HTTPException, UploadFile, File
from utils.logger import logger
import aiofiles

router = APIRouter(
    prefix="/uploadfile",
    tags=["upload_file"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=201)
async def create_upload_file(file: UploadFile = File(...)):
    mega=file.size/pow(10, 6)
    if mega >= 1:
        return {"filename": file.filename, "file_size": file.size, "file_mime_type": file.content_type, "Result": "Failed, File size limit was exceed."} 
    logger.debug(f"File Name: {file.filename}")
    logger.debug(f"File Size: {file.size}")
    logger.debug(f"File MIME Type: {file.content_type}")
    async with aiofiles.open(f"./files/{file.filename}", "wb") as out_file:
        while content := await file.read(4096):
            await out_file.write(content)
            
        logger.debug(f"File {file.filename} has been written to the disk succesfully.")
        
    return {"filename": file.filename, "file_size": file.size, "file_mime_type": file.content_type, "Result": "Ok"}
