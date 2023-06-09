from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form
import utils


app = FastAPI()
templates = Jinja2Templates(directory="templates")

config = {"input_text": "", "selected_option": ""}

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/save_config")
async def save_config(input_text: str = Form(...), input_int: int = Form(...), selected_options: str = Form(...)):
    # Process the form data here
    print(f"Input Text: {input_text}")
    print(f"Input Int: {input_int}")
    print(f"Selected Options: {selected_options}")
    selected_options = selected_options.replace(" ","")
    selected_options = selected_options.split(",")
    utils.main(input_text,input_int,selected_options)



    # Return a response or perform other operations as needed
    return {"message": "Form data received successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8880)