import constants as c
import tester as t

print("")
print("Starting " + c.BB + ".")
t.run(c.BB, c.NK_FILE_PREFIX, 20)
print("Finished.")
print("")
print("Starting " + c.DYNAMIC + ".")
t.run(c.DYNAMIC, c.NK_FILE_PREFIX, 25)
print("Finished.")
print("")
print("Starting " + c.GREEDY + ".")
t.run(c.GREEDY, c.NK_FILE_PREFIX)
print("Finished.")
print("")
print("Starting " + c.REDUX + ".")
t.run(c.REDUX, c.NK_FILE_PREFIX)
print("Finished.")
print("")
print("Starting " + c.FPTAS + " (e = " + str(0.7) + ").")
t.run(c.FPTAS, c.NK_FILE_PREFIX, 40, 0.7)
print("Finished.")
print("")
