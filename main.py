from fastapi import FastAPI

app = FastAPI()

@app.get("/savedata/{user_id}")
async def read_save_json(user_id: int):
    return {"Retribed save json for user " + user_id}

@app.put("/savedata/{user_id}")
async def update_save_json(user_id: int):
    return {"Updated save json for user " + user_id}

@app.post("/savedata/{user_id}")
async def new_save_json(user_id: int):
    return {"Created new save json for user " + user_id}