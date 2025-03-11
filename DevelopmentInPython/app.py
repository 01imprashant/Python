from fastapi import FastAPI, UploadFile

app=FastAPI()


@app.get('/')
def home():
    return {"data":"Welcome to home page"}

@app.get('/about')
def about():
    return {"data":"Welcome to about page"}

@app.get('/contact')
def contact():
    return {"data":"Welcome to contact page"}

@app.post('/upload')
def upload_image(files:list[UploadFile]):
    print(files)
    return {'status':'Got the file'}

import uvicorn
uvicorn.run(app)