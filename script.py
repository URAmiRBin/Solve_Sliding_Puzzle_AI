import problem
import algorithms
import sys
from copy import deepcopy

print("Initialization Phase")
state = []
for i in range(3):
    state.append([])
    a, b, c = input().split()
    state[i].append(int(a))
    state[i].append(int(b))
    state[i].append(int(c))
puzzle = problem.Problem(state)
if sys.argv[1] == "dfs":
    algorithms.dfs(puzzle)
elif sys.argv[1] == "bfs":
    algorithms.bfs(puzzle)
elif sys.argv[1] == "bi":
    algorithms.bidirectional(puzzle)
elif sys.argv[1] == "uni":
    algorithms.uniform_cost(puzzle)
elif sys.argv[1] == "as":
    algorithms.a_star(puzzle)
elif sys.argv[1] == "log":
    parents = [[deepcopy(puzzle.state), "NOP", "NOA", 5]]
    parent = deepcopy(puzzle.state)
    x = algorithms.parent_distance(parent, parents)
    x += 1
    print(x)
