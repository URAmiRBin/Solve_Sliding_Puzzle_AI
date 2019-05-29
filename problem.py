class Problem(object):

    def __init__(self, state):
        self.action_sequence = []
        self.state = state
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def goal_test(self):
        print("Checking Goal")
        if self.state == self.goal:
            return True
        return False

    def actions(self):
        action_list = ["up", "down", "left", "right"]
        if 0 in self.state[0]:
            action_list.remove("up")
        elif 0 in self.state[2]:
            action_list.remove("down")

        if 0 in [row[0] for row in self.state]:
            action_list.remove("left")
        elif 0 in [row[2] for row in self.state]:
            action_list.remove("right")

        return action_list

    def public_actions(self, pre_state):
        action_list = ["up", "down", "left", "right"]
        if 0 in pre_state[0]:
            action_list.remove("up")
        elif 0 in pre_state[2]:
            action_list.remove("down")

        if 0 in [row[0] for row in pre_state]:
            action_list.remove("left")
        elif 0 in [row[2] for row in pre_state]:
            action_list.remove("right")

        return action_list

    def result(self, pre_state, action):
        next_state = pre_state[:]
        x, y = self.find(0, next_state)
        if action is "up":
            next_state[x][y], next_state[x - 1][y] = next_state[x - 1][y], next_state[x][y]
        elif action is "down":
            next_state[x][y], next_state[x + 1][y] = next_state[x + 1][y], next_state[x][y]
        elif action is "left":
            next_state[x][y], next_state[x][y - 1] = next_state[x][y - 1], next_state[x][y]
        elif action is "right":
            next_state[x][y], next_state[x][y + 1] = next_state[x][y + 1], next_state[x][y]
        return next_state

    @staticmethod
    def find(c, state):
        for i, sublist in enumerate(state):
            if c in sublist:
                return i, sublist.index(c)
        print("NOT FOUND")
        return -1

    def show(self):
        print(self.state)
        print("=========================")
