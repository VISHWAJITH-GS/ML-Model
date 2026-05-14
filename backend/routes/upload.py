from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from ..services.upload_service import save_upload_file

router = APIRouter()


@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    # Basic validation for CSV / XLSX
    allowed = (
        "text/csv",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-excel",
    )
    if file.content_type not in allowed:
        raise HTTPException(status_code=400, detail="Only CSV and XLSX supported")

    result = await save_upload_file(file)
    return JSONResponse({"success": True, "message": "Dataset uploaded successfully", "data": result})
