from copy import deepcopy

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def bfs(given_problem):
    parents = [[deepcopy(given_problem.state), "NOP", "NOA"]]
    open_list = []
    close_list = []
    open_list.append(given_problem.state)
    while not given_problem.goal_test():
        parent = open_list.pop(0)
        close_list.append(parent)
        available_actions = given_problem.actions()
        for action in available_actions:
            new_state = given_problem.result(deepcopy(given_problem.state), action)
            if new_state in close_list:
                print("REPEAT")
            elif new_state == goal:
                print("GOAL")
                for line in parents:
                    print(line)
                path(parents, deepcopy(goal))
                return
            else:
                parents.append([new_state, parent, action])
                open_list.append(new_state)
        given_problem.state = open_list[0]
    print("DID IT")
    path(parents, deepcopy(goal))


def path(given_list, find):
    restart = True
    action_sequence = []
    while restart:
        restart = False
        for item in given_list:
            if item[0] == find and item[1] != "NOP":
                restart = True
                find = item[1]
                action_sequence.append(item[2])
                break
    action_sequence = list(reversed(action_sequence))
    print(action_sequence)
    return action_sequence


def dfs(given_problem):
    parents = [[deepcopy(given_problem.state), "NOP", "NOA"]]
    action_sequence = []
    open_list = []
    close_list = []
    open_list.append(given_problem.state)
    while not given_problem.goal_test():
        parent = open_list.pop()
        close_list.append(parent)
        available_actions = given_problem.actions()
        for action in available_actions:
            new_state = given_problem.result(deepcopy(given_problem.state), action)
            if new_state in close_list:
                print("REPEAT")
            elif new_state == goal:
                print("GOAL")
                parents.append([new_state, parent, action])
                for line in parents:
                    print(line)
                return
            else:
                parents.append([new_state, parent, action])
                latest_action = action
                open_list.append(new_state)
        action_sequence.append(latest_action)
        print(action_sequence)
        given_problem.state = open_list[-1]
    print("DID IT")


def bidirectional(given_problem):
    parents = [[deepcopy(given_problem.state), "NOP", "NOA"]]
    open_list = []
    close_list = []
    open_list.append(given_problem.state)

    goal_parents = [[deepcopy(goal), "NOP", "NOA"]]
    goal_open_list = []
    goal_close_list = []
    goal_open_list.append(deepcopy(goal))
    goal_state = deepcopy(goal)

    while True:
        parent = open_list.pop(0)
        close_list.append(parent)
        available_actions = given_problem.actions()

        goal_parent = goal_open_list.pop(0)
        goal_close_list.append(goal_parent)
        goal_available_actions = given_problem.public_actions(deepcopy(goal))

        for action in available_actions:
            new_state = given_problem.result(deepcopy(given_problem.state), action)
            if new_state in close_list:
                print("REPEAT START")
            elif new_state == goal:
                print("GOAL")
                parents.append([new_state, parent, action])
                return
            else:
                parents.append([new_state, parent, action])
                open_list.append(new_state)

        for action in goal_available_actions:
            goal_new_state = given_problem.result(deepcopy(goal_state), action)
            if goal_new_state in goal_close_list:
                print("GOAL REPEAT")
            elif interaction(deepcopy(goal_close_list), close_list):
                found = w_interaction(deepcopy(goal_close_list), close_list)
                print("BIGOAL")
                goal_parents.append([goal_new_state, goal_parent, action])
                mix(path(parents, found), path(goal_parents, found))
                print("PARENTS")
                for line in parents:
                    print(line)
                print("GOAL PARENTS")
                for line in goal_parents:
                    print(line)
                return
            else:
                goal_parents.append([goal_new_state, goal_parent, action])
                goal_open_list.append(goal_new_state)

        goal_state = goal_open_list[0]
        given_problem.state = open_list[0]


def mix(list1, list2):
    action_sequence = []
    for action in list1:
        action_sequence.append(action)
    list2 = list(reversed(list2))
    for i in range(len(list2)):
        if list2[i] == "up":
            list2[i] = "down"
        elif list2[i] == "down":
            list2[i] = "up"
        elif list2[i] == "left":
            list2[i] = "right"
        elif list2[i] == "right":
            list2[i] = "left"
        action_sequence.append(list2[i])
    print(action_sequence)


def interaction(first_list, second_list):
    for item in first_list:
            if item in second_list:
                print("interaction found at", item)
                return True
    return False


def w_interaction(first_list, second_list):
    for item in first_list:
            if item in second_list:
                print("interaction found at", item)
                return item
    return -1


def uniform_cost(given_problem):
    open_list = []
    close_list = []
    open_list.append(given_problem.state)
    while not given_problem.goal_test():
        close_list.append(open_list.pop(0))
        available_actions = given_problem.actions()
        for action in available_actions:
            new_state = given_problem.result(deepcopy(given_problem.state), action)
            if new_state in close_list:
                print("DONE")
            else:
                open_list.append(new_state)
        given_problem.state = open_list[0]
    print("DID IT")


def man_distance(state, target, given_problem):
    distance = 0
    for line in range(3):
        for col in range(3):
            if state[line][col] is not target[line][col]:
                x, y = given_problem.find(state[line][col], deepcopy(target))
                distance += abs(x - line) + abs(y - col)
    return distance


def find_best(list):
    min = 100
    min_id = 0
    for item in range(len(list)):
        if list[item][1] < min:
            min = list[item][1]
            min_id = item
    print("BEST CHOICE IS ", list[min_id][0], " with distance ", min)
    return min_id


def parent_distance(parent, parents):
    for i in range(len(parents)):
        if parents[i][0] == parent:
            return int(parents[i][3])
    print("FUCK")


def a_star(given_problem):
    parents = [[deepcopy(given_problem.state), "NOP", "NOA", 0]]
    open_list = []
    close_list = []
    open_list.append([given_problem.state, man_distance(given_problem.state, goal, given_problem)])
    id = 0
    while not given_problem.goal_test():
        parent = open_list.pop(id)
        close_list.append(parent[0])
        available_actions = given_problem.actions()
        for action in available_actions:
            new_state = given_problem.result(deepcopy(given_problem.state), action)
            if new_state in close_list:
                print("REPEAT")
            else:
                x = parent_distance(parent[0], parents)
                x += 1
                parents.append([new_state, parent[0], action, x])
                open_list.append([new_state, man_distance(new_state, goal, given_problem), x])
        id = find_best(open_list)
        given_problem.state = open_list[id][0]
    parents.append([new_state, parent[0], action, 0])
    for i in parents:
        print(i)
    print("DID IT")
    path(parents, deepcopy(goal))
