# 🧠 Customer Support Ticket Resolution Environment

## 📌 Overview
This project implements a **real-world OpenEnv environment** that simulates a customer support workflow.  
An AI agent interacts with the environment to process user complaints by:

- Classifying the issue
- Assigning priority
- Generating a response

The environment is designed for training and evaluating intelligent agents using step-based interaction.

---

## 🎯 Objective
To simulate how real customer support systems operate and evaluate an agent’s ability to resolve tickets efficiently using structured decision-making.

---

## ⚙️ Environment Design

### 🔁 API Methods

- `reset()` → Initializes a new ticket (episode start)
- `step(action)` → Processes agent action and returns:
  - observation
  - reward
  - done
  - info
- `state()` → Returns current internal environment state

---

## 🧩 Task Design

The environment includes multiple real-world scenarios:

### 🟢 Easy
- Simple billing issues  
- Example: *"My payment failed during checkout"*

### 🟡 Medium
- Technical issues requiring diagnosis  
- Example: *"The app crashes when uploading files"*

### 🔴 Hard
- Account-related queries requiring resolution  
- Example: *"I forgot my password and cannot log in"*

---

## 🤖 Agent Interaction (Multi-Step)

Each episode consists of **3 steps**:

1. **Step 1 → Category Classification**
   - billing / technical / general

2. **Step 2 → Priority Assignment**
   - low / medium / high

3. **Step 3 → Response Generation**
   - meaningful resolution message

---

## 💰 Reward Function

The reward is **progressively assigned** across steps:

| Step | Criteria | Reward |
|------|--------|--------|
| 1 | Correct category | +0.5 |
| 2 | Correct priority | +0.3 |
| 3 | Good response | +0.2 |

- Incorrect classification is penalized
- Final score is normalized between **0 and 1**
- Encourages **partial progress**, not just final success

---

## 📊 Observation Space

```json
{
  "ticket": "Customer complaint text"
}
