state = []


def init():
    print("Initialization Phase")
    for i in range(3):
        state.append([])
        a, b, c = input().split()
        state[i].append(int(a))
        state[i].append(int(b))
        state[i].append(int(c))


def goal_test():
    print("Checking Goal")
    if state is [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        return True
    return False


def actions():
    action_list = ["up", "down", "left", "right"]
    if 0 in state[0]:
        action_list.remove("up")
    elif 0 in state[2]:
        action_list.remove("down")

    if 0 in [row[0] for row in state]:
        action_list.remove("left")
    elif 0 in [row[2] for row in state]:
        action_list.remove("right")

    return action_list


def result(pre_state, action):
    next_state = pre_state
    x, y = find(0, pre_state)
    if action is "up":
        next_state[x][y], next_state[x - 1][y] = next_state[x - 1][y], next_state[x][y]
    elif action is "down":
        next_state[x][y], next_state[x + 1][y] = next_state[x + 1][y], next_state[x][y]
    elif action is "left":
        next_state[x][y], next_state[x][y - 1] = next_state[x][y - 1], next_state[x][y]
    elif action is "right":
        next_state[x][y], next_state[x][y + 1] = next_state[x][y + 1], next_state[x][y]
    return next_state


def find(c, state):
    for i, sublist in enumerate(state):
        if c in sublist:
            return i, sublist.index(0)
    return -1


def show():
    print(state)
    print(actions())
    print(result(state, "down"))


init()
show()
