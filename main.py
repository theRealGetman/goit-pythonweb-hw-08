from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.api import contacts, utils


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(utils.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
