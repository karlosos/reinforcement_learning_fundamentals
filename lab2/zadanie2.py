"""
Gra w zapałki

Mamy do dyspozycji pewną liczbę N zapałek.
W grze bierze udział dwóch graczy, którzy na przemian zabierają
1 lub 2 zapałki.
Przegrywa ten gracz, który zabiera zapałki jako ostatni.
Przeciwnik będzie grał w sposób losowy.
"""

import numpy as np

N = 10

def Q_next(V, gamma):
    Q = np.zeros((N+1, 2))

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

    # Stany od 4 do N
    x = 4
    for i in range(N-3):
        Q[x + i, 0] = 0.5 * (0 + gamma * V[i+1]) + 0.5 * (0 + gamma * V[i+2])
        Q[x + i, 1] = 0.5 * (0 + gamma * V[i]) + 0.5 * (0 + gamma * V[i+1])

    return Q


V_initial = np.zeros(N)
V = V_initial

for i in range(5):
    Q = Q_next(V, gamma=1)
    V = np.max(Q, axis=1)

print(Q)
