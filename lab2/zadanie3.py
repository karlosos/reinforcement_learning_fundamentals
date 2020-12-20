
"""
Gra w zapałki

Mamy do dyspozycji pewną liczbę N zapałek.
W grze bierze udział dwóch graczy, którzy na przemian zabierają
1, 2 lub 3 zapałki.
Przegrywa ten gracz, który zabiera zapałki jako ostatni.
Przeciwnik będzie grał w sposób losowy.
"""

import numpy as np

N = 10

def Q_next(V, gamma):
    Q = np.zeros((N+1, 3))

    # Stan 0
    Q[0, 0] = 1 * (0 + gamma * V[0])
    Q[0, 1] = 1 * (0 + gamma * V[0])
    Q[0, 2] = 1 * (0 + gamma * V[0])

    # Stan 1
    Q[1, 0] = 1 * (0 + gamma * V[0])
    Q[1, 1] = 1 * (0 + gamma * V[0])
    Q[1, 2] = 1 * (0 + gamma * V[0])

    # Stan 2
    Q[2, 0] = 1 * (1 + gamma * V[0])  # ruch zwycięski
    Q[2, 1] = 1 * (0 + gamma * V[0])
    Q[2, 2] = 1 * (0 + gamma * V[0])

    # Stan 3
    Q[3, 0] = 2/3 * (0 + gamma * V[0]) + 1/3 * (0 + gamma * V[1])
    Q[3, 1] = 1 * (1 + gamma * V[0])  # ruch zwycieski
    Q[3, 2] = 1 * (0 + gamma * V[0])

    # Stan 4
    Q[4, 0] = 1/3 * (0 + gamma * V[0]) + 1/3 * (0 + gamma * V[1]) + 1/3 * (0 + gamma * V[2])
    Q[4, 1] = 2/3 * (0 + gamma * V[0]) + 1/2 * (0 + gamma * V[1]) 
    Q[4, 2] = 1 * (1 + gamma * V[0])  # ruch zwycieski

    # Stan 5
    Q[5, 0] = 1/3 * (0 + gamma * V[1]) + 1/3 * (0 + gamma * V[2]) + 1/3 * (0 + gamma * V[3])
    Q[5, 1] = 1/3 * (0 + gamma * V[0]) + 1/3 * (0 + gamma * V[1]) + 1/3 * (0 + gamma * V[2])
    Q[5, 2] = 2/3 * (0 + gamma * V[0]) + 1/3 * (0 + gamma * V[1]) 

    # Stany od 6 do N
    x = 6
    for i in range(N-5):
        Q[x + i, 0] = 1/3 * (0 + gamma * V[i+2]) + 1/3 * (0 + gamma * V[i+3]) + 1/3 * (0 + gamma * V[i+4])
        Q[x + i, 1] = 1/3 * (0 + gamma * V[i+1]) + 1/3 * (0 + gamma * V[i+2]) + 1/3 * (0 + gamma * V[i+3])
        Q[x + i, 2] = 1/3 * (0 + gamma * V[i]) + 1/3 * (0 + gamma * V[i+1]) + 1/3 * (0 + gamma * V[i+2])

    return Q

def wartosc_strategii(id):
    """
    :param id: numer strategii gdzie 0 = -1, 1 = -2, 2 = -3
    """
    V_initial = np.zeros(N+1)
    V = V_initial
    V_prev = V

    for i in range(100):
        Q = Q_next(V, gamma=1)
        V = Q[:, id]

        if np.sum(V_prev - V) == 0:
            break

        V_prev = V

    return Q

def optymalna_strategia():
    V_initial = np.zeros(N+1)
    V = V_initial
    V_prev = V

    for i in range(100):
        Q = Q_next(V, gamma=1)
        V = np.max(Q, axis=1)
        
        if np.sum(V_prev - V) == 0:
            break

        V_prev = V

    return Q


if __name__ == "__main__":
    print("V pi1")
    Q1 = wartosc_strategii(0)
    print(Q1[:, 0])
    print("V pi2")
    Q2 = wartosc_strategii(1)
    print(Q1[:, 1])
    print("V pi3")
    Q3 = wartosc_strategii(2)
    print(Q1[:, 2])
    print("Q optymalnej strategi")
    Q = optymalna_strategia()
    print(Q)
