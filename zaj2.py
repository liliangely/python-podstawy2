'''
#bingo
a, b = input().split()
a, b = int (a), int (b)
x = int(input())

if x < a:
	print(a - x)
elif x > b:
	print(x - b)
else:
	print('BINGO')


#rokprzestepny
rok = int(input())
if (rok%4 == 0 and rok%100 > 0) or rok%400 == 0:
	print('Yes')
else:
	print('No')


#ciagiliczb
x, y = input().split()
x, y = int(x), int(y)
znak = input()

for muz in range(x, y+1):
    if znak == 'p' and muz%2==0:
        print(muz, end=' ')
    if znak == 'n' and muz%2==1:
        print(muz, end=' ')

'''

#szescianyliczb

#input()
#dane=([int(x)**3 for x in input().split()])
#print(dane)


#starszadata
rok1, m1, d1= input().split()
rok2, m2, d2= input().split()
rok1, m1, d1 = int(rok1), int(m1), int(d1)
rok2, m2, d2 = int(rok2), int(m2), int(d2)

if rok1<rok2:
    print(rok1, m1, d1)
elif rok1==rok2:
    if m1<m2:
        print(rok1, m1, d1)
    elif m1==m2:
        if d1<d2:
            print(rok1, m1, d1)
        elif d1==d2:
            print(rok1, m1, d1)
        else:
            print(rok2, m2, d2)
    else:
        print(rok2, m2, d2)
else:
    print(rok2, m2, d2)
