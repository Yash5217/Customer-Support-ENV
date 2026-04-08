from pydantic import BaseModel

class Observation(BaseModel):
    ticket: str

class Action(BaseModel):
    category: str
    priority: str
    response: str

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict
