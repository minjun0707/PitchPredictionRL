#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import gym
from gym import spaces
from gym.envs.registration import register
import predictMain


class BaseBallEnv(gym.Env):
    metadata = {'render.modes':['human']}
    # 한 에피소드마다 투수의 구종을 받음
    # 1 : 직구
    # 2 : 커브
    # 3 : 체인지업
    # 4 : 슬라이더
    # 5 : 싱커

    input = predictMain.main()
    print(input)

    def __init__(self):
        super(BaseBallEnv, self).__init__()
        
        # 학습할 야구 데이터?
        # self.df = df
        self.reward_range = (0, 500)
        self.flag_ball = 0
        self.flag_strike = 0
        self.reward = 0
        self.done = False

        # score = 공을 칠 때 얻는 +reward
        # penalty = strike 또는 out일 때 얻는 -reward
        self.score = 0
        self.penalty = 0

        # 주자의 out 횟수
        self.out = 0

        # 구종별 타율 및 타율 적용 후 액션 index
        self.actionWbatting = 0
        self.battingAvg = {'직구': 0.3, '커브': 0.2, '체인지업': 0.32, '슬라이더': 0.28, '싱커': 0.29}
        
        # Define action and observation space
        
        # Using Discrete action space
        # 3 actions Hit / Cutting / Do not hit
        self.action_space = spaces.Discrete(3)
        
        # Obeservation space
        # 0: 6가지 투구 종류
        # 1 : ball count
        # 2 : 구종별 타율
        self.observation_space = spaces.Discrete(4)
    
    def step(self, action):
        # Agent가 랜덤하게 action을 진행함
        # action을 진행하면
        # 0 : Hit the ball --> +30
        # 1 : Cutting the ball --> + 15
        # 2 : Not hitting the ball --> if flag_ball == 3 --> +30, else flag_strike == 3 --> +5
        
        # Goal : Reward가 10점 이상

        self.action = action

        if action == 0:
            self.actionWbatting = random.choices([0, 2], [self.battingAvg[self.input], 1-self.battingAvg[self.input]])

            if self.actionWbatting == 0:
                self.score = 30
                out = random.choice(['base', 'out'])


                if out == 'out':
                    self.penalty = -5
                    self.out += 1

                    if self.out == 3:
                        self.penalty = -10
                        self.out = 0

            else: # action == 2 (Fail to hitting the ball)
                self.flag_strike += 1
                self.score = 2
                if self.flag_strike == 4:
                    self.penalty = -10
                    self.flag_strike = 0


        elif action == 1:
            self.actionWbatting = random.choices([1, 2], [self.battingAvg[self.input], 1-self.battingAvg[self.input]])

            if self.actionWbatting == 1:
                self.score = 15
                out = random.choice(['foul', 'strike'])

                if out == 'out':
                    self.penalty = -5
                    self.out += 1

                    if self.out == 3:
                        self.penalty = -10
                        self.out = 0


            else: # action == 2 (Fail to hitting the ball)
                self.flag_strike += 1
                self.score = 2
                if self.flag_strike == 3:
                    self.penalty = -10
                    self.flag_strike = 0


        else: # action == 2 (Not hitting the ball)
            action = random.choice(['ball', 'strike'])
            if action == 'ball':
                self.flag_ball += 1
                self.score = 5
                if self.flag_ball == 3:
                    self.score = 30
                    self.flag_ball = 0
            if action == 'strike':
                self.flag_strike += 1
                self.score = 2
                if self.flag_strike == 3:
                    self.penalty = -10
                    self.flag_strike = 0

        self.reward = self.score + self.penalty
            
        self.done = (self.reward >= 10)
        
        return self._get_obs(), self.reward, self.done, self.done, {}
    
        
        
        
    def reset(self):
        self.reward = 0
        self.penalty = 0
        self.flag_ball = 0
        self.flag_strike = 0
        self.flag_out = 0
        self.done = False
        return self._get_obs()
    
    
    def _get_obs(self):
        # 관측한 상태 반환
        flag_list = []
        flag_list.append(self.flag_ball)
        flag_list.append(self.flag_strike)
        return self.flag_ball
    
    
    def render(self, mode='human', close=False):
        print(f"Select Action: {self.action}, Current Action: {self.actionWbatting}, Reward: {self.reward}")


# In[5]:


import inspect
print(inspect.getfile(gym))


# 환경 등록
gym.envs.register(
    id='BaseBallEnv-v0',
    entry_point='BaseBallEnv:BaseBallEnv',
    max_episode_steps=1000,)

# 등록된 환경 인스턴스화
env = gym.make('BaseBallEnv-v0')



