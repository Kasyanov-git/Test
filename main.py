from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/")
async def root(name: str, message: str):
    return HTMLResponse("Rekruto! Давай дружить!")
@app.get("/url_name")
async def url_name(name: str, message: str):
    return HTMLResponse(f"<b>Привет от Никиты, {name}! <br> {message}</b>")