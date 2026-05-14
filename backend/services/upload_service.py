import os
import uuid
from typing import Dict

from fastapi import UploadFile


async def save_upload_file(file: UploadFile, save_dir: str | None = None) -> Dict:
    save_dir = save_dir or os.getenv("MODEL_STORAGE_PATH", "backend/saved_models")
    os.makedirs(save_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    file_path = os.path.join(save_dir, filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"filename": filename, "path": file_path}
