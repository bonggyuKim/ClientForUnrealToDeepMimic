import socket
import time
# from learning.rl_world import RLWorld
# from learning.rl_agent import RLAgent
import learning.agent_builder as AgentBuilder
from env.unreal_env import UnrealEnv
from util.arg_parser import ArgParser
from learning.unreal_world import UnrealRL
import learning.tf_util as TFUtil
import numpy as np


def build_arg_parser(filename):
    arg_parser = ArgParser()
    succ = arg_parser.load_file(filename)
    return arg_parser


def convert_data_to_float(data):
    global agentNum
    global agentBehavior
    global needNewAction
    dataArray = data.split(" ")

    agentBehavior = int(dataArray.pop(0))
    isNeedAction = int(dataArray.pop(0))
    if(isNeedAction):
        needNewAction = True
        agentNum = int(dataArray.pop(0))

        StateArray = []
        GoalArray = []
        for dataidx in range(226):
            StateArray.append(float(dataArray[dataidx]))
        for dataidx in range(226,229):
            GoalArray.append(float(dataArray[dataidx]))

        states = np.array(StateArray)
        goals = np.array(GoalArray)
        return states, goals
    else:
        needNewAction = False
        return np.array(0), np.array(0)



def convert_data_to_string(data):
    data_out = ""
    for i in data:
        data_out += str(i) + " "
    return data_out

needNewAction = True
world = None
env = None
HOST = "192.168.0.43"
PORT = 3000
data_size = 8000

agentNum = 0
agentBehavior = 0

def main():
    global world
    global env
    global agentNum
    global needNewAction
    # Command line arguments

    # data = client.recv(data_size)
    # data = data.decode("utf-8")
    #
    # if data == '0':
    #     policy = policyList[0]
    # elif data == '1':
    #     policy = policyList[1]
    # elif data == '2':
    #     policy = policyList[2]
    # elif data == '3':
    #     policy = policyList[3]
    policyList = ['backflip', 'crawl', 'run', 'jump', 'sword_model', 'run_amp_humanoid3d_sideflip_args']

    policy = ['socket/run_amp_heading_humanoid3d_locomotion_args.txt']
    arg_parser = []
    for i in policy:
        arg = build_arg_parser(i)
        arg_parser.append(arg)
    env = UnrealEnv(arg_parser, enable_draw=True)
    world = UnrealRL(env, arg_parser)
    world.env.set_goal_size(agentBehavior, 3)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print("Socket Ready")
    #try:
    while 1:
        client, address = server.recvfrom(3001)
        data = client.decode("utf-8")
        states, goals = convert_data_to_float(data)
        world.env.set_action_bool(needNewAction)
        if(needNewAction):

            world.env.store_state(agentBehavior, states)
            world.env.store_goal(agentBehavior, goals)
            #world.env.store_goal(agentNum, goals)
            world.update(agentBehavior)
            action = world.env.set_unreal_action(agentBehavior)
            # if(tempNum!=agentNum):
            #     action = np.zeros(226)
            #     tempNum = agentNum
            action = convert_data_to_string(action)
            server.sendto(action.encode(), address)
        else:
            continue
    #except:
        #server.close()
        #main()

if __name__ == '__main__':
    main()
