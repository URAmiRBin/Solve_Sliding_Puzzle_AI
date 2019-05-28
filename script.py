import problem
import algorithms
import sys

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
elif sys.argv[1] == "log":
    print(puzzle.result([[1, 2, 3], [4, 5, 6], [7, 8, 0]], "up"))
