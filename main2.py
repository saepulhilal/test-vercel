# import FastApi
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

key = "hacktiv8mania2023"

#public
@app.get("/")
def helloFunction():
    return {
        "message" : "hello world"
    }

#secret -> harus memasukan authentication
@app.get("/secret")
def helloFunction(api_key: str = Header(None)):
    # check api_key dari header
    if api_key is None or api_key != key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    return {
        "message" : "secret message"
    }
