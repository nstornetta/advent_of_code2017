from itertools import repeat

# inp = input given specific to user

#---------------- Part 1 ---------------------#

def part1(inp):
	memory_blocks = list(map(int, inp.split('\t')))
	seen_state_set = set(tuple(memory_blocks))
	cycles = 0

	while tuple(memory_blocks) not in seen_state_set:
		seen_state_set.add(tuple(memory_blocks))
		reallocation_amt = max(memory_blocks)
		reallocation_idx = memory_blocks.index(reallocation_amt)
		memory_blocks[reallocation_idx] = 0
		while reallocation_amt:
			reallocation_idx = (reallocation_idx+1)%len(memory_blocks)
			memory_blocks[reallocation_idx] += 1
			reallocation_amt -= 1
		cycles += 1
	return cycles


#--------------- Part 2 ---------------------#
def part2(inp):
	memory_blocks = list(map(int, inp.split('\t')))
	seen_state_set = set(tuple(memory_blocks))

	while True:
		reallocation_amt = max(memory_blocks)
		reallocation_idx = memory_blocks.index(reallocation_amt)
		memory_blocks[reallocation_idx] = 0
		for _ in list(repeat(1, reallocation_amt)):
			reallocation_idx = (reallocation_idx+1)%len(memory_blocks)
			memory_blocks[reallocation_idx] += 1
		if tuple(memory_blocks) != inp:
			seen_state_set.add(tuple(memory_blocks))
		else:
			break
	return len(seen_state_set)

if __name__ == '__main__':
	part1(inp=inp)
	part2(inp=inp)