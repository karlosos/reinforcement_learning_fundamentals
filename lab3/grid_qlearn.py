import random
import numpy as np


class Grid:
    def __init__(self):
        self.height = 10
        self.width = 10
        self.actions = [0, 1, 2, 3]
        self.state_count = self.height * self.width
        self.action_count = len(self.actions)

        self.policy_print_characters = {0: "<", 1: ">", 2: "^", 3: "v"}

        self.grid = np.zeros((self.height, self.width))
        # end points
        self.grid[0, 0] = 20
        self.grid[0, -1] = 20

        # obstacles
        self.grid[3, 2] = -1
        self.grid[3, 3] = -1
        self.grid[3, 4] = -1
        self.grid[3, 4] = -1
        self.grid[3, 5] = -1
        self.grid[3, 6] = -1
        self.grid[3, 7] = -1

        self.grid[2, 5] = -1
        self.grid[3, 5] = -1
        self.grid[4, 5] = -1
        self.grid[5, 5] = -1
        self.grid[6, 5] = -1
        self.grid[7, 5] = -1

    def random_position(self):
        """Find random starting position"""
        return (9, 9)
        while True:
            h = random.randrange(0, self.height)
            w = random.randrange(0, self.width)
            if self.grid[h, w] == 0:
                return (h, w)

    def is_terminal(self, state):
        """Terminal states are those with reward greater than 0"""
        if self.grid[state[0], state[1]] > 0:
            return True
        else:
            return False

    def to_string(self, state=None, policy=None):
        res = "┌" + "─" * self.width + "┐" + "\n"
        for i in range(self.height):
            res += "│"
            for j in range(self.width):
                if self.grid[i, j] == -1:
                    res += "#"
                elif self.grid[i, j] > 0:
                    res += "X"
                elif state is not None and state[0] == i and state[1] == j:
                    res += "¤"
                elif policy is not None:
                    res += self.policy_print_characters[policy[i, j]]

                else:
                    res += " "
            res += "│"
            res += "\n"
        res += "└" + "─" * self.width + "┘"
        return res

    def __str__(self):
        return self.to_string()

    def available_actions(self, state):
        actions = []
        if self.is_terminal(state):
            return actions

        h, w = state
        if h > 0:
            if self.grid[h-1, w] >= 0:
                actions.append(2)  # up
        if w > 0:
            if self.grid[h, w-1] >= 0:
                actions.append(0)  # left
        if h < self.height-1:
            if self.grid[h+1, w] >= 0:
                actions.append(3)  # down
        if w < self.width-1:
            if self.grid[h, w+1] >= 0:
                actions.append(1)  # right

        return actions


    def take_action(self, state, action):
        h, w = state
        state_next = [h, w]

        if action == 0:  # left
            state_next[1] = w-1
        if action == 1:  # right
            state_next[1] = w+1
        if action == 2:  # up
            state_next[0] = h-1
        if action == 3:  # down
            state_next[0] = h+1

        done = self.is_terminal(state_next) or self.available_actions(state_next) == []
        reward = self.grid[state_next[0], state_next[1]]
        return state_next, reward, done



def main():
    import numpy as np
    import time
    import os

    env = Grid()

    qtable = np.random.rand(env.height, env.width, env.action_count)

    epochs = 2000
    gamma = 0.6
    epsilon = 0.1

    for i in range(epochs):
        state = env.random_position()
        reward = 0
        done = False
        steps = 0


        while not done:
            h, w = state

            # count steps to finish game
            steps += 1

            # exploration
            if np.random.uniform() < epsilon:
                action = np.random.choice(env.available_actions(state))
            # best action
            else:
                action = qtable[h, w].argmax()
                available_actions = env.available_actions(state)
                if action not in available_actions:
                    action = np.random.choice(env.available_actions(state))


            # take action
            state_next, reward, done = env.take_action(state, action)

            # update qtable value with Bellman equation
            qtable[h, w, action] = reward + gamma * np.max(qtable[state_next])

            # update state
            state = state_next 

            # print(env.to_string(state=state))

        print("Epoka: ", i + 1, "kroki:", steps)

    print("Wyznaczona strategia")
    policy = np.argmax(qtable, axis=2)
    print(policy)
    print(env.to_string(policy=policy))

if __name__ == "__main__":
    main()
