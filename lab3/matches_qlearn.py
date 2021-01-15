import random
import numpy as np

def take_action(state, action):
    # if losing state
    if state == 1:
        return 0, 0, True

    state_next = state - (action+1)
    # if winning move return R and state
    if state_next == 1:
        return 0, 1, True 

    # random opponents action
    action_opponent = random_action()

    # calculate reward
    R = 0
    done = False
    state_next = state_next - (action_opponent+1)

    if state_next <= 0:
        X_n = 0
        R = 1
        done = True

    return state_next, R, done

def random_action():
    return random.choice([0, 1])

def main():
    N = 10  # starting state 
    q = np.random.rand(N+1, 2)

    gamma = 0.01
    epochs = 5000
    epsilon = 0.2  # exploration

    for i in range(epochs):
        state = N
        done = False

        while not done:
            print(f"Epoka {i}/{epochs}")

            # chose action
            if random.random() < epsilon:
                action = random_action()
            else:
                action = q[state].argmax()

            # take action
            state_next, reward, done = take_action(state, action)

            # update delta
            q[state][action] = reward + gamma * q[state_next].max()
            state = state_next

    print()
    print("Macierz Q")
    print(q)

    print("Wyznaczona strategia")
    policy = np.argmax(q, axis=1)+1
    print(policy)

    print("Sprawdzenie strategii")
    print(policy[9] == 2 and 
            policy[8] == 1 and 
            policy[6] == 2 and
            policy[5] == 1 and
            policy[4] == 1 and
            policy[3] == 2 and
            policy[2] == 1)
    

if __name__ == "__main__":
    main()
