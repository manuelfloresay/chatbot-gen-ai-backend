from fastapi import FastAPI
import uvicorn
from routers import prompt
from models import Request, Response

app = FastAPI()

app.include_router(prompt)
app.state.limiter = limiter

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)