import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/generate")
async def root():
    time.sleep(10)
    return {'message': "Hello"}
