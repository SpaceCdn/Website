from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
pages = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return pages.TemplateResponse("index.html", {"request": request})


@app.get("/install", response_class=fastapi.responses.HTMLResponse)
def install(request: fastapi.Request):
    return fastapi.responses.RedirectResponse(
        "https://alpha.deta.space/discovery/spaceshuttle-sbm-v0.1.1.2"
    )
