from fastapi import FastAPI
import utils

app = FastAPI()

# Save data
@app.get("/savedata/{user_id}")
async def read_save_json(user_id: int):
    return {"Retribed save json for user " + user_id}

@app.put("/savedata/{user_id}")
async def update_save_json(user_id: int):
    return {"Updated save json for user " + user_id}

@app.post("/savedata/{user_id}")
async def new_save_json(user_id: int):
    return {"Created new save json for user " + user_id}


# Leaderboard
@app.get("/leaderboard/user")
async def read_user_leaderboard(user_id: int):
    return {"Retrieved leaderboard for user " + user_id + " at " + utils.getDate()}

@app.post("/leaderboard/user")
async def create_user_leaderboard(user_id: int):
    return {"Created leaderboard for user " + user_id}

@app.get("/leaderboard/global")
async def read_global_leaderboard(user_id: int):
    return {"Retrieved global leaderboard at " + utils.getDate()}




# Other
@app.get("/other/refresh")
async def when_next_leaderboard_refresh():
    return {"Next refresh is in " + utils.getRefresh}