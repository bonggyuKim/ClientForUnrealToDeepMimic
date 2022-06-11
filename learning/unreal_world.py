from env.unreal_env import UnrealEnv
import learning.tf_util as TFUtil
import learning.agent_builder as AgentBuilder


class UnrealRL(object):

    def __init__(self, environment, arg_parser):
        TFUtil.disable_gpu()
        self.env = environment
        self.agents = []
        self.arg_parser = arg_parser
        self.build_agents()
        self.model_files = []
        self.output_path = []
        self.int_output_path = []

    def build_agents(self):
        num_agents = 1
        agent_files = []
        model_files = []

        for i in range(num_agents):
            agent_files.extend(self.arg_parser[i].parse_strings('agent_files'))
            #assert (len(agent_files) == num_agents or len(agent_files) == 0)

            model_files.extend(self.arg_parser[i].parse_strings('model_files'))
            #assert (len(model_files) == num_agents or len(model_files) == 0)

            output_path = self.arg_parser[i].parse_string('output_path')
            int_output_path = self.arg_parser[i].parse_string('int_output_path')

        for i in range(num_agents):
            curr_file = agent_files[i]
            curr_agent = self._build_agent(i, curr_file)

            if curr_agent is not None:
                curr_agent.output_dir = output_path
                curr_agent.int_output_dir = int_output_path

                if len(model_files[i]) > 0:
                    curr_model_file = model_files[i]
                    if curr_model_file != 'none':
                        curr_agent.load_model(curr_model_file)

            self.agents.append(curr_agent)
        return

    def _build_agent(self, id, agent_file):
        if agent_file == 'none':
            agent = None
        else:
            agent = AgentBuilder.build_agent(self, id, agent_file)
            assert (agent is not None), 'Failed to build agent {:d} from: {}'.format(id, agent_file)

        return agent

    def update(self, agents_num):
        self.agents[agents_num].update(agents_num)
        return

    def update_env(self, timestep):
        self.env.update(timestep)
        return