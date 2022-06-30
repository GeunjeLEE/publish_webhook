from fastapi import FastAPI
from pydantic import BaseModel
from manager.version_manager import VersionManager

app = FastAPI()

class Body(BaseModel):
    callback_url: str
    push_data: dict
    repository: dict

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

@app.post("/dockerhub/{image_name}")
async def update(image_name, body: Body):
    tag = body.push_data['tag']
    v = VersionManager()

    return v.run(image_name, tag)
