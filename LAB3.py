from array import array
from ctypes import Array
from typing import Tuple
# zad1

count=0
def numbersrek(n: int):
    global count
    count+=1
    print(n)
    if n == 0:
        return 0
    return numbersrek(n - 1)





def numbersn(n: int):
    global count
    count = 0
    while n >= 0:
        count+=1
        print(n)
        n -= 1

numbersrek(5)
print(f"Wywoluje sie w {count} próbach ")
numbersn(5)
print(f"Wywoluje sie w {count} próbach ")
# zad2

def reversen(txt: str)->str:
    global count
    count = 0
    ile = len(txt)
    nowy=""
    for i in range(ile) :
        count+=1
        nowy+=txt[ile-i-1]
    return nowy




def reverserek(txt: str):
    global dlugosc
    global count
    count+=1
    dlugosc=len(txt)
    if dlugosc==1:
        return txt
    return reverserek(txt[1:])+txt[0]

#zad3

def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    pocz = 0
    global count
    koniec = len(numbers) - 1
    while pocz <= koniec:
        count+=1
        srodek = (pocz + koniec) // 2
        if numbers[srodek] == value:
            return True, srodek
        elif numbers[srodek] < value:
            pocz = srodek + 1
        else:
            koniec = srodek - 1
    return False, -1




def binary_searchrek(n: int, m: int, p: int, numbers: Array)->Tuple[bool,int]:
    global count
    srodek=(n+m)//2
    count+=1
    if n>m:
        return False, -1
    if numbers[srodek] == p:
        return True,srodek
    elif numbers[srodek]<p:
        return binary_searchrek(srodek+1,m,p,numbers)
    else:
        return binary_searchrek(n,srodek-1,p,numbers)


#zad4
def n_sum_n(n: int, m: int)->list[int]:
    lista=[]
    for i in range(10):
        if i==m and n==1:
            lista.append(i)
        elif n>0:
            for j in n_sum_n(n-1,m-i):
                lista.append(j*10+i)
    return lista


print(n_sum_n(2,5))

#zad5

#zad6

def powern(n, m):
    wynik=1
    global count
    for i in range(m):
        count+=1
        wynik*=n
    return wynik

def powerrek(number : int, n:int)->int:
    global count
    count+=1
    if(n==0):
        return 1
    if(n==1):
        return number
    else:
        return number*powerrek(number,n-1)


def fastpowerrek(number: int, n:int)->int:
    global count
    count+=1
    if n==0:
        return 1
    if n%2!=0:
        return number*fastpowerrek(number,n-1)
    else:
        return number*fastpowerrek(number,n//2)


#zad7

count=0
print(reversen("Dawid"))
print(f"Wywoluje sie w {count} próbach ")
count=0
print(reverserek("Dawid"))
print(f"Wywoluje sie w {count} próbach ")
count=0
ints = array('I', [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71])
result = binary_search(ints, 8)
print(result)
print(f"Wywoluje sie w {count} próbach ")
count=0
resultrek=binary_searchrek(0,16,13,ints)
print(resultrek)
print(f"Wywoluje sie w {count} próbach ")
count=0
print(powern(2,3))
print(f"Wywoluje sie w {count} próbach ")
count=0
print(powerrek(2,3))
print(f"Wywoluje sie w {count} próbach ")
count=0
print(fastpowerrek(2,3))
print(f"Wywoluje sie w {count} próbach ")

