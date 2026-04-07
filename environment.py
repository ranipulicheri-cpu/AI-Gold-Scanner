class GoldEnv:
    def __init__(self):
        self.state = None

    def reset(self):
        # Start with a sample composition
        self.state = {"gold": 90, "copper": 10}
        return self.state

    def step(self, action):
        # Action = predicted gold percentage
        true_gold = self.state["gold"]
        reward = max(0.0, 1.0 - abs(true_gold - action) / 100)
        done = True
        return self.state, reward, done

    def state(self):
        return self.state
