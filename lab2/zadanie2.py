"""
Gra w zapałki

Mamy do dyspozycji pewną liczbę N zapałek.
W grze bierze udział dwóch graczy, którzy na przemian zabierają
1 lub 2 zapałki.
Przegrywa ten gracz, który zabiera zapałki jako ostatni.
Przeciwnik będzie grał w sposób losowy.
"""

import numpy as np

def Q_next(V, gamma):
    Q = np.zeros((11, 2))

    # Stan 0
    Q[0, 0] = 1 * (0 + gamma * V[0])
    Q[0, 1] = 1 * (0 + gamma * V[0])

    # Stan 1
    Q[1, 0] = 1 * (0 + gamma * V[0])
    Q[1, 1] = 1 * (0 + gamma * V[0])

    # Stan 2
    Q[2, 0] = 1 * (1 + gamma * V[0])  # ruch zwycięzki
    Q[2, 1] = 1 * (0 + gamma * V[0])

    # Stan 3
    Q[3, 0] = 0.5 * (0 + gamma * V[0]) + 0.5 * (0 + gamma * V[1])
    Q[3, 1] = 1 * (1 + gamma * V[0])

    # Stan 4
    Q[4, 0] = 0.5 * (0 + gamma * V[1]) + 0.5 * (0 + gamma * V[2])
    Q[4, 1] = 0.5 * (0 + gamma * V[0]) + 0.5 * (0 + gamma * V[1])

    # Stan 5
    Q[5, 0] = 0.5 * (0 + gamma * V[2]) + 0.5 * (0 + gamma * V[3])
    Q[5, 1] = 0.5 * (0 + gamma * V[1]) + 0.5 * (0 + gamma * V[2])

    # Stan 6
    Q[6, 0] = 0.5 * (0 + gamma * V[3]) + 0.5 * (0 + gamma * V[4])
    Q[6, 1] = 0.5 * (0 + gamma * V[2]) + 0.5 * (0 + gamma * V[3])

    # Stan 7
    Q[7, 0] = 0.5 * (0 + gamma * V[4]) + 0.5 * (0 + gamma * V[5])
    Q[7, 1] = 0.5 * (0 + gamma * V[3]) + 0.5 * (0 + gamma * V[4])

    # Stan 8
    Q[8, 0] = 0.5 * (0 + gamma * V[5]) + 0.5 * (0 + gamma * V[6])
    Q[8, 1] = 0.5 * (0 + gamma * V[4]) + 0.5 * (0 + gamma * V[5])

    # Stan 9
    Q[9, 0] = 0.5 * (0 + gamma * V[6]) + 0.5 * (0 + gamma * V[7])
    Q[9, 1] = 0.5 * (0 + gamma * V[5]) + 0.5 * (0 + gamma * V[6])

    # Stan 10
    Q[10, 0] = 0.5 * (0 + gamma * V[7]) + 0.5 * (0 + gamma * V[8])
    Q[10, 1] = 0.5 * (0 + gamma * V[6]) + 0.5 * (0 + gamma * V[7])

    return Q


if __name__ == "__main__":
    N = 10
    # Wypełniam funkcje wartości
    V_initial = np.zeros(N)
    V = V_initial
    for i in range(5):
        Q = Q_next(V, gamma=1)
        V = np.max(Q, axis=1)
        print(Q)

    
