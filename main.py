from fastapi import FastAPI
import uvicorn
from routers.prompt import router
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)