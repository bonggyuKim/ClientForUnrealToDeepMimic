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
    dataArray = data.split(" ")
    #dataArray.pop(454)
    #print(dataArray)
    dataArray.pop(0)
    dataArray.pop(0)
    agentNum.append(int(dataArray.pop(0)))
    agentNum.append(int(dataArray.pop(226)))
    floatArray = []
    stateSize = 226

    for i in range(0,2):
        for j in range(stateSize):
            floatArray.append((float(dataArray[i*stateSize + j])))
    states = np.array(floatArray)
    return states


def convert_data_to_string(data):
    data_out = ""
    for i in data:
        data_out += str(i) + " "
    return data_out


world = None
env = None
HOST = "192.168.0.43"
PORT = 3000
data_size = 8000

agentNum = []


def main():
    global world
    global env
    global agentNum

    policy = ['args/run_amp_humanoid3d_walk_args.txt', 'args/run_amp_humanoid3d_walk_args.txt']
    arg_parser1 = build_arg_parser(policy[0])
    arg_parser2 = build_arg_parser(policy[1])
    arg_parser = [arg_parser1, arg_parser2]
    env = UnrealEnv(arg_parser, enable_draw=True)
    world = UnrealRL(env, arg_parser)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print("Socket Ready")
    #try:
    while 1:
        client, address = server.recvfrom(30000)
        action = []
        data = client.decode("utf-8")
        states = convert_data_to_float(data)

        world.env.store_state(agentNum[0], states[0:226])
        world.update(agentNum[0])
        action.extend(world.env.set_unreal_action(agentNum[0]))

        world.env.store_state(agentNum[1], states[226:])
        world.update(agentNum[1])
        action.extend(world.env.set_unreal_action(agentNum[1]))

        action = convert_data_to_string(action)
        server.sendto(action.encode(), address)

    #except:
        #server.close()
        #main()

if __name__ == '__main__':
    main()