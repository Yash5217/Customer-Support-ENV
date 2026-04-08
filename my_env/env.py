from my_env.models import Observation, Action, StepResult
from my_env.tasks import TASKS
from my_env.grader import calculate_reward

class SupportEnv:

    def __init__(self):
        self.current_task = None
        self.done = False
        self.step_count = 0
        self.total_reward = 0.0

    def reset(self, task_index=0):
        self.current_task = TASKS[task_index]
        self.done = False
        self.step_count = 0
        self.total_reward = 0.0

        return Observation(ticket=self.current_task["ticket"])

    def step(self, action: Action):
        if self.done:
            raise Exception("Episode already finished.")

        self.step_count += 1

        reward = calculate_reward(action, self.current_task, self.step_count)
        self.total_reward += reward

        if self.step_count >= 3:
            self.done = True

        observation = Observation(ticket=self.current_task["ticket"])

        return StepResult(
            observation=observation,
            reward=reward,
            done=self.done,
            info={
                "step": self.step_count,
                "task_name": self.current_task["name"],
                "total_reward": round(self.total_reward, 2)
            }
        )

    def state(self):
        return {
            "task": self.current_task,
            "step": self.step_count,
            "done": self.done,
            "total_reward": round(self.total_reward, 2)
        }

    def close(self):
        pass
