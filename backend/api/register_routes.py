import pandas as pd
from backend.controllers import login, money
from backend.ml import model_1, model_2, model_3
from backend.models import User
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.security import HTTPBearer
from sklearn.metrics import accuracy_score

router = APIRouter(prefix="/api")


@router.post("/login")
def get_token(user: User):
    token = login(user)
    return token

@router.post("/predict")
async def create_upload_file(model_name: str, file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        Y = df['Label']
        X = df.drop('Label', axis=1)
        if model_name == 'dt':
            predict = model_1.predict(X)
        elif model_name == 'lr':
            predict = model_2.predict(X)
        else:
            predict = model_3.predict(X)
        accuracy = accuracy_score(Y, predict)
        return {'accuracy': accuracy}
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="Empty CSV file")
    except pd.errors.ParserError:
        raise HTTPException(status_code=400, detail="Invalid CSV file format")
    
@router.get("/money")
def get_money(user: User):
    money_user = money(user)
    return money_user

# @router.post('/add_money')
# def add_money(user: User):
#     try:
#         pass
#     except NoResultFound:
#         raise HTTPException(status_code=404, detail="User not found in the money database")
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")



