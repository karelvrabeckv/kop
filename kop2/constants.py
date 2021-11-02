# Module constants

NUM_OF_THINGS = [4, 10, 15, 20, 22, 25, 27, 30, 32, 35, 37, 40]

NK_FILE_PREFIX = "NK/NK"
ZKC_FILE_PREFIX = "ZKC/ZKC"
ZKW_FILE_PREFIX = "ZKW/ZKW"

INST_FILE_POSTFIX = "_inst.dat"
SOL_FILE_POSTFIX = "_sol.dat"

BB = "BRANCH & BOUND"
BB_STMT = """bb(instance["M"], instance["w"], instance["c"])"""
BB_SETUP = """from algorithms.bb import bb"""

DYNAMIC = "DYNAMIC PROGRAMMING"
DYNAMIC_STMT = """dynamic(instance["n"], instance["M"], instance["w"], instance["c"])"""
DYNAMIC_SETUP = """from algorithms.dynamic import dynamic"""

GREEDY = "GREEDY HEURISTIC"
GREEDY_STMT = """greedy(instance["M"], instance["w"], instance["c"])"""
GREEDY_SETUP = """from algorithms.greedy import greedy"""

REDUX = "MODIFIED GREEDY"
REDUX_STMT = """redux(instance["M"], instance["w"], instance["c"])"""
REDUX_SETUP = """from algorithms.redux import redux"""

FPTAS = "FPTAS"
FPTAS_STMT = """fptas(instance["n"], instance["M"], instance["w"], instance["c"], e)"""
FPTAS_SETUP = """from algorithms.fptas import fptas"""
