import constants as c
import tester as t

print("")
print("Starting " + c.BF + " " + c.ALL_INSTANCES + "...")
t.run(c.BF, c.ALL_INSTANCES, c.LIMIT, c.ZR_INST_FILE_PATH_PREFIX)
print("Finished.")
print("")
print("Starting " + c.BF_BETTER + " " + c.ALL_INSTANCES + "...")
t.run(c.BF_BETTER, c.ALL_INSTANCES, c.LIMIT, c.ZR_INST_FILE_PATH_PREFIX)
print("Finished.")
print("")
print("Starting " + c.BB + " " + c.ALL_INSTANCES + "...")
t.run(c.BB, c.ALL_INSTANCES, c.LIMIT, c.ZR_INST_FILE_PATH_PREFIX)
print("Finished.")
print("")
