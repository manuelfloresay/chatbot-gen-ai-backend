from fastapi import FastAPI
import uvicorn
from routers import prompt

app = FastAPI()
app.include_router(prompt)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)