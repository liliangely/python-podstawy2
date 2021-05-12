'''
we = input()
a,b = we.split()

a = int(a)
b = int(b)
c = a + b
print(c)


a,b = input().split()
a = int(a)
b = int(b)
c=a+b

print('Suma liczb %s i %i wynosi %.4f'%(a,b,c))



a = float(input())
b = float(input())
h = float(input())
p = 1/2 * (a+b) * h
print("Pole trapezu jest rowne ","%.2f" %p)
'''
'''
a,b,c = map(int, input().split())
p = -(b/2*a)
q = -((b**2 - 4*a*c)/4*a)
print("W = (","%.1f" %p,",","%.1f" %q,")")
'''
'''
a = int(input()); b = int(input()); c = int(input()); d = int(input()); e = int(input()); f = int(input())
s = a**3 + b**3 + c**3 + d**3 + e**3 + f**3 - 2
print(s)

'''

a,b = input().split()
x,y = input().split()
a = int(a)
b, x, y = int(b), int(x), int(y)

a, b = b, a
'''do a wkładamy b, do b wkładamy a'''



'''odległość punktów'''
d = ((a-x)**2 + (b-y)**2)**.5
print(round(d, 1))
