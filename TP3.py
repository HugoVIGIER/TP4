import math as m

#Fonction:

def Newton (f, fder, x0, epsilon, Nitermax):
    xold = x0
    xnew = xold - ((f(xold))/fder(xold))
    erreur = xnew - xold
    xold = xnew
    n = 1
    while abs(erreur) > epsilon and n < Nitermax :
        n = n + 1
        xnew = xold - ((f(xold))/fder(xold))
        erreur = xnew - xold
        xold = xnew
        print(xnew,n)
    return xnew,n, abs(xnew-xold)



#Question 1:

print("="*25,"Question 1","="*25)

def f1(x):
    return ((x**4)+3*x-9)

def fder1(x):
    return (4*(x**3)+ 3)

print(Newton(f1, fder1, 3/2, 1e-10, 5e4))

print("="*20)

print(Newton(f1, fder1, -(3/2), 1e-10, 5e4))



#Question 2:

print("="*25,"Question 2","="*25)


def f2(x):
    return 3*m.cos(x)-2-x

def fder2(x):
    return -3*m.sin(x)-1
    
print(Newton(f2, fder2, 0.4, 1e-10, 5e4))

print("="*20)

print(Newton(f2, fder2, -(1.4), 1e-10, 5e4))

print("="*20)

print(Newton(f2, fder2, -(3.5), 1e-10, 5e4))



#Question 3:

print("="*25,"Question 3","="*25)

def f3(x):
    return x*m.exp(x)-7

def fder3(x):
    return m.exp(x)+x*m.exp(x)

print(Newton(f3, fder3, 1.4, 1e-10, 5e4))



#Question 4:

print("="*25,"Question 4","="*25)

def f4(x):
    return m.exp(x)-x-10

def fder4(x):
    return m.exp(x)-1

print(Newton(f4, fder4, 2.5, 1e-10, 5e4))

print("="*20)

print(Newton(f4, fder4, -(9.5), 1e-10, 5e4))



#Question 5:

print("="*25,"Question 5","="*25)

def f5(x):
    return 2*m.tan(x)-x-5

def fder5(x):
    return (2/(m.cos(x)**2))-1

print(Newton(f5, fder5, 1.3, 1e-10, 5e4))



#Question 6:

print("="*25,"Question 6","="*25)

def f6(x):
    return m.exp(x)-x**2-3

def fder6(x):
    return m.exp(x)-2*x

print(Newton(f6, fder6, 1.7, 1e-10, 5e4))



#Question 7:

print("="*25,"Question 7","="*25)

def f7(x):
    return 3*x+4*m.log(x)-7

def fder7(x):
    return 3+(4/x)

print(Newton(f7, fder7, 1.7, 1e-10, 5e4))



#Question 8:

print("="*25,"Question 8","="*25)

def f8(x):
    return ((x**4)-2*x**2+4*x-17)

def fder8(x):
    return 4*x**3-4*x+4

print(Newton(f8, fder8, 1.8, 1e-10, 5e4))

print("="*20)

print(Newton(f8, fder8, -(2.6), 1e-10, 5e4))



#Question 9:

print("="*25,"Question 9","="*25)

def f9(x):
    return m.exp(x)-2*m.sin(x)-7

def fder9(x):
    return m.exp(x)-2*m.cos(x)

print(Newton(f9, fder9, 2.3, 1e-10, 5e4))



#Question 10:

print("="*25,"Question 10","="*25)

def f10(x):
    return m.log(x**2+4)*m.exp(x)-10

def fder10(x):
    return m.exp(x)*m.log(x**2+4)+m.exp(x)*(2*x)/(x**2+4)

print(Newton(f10, fder10, 1.8, 1e-10, 5e4))

