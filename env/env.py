from abc import ABC, abstractmethod
import numpy as np
from enum import Enum

from numpy import inf

from learning.normalizer import Normalizer

class Env(ABC):
    class Terminate(Enum):
        Null = 0
        Fail = 1
        Succ = 2

    def __init__(self, args, enable_draw):
        self.enable_draw = enable_draw
        return

    # rl interface

    @abstractmethod
    def get_num_agents(self):
        return 0

    @abstractmethod
    def record_state(self, agent_id):
        pass

    @abstractmethod
    def record_goal(self, agent_id):
        pass

    @abstractmethod
    def set_action(self, agent_id, action):
        pass

    @abstractmethod
    def get_action_space(self, agent_id):
        pass

    @abstractmethod
    def get_state_size(self, agent_id):
        pass

    @abstractmethod
    def get_goal_size(self, agent_id):
        pass

    @abstractmethod
    def get_action_size(self, agent_id):
        pass

    @abstractmethod
    def get_num_actions(self, agent_id):
        pass

    @abstractmethod
    def log_val(self, agent_id, val):
        pass

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
        action_size = self.get_action_size()
        return np.zeros(action_size)

    def build_action_scale(self, agent_id):
        action_size = self.get_action_size()
        return np.ones(action_size)

    def build_action_bound_min(self, agent_id):
        action_size = self.get_action_size()
        return -inf * np.ones(action_size)

    def build_action_bound_max(self, agent_id):
        action_size = self.get_action_size()
        return inf * np.ones(action_size)

    def build_state_norm_groups(self, agent_id):
        state_size = self.get_state_size(agent_id)
        return Normalizer.NORM_GROUP_SINGLE * np.ones(state_size, dtype=np.int32)

    def build_goal_norm_groups(self, agent_id):
        goal_size = self.get_goal_size(agent_id)
        return Normalizer.NORM_GROUP_SINGLE * np.ones(goal_size, dtype=np.int32)

    @abstractmethod
    def calc_reward(self, agent_id):
        return 0

    @abstractmethod
    def get_reward_min(self, agent_id):
        return 0

    @abstractmethod
    def get_reward_max(self, agent_id):
        return 1

    @abstractmethod
    def get_reward_fail(self, agent_id):
        return self.get_reward_min(agent_id)

    @abstractmethod
    def get_reward_succ(self, agent_id):
        return self.get_reward_max(agent_id)

    @abstractmethod
    def is_episode_end(self):
        return False


    @abstractmethod
    def check_valid_episode(self):
        return True

    @abstractmethod
    def set_sample_count(self, count):
        pass

    @abstractmethod
    def set_mode(self, mode):
        pass