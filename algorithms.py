import problem
from copy import deepcopy
import queue

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
                parents.append([new_state, parent, action])
                path(parents)
                return
            else:
                parents.append([new_state, parent, action])
                open_list.append(new_state)
        given_problem.state = open_list[0]
    print("DID IT")
    path(parents)


def path(given_list):
    restart = True
    find = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
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


def dfs(given_problem):
    action_sequence = []
    open_list = []
    close_list = []
    open_list.append(given_problem.state)
    while not given_problem.goal_test():
        close_list.append(open_list.pop())
        available_actions = given_problem.actions()
        for action in available_actions:
            new_state = given_problem.result(deepcopy(given_problem.state), action)
            if new_state in close_list:
                print("REPEAT")
            elif new_state == goal:
                print("GOAL")
                return
            else:
                latest_action = action
                open_list.append(new_state)
        action_sequence.append(latest_action)
        print(action_sequence)
        given_problem.state = open_list[-1]
    print("DID IT")


def bidirectional(given_problem):
    open_list = []
    close_list = []
    open_list.append(given_problem.state)

    goal_open_list = []
    goal_close_list = []
    goal_open_list.append(deepcopy(goal))
    goal_state = deepcopy(goal)

    while True:
        close_list.append(open_list.pop(0))
        available_actions = given_problem.actions()

        goal_close_list.append(goal_open_list.pop(0))
        goal_available_actions = given_problem.public_actions(deepcopy(goal))

        for action in available_actions:
            new_state = given_problem.result(deepcopy(given_problem.state), action)
            if new_state in close_list:
                print("REPEAT START")
            elif new_state == goal:
                print("GOAL")
                return
            else:
                open_list.append(new_state)

        for action in goal_available_actions:
            goal_new_state = given_problem.result(deepcopy(goal_state), action)
            if goal_new_state in goal_close_list:
                print("GOAL REPEAT")
            elif interaction(deepcopy(goal_open_list), open_list):
                print("BIGOAL")
                return
            else:
                goal_open_list.append(goal_new_state)

        goal_state = goal_open_list[0]
        given_problem.state = open_list[0]


def interaction(first_list, second_list):
    for item in first_list:
            if item in second_list:
                print("interaction found")
                return True
    return False


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
