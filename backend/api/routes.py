import pandas as pd
from backend.controllers import login, money
from backend.ml import model_1, model_2, model_3
from backend.models import User
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.security import HTTPBearer
from sklearn.metrics import accuracy_score
from backend.api.queue.worker import queue
from tasks import predict_task
import time

router = APIRouter(prefix="/api")


@router.post("/login")
def get_token(user: User):
    token = login(user)
    return token


def create_job():
    job = queue.enqueue(predict_task, args=(2, 2))
    job_id = job.get_id()
    print(f"Job ID: {job_id}")
    print(job.is_finished)
    print(job.result)

    while not job.is_finished:
        job.refresh()
        time.sleep(0.5)

    result = job.result
    print(result)
    return {"accuracy":  0.6}

@router.post("/predict")
async def create_upload_file(model_name: str, file_path: str):
    try:
        result = create_job()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.get("/money")
def get_money(user: User):
    money_user = money(user)
    return money_user
