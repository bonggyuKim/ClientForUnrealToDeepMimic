import numpy as np
from env.env import Env
from numpy import inf
from env.action_space import ActionSpace
from learning.normalizer import Normalizer


class UnrealEnv(Env):
    def __init__(self, args, enable_draw):
        super().__init__(args, enable_draw)

        self.state_size = 226  # 왜인지는 모르겠지만 콘솔창에 뜸  #드리블은 공추가로 197개
        self.goal_size = 0  # 왜인지는 모르겠지만 코드에서 이렇게 씀
        self.action_size = 28  # 왜인지는 모르겠지만 논문에서 이렇게 씀
        self.state = np.array(226)
        self.goal = np.array(0)
        self.action = None
        self.need_action = True

    # def get_state_size(self, agent_id):
    #     return self.state_size
    #
    # def get_goal_size(self, agent_id):
    #     return self.goal_size
    #
    # def get_action_size(self, agent_id):
    #     return self.action_size
    #
    # def build_state_offset(self, agent_id):
    #     return
    #
    # def build_state_norm_groups(self, agent_id):
    #     state_size = self.get_state_size(agent_id)
    #     return Normalizer.NORM_GROUP_SINGLE * np.ones(state_size, dtype=np.int32)
    #
    # def build_goal_norm_groups(self, agent_id):
    #     goal_size = self.get_goal_size(agent_id)
    #     return Normalizer.NORM_GROUP_SINGLE * np.ones(goal_size, dtype=np.int32)
    #
    # def build_state_offset(self, agent_id):
    #     state_size = self.get_state_size(agent_id)
    #     return np.zeros(state_size)
    #
    # def build_state_scale(self, agent_id):
    #     state_size = self.get_state_size(agent_id)
    #     return np.ones(state_size)
    #
    # def build_goal_offset(self, agent_id):
    #     goal_size = self.get_goal_size(agent_id)
    #     return np.zeros(goal_size)
    #
    # def build_goal_scale(self, agent_id):
    #     goal_size = self.get_goal_size(agent_id)
    #     return np.ones(goal_size)
    #
    # def build_action_offset(self, agent_id):
    #     action_size = self.get_action_size(agent_id)
    #     return np.zeros(action_size)
    #
    # def build_action_scale(self, agent_id):
    #     action_size = self.get_action_size(agent_id)
    #     return np.ones(action_size)
    #
    # def build_action_bound_min(self, agent_id):
    #     action_size = self.get_action_size(agent_id)
    #     return -inf * np.ones(action_size)
    #
    # def build_action_bound_max(self, agent_id):
    #     action_size = self.get_action_size(agent_id)
    #     return inf * np.ones(action_size)
    #
    # def get_reward_min(self, agent_id):
    #     return 0
    #
    # def get_reward_max(self, agent_id):
    #     return 1
    #
    # def get_reward_fail(self, agent_id):
    #     return self.get_reward_min(agent_id)
    #
    # def get_reward_succ(self, agent_id):
    #     return self.get_reward_max(agent_id)
    #
    # def record_state(self, agent_id):
    #     return
    #
    # def record_goal(self, agent_id):
    #     return
    #
    # def calc_reward(self, agent_id):
    #     return
    #
    # def set_action(self, agent_id, action):
    #     print(action)
    #     return
    #
    # def check_terminate(self, agent_id):
    #     return
    #
    # def enable_amp_task_reward(self):
    #     return
    #
    # def get_amp_obs_scale(self):
    #     return np.ones(226)
    #
    # def get_amp_obs_offset(self):
    #     return np.zeros(226)
    #
    # def get_amp_obs_size(self):
    #     return 226
    #
    # def get_amp_obs_norm_group(self):
    #     return np.zeros(226)
    #
    # def record_amp_obs_expert(self):
    #     return
    #
    # def record_amp_obs_agent(self):
    #     return
    #
    # def update(self, timestep):
    #     return
    #
    # def get_action_space(self, agent_id):
    #     return ActionSpace(1)

#모르겠다 나도

        return





    # rl interface

    def get_num_agents(self):
        return 1

    def set_action_bool(self, need):
        self.need_action = need

    def need_new_action(self, agent_id):
        return True

    def record_state(self, agent_id):
        return self.state

    def store_state(self, agent_id, state):
        self.state = state

    def store_goal(self, agent_id, goal):
        self.goal = goal

    def set_goal_size(self, agent_id, goal_size):
        self.goal_size = goal_size

    def record_goal(self, agent_id):
        return self.goal

    def get_action_space(self, agent_id):
        return ActionSpace(ActionSpace(1))

    def set_action(self, agent_id, action):
        self.action = action


    def set_unreal_action(self, agent_id):
        return self.action

    def get_state_size(self, agent_id):
        return self.state_size

    def get_goal_size(self, agent_id):
        return self.goal_size

    def get_action_size(self, agent_id):
        return self.action_size

    def get_num_actions(self, agent_id):
        return 0

    def build_state_offset(self, agent_id):
        state_size = self.get_state_size(agent_id)
        return np.zeros(state_size)

    def build_state_scale(self, agent_id):
        state_size = self.get_state_size(agent_id)
        return np.ones(state_size)

    def build_goal_offset(self, agent_id):
        goal_size = self.get_goal_size(agent_id)
        return np.zeros(goal_size)

    def build_goal_scale(self, agent_id):
        goal_size = self.get_goal_size(agent_id)
        return np.ones(goal_size)

    def build_action_offset(self, agent_id):
        action_size = self.get_action_size(agent_id)
        return np.zeros(action_size)

    def build_action_scale(self, agent_id):
        action_size = self.get_action_size(agent_id)
        return np.ones(action_size)

    def build_action_bound_min(self, agent_id):
        action_size = self.get_action_size(agent_id)
        return -inf * np.ones(action_size)

    def build_action_bound_max(self, agent_id):
        action_size = self.get_action_size(agent_id)
        return inf * np.ones(action_size)

    def build_state_norm_groups(self, agent_id):
        state_size = self.get_state_size(agent_id)
        return Normalizer.NORM_GROUP_SINGLE * np.ones(state_size)

    def build_goal_norm_groups(self, agent_id):
        goal_size = self.get_goal_size(agent_id)
        return Normalizer.NORM_GROUP_SINGLE * np.ones(goal_size)

    def calc_reward(self, agent_id):
        return

    def get_reward_min(self, agent_id):
        return 0

    def get_reward_max(self, agent_id):
        return 1

    def get_reward_fail(self, agent_id):
        return self.get_reward_min(agent_id)

    def get_reward_succ(self, agent_id):
        return self.get_reward_max(agent_id)

    def enable_amp_task_reward(self):
        return False

    def get_amp_obs_scale(self):
        return np.ones(226)

    def get_amp_obs_offset(self):
        return np.zeros(226)

    def get_amp_obs_size(self):
        return 226

    def get_amp_obs_norm_group(self):
        return np.zeros(226)

    def record_amp_obs_expert(self, agent_id):
        return

    def record_amp_obs_agent(self, agent_id):
        return

    def is_episode_end(self):
        return False

    def check_terminate(self, agent_id):
        return

    def check_valid_episode(self):
        return

    def log_val(self, agent_id, val):
        return

    def set_sample_count(self, count):
        return

    def set_mode(self, mode):
        return
