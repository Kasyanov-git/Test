from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/url_name")
async def root(name: str, message: str):
    return HTMLResponse(f"<b>Привет от Никиты, {name}! <br> {message}</b>")
