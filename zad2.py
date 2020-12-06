
def funkcja_wartosci_1(g):
    print("V1(1)=", -1 * g**0 - 1 * g**1 - 1 * g**2 -1* g**3 -1 * g**4 -1*g**5)
    print("V1(2)=", -1 * g**0 - 1 * g**1 - 1 * g**2 -1* g**3 -1 * g**4 )
    print("V1(3)=", -1 * g**0 - 1 * g**1 - 1 * g**2 -1* g**3 )
    print("V1(4)=", -1 * g**0 - 1 * g**1 - 1 * g**2 )
    print("V1(5)=", -1 * g**0 - 1 * g**1 )
    print("V1(6)=", -1 * g**0 - 1 )
    print("V1(7)=", 0)

def funkcja_wartosci_2(g):
    print("V2(1)=", -9/4 * g**0 -9/4 * g**1 - 9/4 * g**2)
    print("V2(2)=", -9/4 * g**0 -9/4 * g**1 - 9/4 * g**2)
    print("V2(3)=", -9/4 * g**0 -9/4 * g**1)
    print("V2(4)=", -9/4 * g**0 -9/4 * g**1)
    print("V2(5)=", -9/4 * g**0)
    print("V2(6)=", -9/4 * g**0)
    print("V2(7)=", 0)

def funkcja_wartosci_akcji_2_1(g):
    print("Q2(1,1)=", -1 * g** 0 -9/4 * g**1 -9/4 * g**2 - 9/4 * g**2)
    print("Q2(2,1)=", -1 * g**0 -9/4 * g**1 -9/4 * g**2)
    print("Q2(3,1)=", -1 * g**0 -9/4 * g**1 -9/4 * g**2)
    print("Q2(4,1)=", -1 * g**0 -9/4 * g**1)
    print("Q2(5,1)=", -1 * g**0 -9/4 * g**1)
    print("Q2(6,1)=", -1 * g**0)
    print("Q2(7,1)=", 0)



g = 1
print(f"g={g}")
funkcja_wartosci_1(g)
print(" ")
funkcja_wartosci_2(g)
print("==========")

g = 0.9
print(f"g={g}")
funkcja_wartosci_1(g)
print(" ")
funkcja_wartosci_2(g)
print("==========")

g = 0.7
print(f"g={g}")
funkcja_wartosci_1(g)
print(" ")
funkcja_wartosci_2(g)
print("==========")


print("==========")
print("Do wyznaczenia strategii zachlannej")
print("==========")
funkcja_wartosci_2(g=0.9)
print(" ")
funkcja_wartosci_akcji_2_1(g=0.9)
