'''
Inspired by: Moustafa Alzantot
https://medium.com/@m.alzantot/deep-reinforcement-learning-demysitifed-episode-2-policy-iteration-value-iteration-and-q-978f9e89ddaa
'''

import gym
import random
import numpy as np


def value_iteration(env, gamma=1.0, eps=1e-20, max_iterations=100000):
    V = np.zeros(env.nS)
    Q = np.zeros((env.nS, env.nA))
    for i in range(max_iterations):
        old_V = np.copy(V)
        for s in range(env.nS):
            for a in range(env.nA):
                env.P[s][a][0]
                Q[s][a] = gamma * sum(r/gamma + p * V[s_] for p, s_, r, _ in env.P[s][a])
            V[s] = max(Q[s])
        if np.sum(np.fabs(V - old_V)) < eps:
            print('Value iteration done with {} iterations.'.format(i))
            break
    return V, Q

def extract_policy(env, Q):
    policy = [np.argmax(Q[s]) for s in range(env.nS)]
    return policy

def evaluate_policy(env, policy, n=1000):
    success = 0
    for _ in range(n):
        success += run_episode(env, policy)
    print('Our policy performs well in {}% of times.'.format(success/n*100))

def run_episode(env, policy, render=False, max_iterations=10000000):
    obs = env.reset()
    for _ in range(max_iterations):
        if render:
            env.render()
        obs, reward, done, _ = env.step(policy[obs])
        if done:
            if render:
                env.render()
            return reward
    return 0

if __name__ == '__main__':
    env = gym.make('FrozenLake8x8-v0')
    env.env.P
    V, Q = value_iteration(env)
    opt_policy = extract_policy(env, Q)
    evaluate_policy(env, opt_policy)
    run_episode(env, opt_policy, render=True)