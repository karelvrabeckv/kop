# Module constants

DATA_FOLDER = "data"

BF = "BRUTE FORCE"
BF_STMT = """bf(instance["M"], instance["w"], instance["c"])"""
BF_SETUP = """from algorithms.bf import bf"""

BB = "BRANCH & BOUND"
BB_STMT = """bb(instance["M"], instance["w"], instance["c"])"""
BB_SETUP = """from algorithms.bb import bb"""

DP = "DYNAMIC PROGRAMMING"
DP_STMT = """dp(instance["n"], instance["M"], instance["w"], instance["c"])"""
DP_SETUP = """from algorithms.dp import dp"""

GR = "GREEDY HEURISTIC"
GR_STMT = """gr(instance["M"], instance["w"], instance["c"])"""
GR_SETUP = """from algorithms.gr import gr"""
