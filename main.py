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
    X = set(map(int,X.split(",")))
    Y = set(map(int,Y.split(",")))
    return {"relation":calculate_relation(relation,X,Y)}

@app.get("/domain")
def domain(relation: str, X: str, Y: str):
    X = set(map(int,X.split(",")))
    Y = set(map(int,Y.split(",")))
    return {"domain":calculate_domain(relation,X,Y)}

@app.get("/range")
def range_(relation: str, X: str, Y: str):
    X = set(map(int,X.split(",")))
    Y = set(map(int,Y.split(",")))
    return {"range":calculate_range(relation,X,Y)}

@app.get("/cartesian_product")
def cartesian_product(X: str, Y: str):
    X = set(map(int,X.split(",")))
    Y = set(map(int,Y.split(",")))
    return {"product":calculate_cartesian_product(X,Y)}

@app.get("/is_function")
def is_function_(relation: str, X: str, Y: str):
    X = set(map(int,X.split(",")))
    Y = set(map(int,Y.split(",")))
    return {"is_function":is_function(relation,X,Y)}

