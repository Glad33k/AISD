from array import array
from ctypes import Array
from typing import Tuple

# zad1.1
age = int(input("Wprowadz swoj wiek: "))
if 18 <= age <= 100:
    print("Autoryzacja uzyskana")
else:
    print("Odmowa")

# b

a = int(input("Wprowadz liczbe:"))
if a > 0:
    print("|a|=", a)
else:
    print("|a|=", -a)

# zad1.2
n = 5
s = 1
for i in range(1, n + 1):
    s *= i  # i=1,s=1/i=2,s=2/i=3,s=6/i=4,s=24/i=5,s=120/
print(s)

a = 1
c = 0
while a < 3:
    for b in range(1, 3):
        c += a + b + 1  # b=1,c=3,a=1/b=2,c=15,a=1/b=1,c=27,a=2/b=2,c=40,a=2
        c += 8  # c=11/c=23/c=35/c=48
    a += 1
    print(c)


# zad 1.3

def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    pocz = 0
    koniec = len(numbers) - 1
    while pocz <= koniec:
        srodek = (pocz + koniec) // 2
        if numbers[srodek] == value:
            return True, srodek
        elif numbers[srodek] < value:
            pocz = srodek + 1
        else:
            koniec = srodek - 1
    return False, -1


ints = array('I', [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71])
result = binary_search(ints, 72)
print(result)


licznikfunkcji=0

def fib(n):
    global licznikfunkcji
    if n<=1: return n
    else:
        licznikfunkcji+=1
        return fib(n-1)+fib(n-2)



print(fib(6),"a obliczeń mamy ", licznikfunkcji)

#petla
print(" \n\n")

suma=0
pierwsza=0
druga=1
licznik=0
for i in range (0,n):
    suma=pierwsza+druga
    licznik+=1
    pierwsza=druga
    druga=suma

print("Oto wynik suma ",suma,"A liczba sum to: ",licznik)
