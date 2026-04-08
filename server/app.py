from my_env.env import SupportEnv
from my_env.models import Action


def main():
    env = SupportEnv()

    obs = env.reset(task_index=0)

    total_reward = 0

    for step in range(3):
        # Dummy action (you can improve logic if needed)
        action = Action(category="billing", priority="high")

        result = env.step(action)

        total_reward += result.reward

        if result.done:
            break

    env.close()

    return {
        "success": total_reward >= 0.5,
        "score": total_reward
    }


if __name__ == "__main__":
    main()
