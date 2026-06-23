from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# cd "D:\00. Git Repository\API\fastapi"
# uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs