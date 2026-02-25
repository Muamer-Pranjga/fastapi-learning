from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"name": "Muamer", "role": "developer"}

@app.get("/contact")
def contact():
    return {"name": "Muamer", "email": "muamer.92@gmail.com", "contact": "6476478899"}