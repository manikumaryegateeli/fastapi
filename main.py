from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message":"Hello welcome to neuralpace, a place to chase your passion!"}
