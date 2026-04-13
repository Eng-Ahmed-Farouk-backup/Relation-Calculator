import fastapi
import fastapi.middleware
import fastapi.middleware.cors
from algorithm import *

app = fastapi.FastAPI()
app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/relation")
def relation(relation: str, X: str, Y: str): 
    try:
        X = set(map(float,X.split(","))) if ":" not in X else set(range(int(X.split(":")[0]),int(X.split(":")[1])+1))
        Y = set(map(float,Y.split(","))) if ":" not in Y else set(range(int(Y.split(":")[0]),int(Y.split(":")[1])+1))
        return {"relation":calculate_relation(relation,X,Y)}
    except Exception as e:
        raise fastapi.HTTPException(status_code=400,detail="error 400: wrong format entered, X must be entered as a string in this form: '1,2,3' and Y must be entered in this form: '1,2,3' and relation must be a string in this format: '2x>y/1.5'")

@app.get("/domain")
def domain(relation: str, X: str, Y: str):
    try:
        X = set(map(float,X.split(","))) if ":" not in X else set(range(int(X.split(":")[0]),int(X.split(":")[1])+1))
        Y = set(map(float,Y.split(","))) if ":" not in Y else set(range(int(Y.split(":")[0]),int(Y.split(":")[1])+1))
        return {"domain":calculate_domain(relation,X,Y)}
    except Exception as e:
        raise fastapi.HTTPException(status_code=400,detail="error 400: wrong format entered, X must be entered as a string in this form: '1,2,3' and Y must be entered in this form: '1,2,3' and relation must be a string in this format: '2x>y/1.5'")

@app.get("/range")
def range_(relation: str, X: str, Y: str):
    try:
        X = set(map(float,X.split(","))) if ":" not in X else set(range(int(X.split(":")[0]),int(X.split(":")[1])+1))
        Y = set(map(float,Y.split(","))) if ":" not in Y else set(range(int(Y.split(":")[0]),int(Y.split(":")[1])+1))
        return {"range":calculate_range(relation,X,Y)}
    except Exception as e:
        raise fastapi.HTTPException(status_code=400,detail="error 400: wrong format entered, X must be entered as a string in this form: '1,2,3' and Y must be entered in this form: '1,2,3' and relation must be a string in this format: '2x>y/1.5'")

@app.get("/cartesian_product")
def cartesian_product(X: str, Y: str):
    try:
        X = set(map(float,X.split(","))) if ":" not in X else set(range(int(X.split(":")[0]),int(X.split(":")[1])+1))
        Y = set(map(float,Y.split(","))) if ":" not in Y else set(range(int(Y.split(":")[0]),int(Y.split(":")[1])+1))
        return {"product":calculate_cartesian_product(X,Y)}
    except Exception as e:
        raise fastapi.HTTPException(status_code=400,detail="error 400: wrong format entered, X must be entered as a string in this form: '1,2,3' and Y must be entered in this form: '1,2,3'")


@app.get("/is_function")
def is_function_(relation: str, X: str, Y: str):
    try:
        X = set(map(float,X.split(","))) if ":" not in X else set(range(int(X.split(":")[0]),int(X.split(":")[1])+1))
        Y = set(map(float,Y.split(","))) if ":" not in Y else set(range(int(Y.split(":")[0]),int(Y.split(":")[1])+1))
        return {"is_function":is_function(relation,X,Y)}
    except Exception as e:
        raise fastapi.HTTPException(status_code=400,detail="error 400: wrong format entered, X must be entered as a string in this form: '1,2,3' and Y must be entered in this form: '1,2,3' and relation must be a string in this format: '2x>y/1.5'")


