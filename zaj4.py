'''
#parzysta czy nieparzysta
input()
dane=[int(x) for x in input().split()]

for o in dane:
    if o%2 == 0:
        print('P', end='')
    else:
        print('N', end='')

#odwroc tablice
input()
dane=[int(x) for x in input().split()]

dane.reverse()
print(*dane)

#sum of cubes
a,b=[int(x) for x in input().split()]

suma=0
for x in range (a, b+1):
    suma=suma+x**3
print(x)

#sredniabezzera
liczba=int(input())
i=0
suma=0

while liczba!=0:
    i=i+1
    suma=suma+liczba
    liczba=int(input())
srednia=float(suma)/i
print(srednia)

#zlicz najwieksza
#cos tu nie dziala
n=int(input())
dane=int(input())
max=dane
licznik=0

for i in range(n):
    if dane>max:
        max=dane
        licznik=1
    elif dane==max:
        licznik=licznik+1
print(licznik)


#wieksza liczba
a, b = input().split()
a, b = int(a), int(b)
if a>b:
    print(a)
else:
    print(b)


#porownanie liczb
a, b = input().split()
a, b = int(a), int(b)
if a>b:
    print("A>B")
elif a<b:
    print("A<B")
else:
    print("A==B")


#znak liczby

a=int(input())
if a>0:
    print("+")
elif a<0:
    print("-")
else:
    print(0)


#suma wielu liczb

input()
liczby=[int(x) for x in input().split()]
suma=0

for o in liczby:
    suma=suma+o
print(suma)
'''

#suma liczb z przediału

a, b = input().split()
a, b = int(a), int(b)

suma=0
for o in range(a,b+1):
    suma=suma+a
    a=a+1
print(suma)
