from fastapi import FastAPI
try:
  import simplejson as json
except ImportError:
  import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": "blah"}

