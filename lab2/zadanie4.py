"""
Gra w ruletkę.
Obstawiamy wielokrotność 1 zł na kolor.
Porawdopobieństwo wygranej p = 18/37

Wyznaczyć optymalną strategię obstawiania, tak aby wygrać dokładnie 100 zł.
Sporządzić wykres optymalnej funkcji wartości V*(x) i optymalnej strategii pi*(x)

Stan x określa kapitał gracza x in {0, 1, 2, 3, ..., 100}
Możliwe akcje a w stanie x: a in {1, ..., min(x, 100-x)}
    Czyli dla maksymalna akcja = 50 (bo dla x = 50 możemy postawić maksymalnie 50).
    Co dla stanu 0? Raczej nie ma żadnej możliwej akcji.
Oczekiwana wartość wzmocnienia: R_{xy} = 1 dla y = 100, w innych przypadkach R=0
Prawodopodobieństwa przejścia p dla y = x+a (wygrana), w innym przypadku (1-p)
"""


import numpy as np
import matplotlib.pyplot as plt

p = 18 / 37


def Q_next(V, gamma):
    Q = np.zeros((101, 50))  # każdy maksymalnie będzie 50 stanów (dla x = 50)

    for x in range(101):  # dla wszystkich stanów
        for a in range(50):  # dla wszystkich akcji
            if a > min(x, 100 - x):  # niemożliwe akcje
                Q[x, a] = 0
            else:
                loss = (1 - p) * (0 + gamma * V[x - a])
                R = 1 if x + a == 100 else 0
                win = p * (R + gamma * V[x + a])
                Q[x, a] = p * win + (1 - p) * loss

    return Q


def optymalna_strategia():
    V_initial = np.zeros(101)  # dla każdego stanu {0, 1, 2, ..., 100}
    V = V_initial
    V_prev = V

    while True:
        Q = Q_next(V, gamma=1)
        V = np.max(Q, axis=1)

        if np.sum(V_prev - V) == 0:
            break

        V_prev = V

    return Q


if __name__ == "__main__":
    print("Q optymalnej strategi")
    Q = optymalna_strategia()
    print(Q[50, :])

    # TODO: coś mi nie pasuje, bo:
    # występują skoki
    # dla stanu 50 zł powinno sie postawić złotówkę, w innych przypadkach trzeba grać va bank
    # dla stanu 50 zł wartość akcji jest wszędzie prawie identyczna

    V = np.max(Q, axis=1)
    plt.plot(V)
    plt.title("Optymalna funkcja wartości $V^*(x)$")
    plt.show()
    pi = np.argmax(Q, axis=1)
    plt.plot(pi)
    plt.title("Optymalna strategia $\pi^*(x)$")
    plt.show()
    print(Q)
