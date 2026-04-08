from fastapi import FastAPI
from my_env.env import SupportEnv

app = FastAPI()

env = SupportEnv()

@app.get("/")
def home():
    return {"message": "Server running"}

@app.post("/reset")
def reset():
    obs = env.reset(task_index=0)
    return {"ticket": obs.ticket}

@app.post("/step")
def step(action: dict):
    result = env.step(action)
    return {
        "reward": result.reward,
        "done": result.done
    }
