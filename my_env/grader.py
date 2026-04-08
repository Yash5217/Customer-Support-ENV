def calculate_reward(action, correct, step):
    score = 0.0

    if step == 1:
        if action.category == correct["category"]:
            score += 0.5
        else:
            score -= 0.2

    elif step == 2:
        if action.priority == correct["priority"]:
            score += 0.3

    elif step == 3:
        if len(action.response.strip()) > 20:
            score += 0.2

    return max(0.0, min(score, 1.0))
