# inp = given input specific to user

#-------------- Part 1 -------------------#
inp_list = list(map(int, inp.splitlines()))
idx = 0
steps_tracker = 0
while idx < len(inp_list):
    step_size = inp_list[idx]
    inp_list[idx] += 1
    idx += step_size
    steps_tracker += 1
print("{} steps to reach the exit for Part 1".format(steps_tracker))

#-------------- Part 2 -------------------#
inp_list = list(map(int, inp.splitlines()))
idx = 0
steps_tracker = 0

while idx < len(inp_list):
    step_size = inp_list[idx]
    if inp_list[idx] >= 3:
        inp_list[idx] -= 1
    else:
        inp_list[idx] += 1
    idx += step_size
    steps_tracker += 1
print("{} steps to reach the exit for Part 2".format(steps_tracker))