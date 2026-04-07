from environment import GoldEnv

print("[START] AI Gold Finder Inference")

env = GoldEnv()
state = env.reset()
print("[STEP] Initial state:", state)

# Example prediction (AI agent guesses gold percentage)
action = 90
state, reward, done = env.step(action)

print("[STEP] Action:", action)
print("[STEP] Reward:", reward)
print("[END] Finished inference")
