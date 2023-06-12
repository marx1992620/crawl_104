from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import utils
import json
import os
import csv


app = FastAPI()
templates = Jinja2Templates(directory="templates")

config = {"input_text": "", "selected_option": ""}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/save_config")
async def save_config(request: Request, input_text: str = Form(...), input_int: int = Form(...), selected_options: str = Form(None), file: UploadFile = File(None)):
    # Process the form data here
    print(f"Input Text: {input_text}")
    print(f"Input Int: {input_int}")
    print(f"Selected Options: {selected_options}")
    if selected_options == None:
        selected_options = ["不拘"]
    else:
        selected_options = selected_options.replace(" ","")
        selected_options = selected_options.split(",")

    if file != None:
        data = await file.read()
        if len(data) > 0 :
            json_data = json.loads(data)
        else:
            json_data = None
    else:
        json_data = None

    dataframe = utils.main(input_text,input_int,selected_options,json_data)

    return templates.TemplateResponse('success.html', {"request": request,"numpy_array": dataframe})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8880)