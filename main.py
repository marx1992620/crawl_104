from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
from fastapi import FastAPI, Form

app = FastAPI()
templates = Jinja2Templates(directory="templates")

config = {"input_text": "", "selected_option": ""}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("home1.html", {"request": request})

@app.post("/save_config")
async def save_config(input_text: str = Form(...), selected_options: List[str] = Form(...)):
    # Use the input_text and selected_options in your backend logic
    # ...
    return {"message": "Config saved successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8880)