import random
import gym
from gym import spaces
import numpy as np
from BaseBallEnv import BaseBallEnv

print(gym.__version__)

env = gym.make('BaseBallEnv-v0')

# Initialize table with all zeros
Q = np.zeros([env.observation_space.n, env.action_space.n])
print(Q)

# Discount factor
alpha = 0.5
gamma = 0.9
dis = .99
num_episodes = 2000

# create lists to contain total rewards and steps per episode
rList = []

for i in range(1000):
    print(f' --- episode {i} --- ')
    # Reset environment and get first new observation
    state = env.reset()
    rAll = 0
    done = False

    # set epsilon
    e = 1. / ((i / 100) + 1)

    # The Q-table learning algorithm

    j = 0
    while j < 500:
        j += 1
        if np.random.rand(1) < e:
            # Choose an action by E-Greedy (with noise) picking from Q table
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        # Get new state and reward from environment
        new_state, reward, done, done2, info = env.step(action)

        # Update Q-Table with new knowledge using decay rate
        Q[state, action] = reward + dis * np.max(Q[state, :])

        rAll += reward
        state = new_state

    rList.append(rAll)
    env.render()

if (action == 0):
    action_print = 'hit the ball'

elif (action == 1):
    action_print = 'cutting the ball'

else:
    action_print = 'not hit the ball'

predict_input = BaseBallEnv.input

print('If ' + predict_input + ' is comming, You have to ' + action_print)