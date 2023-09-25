import math as m

X=float(input("\ndigite valor de x: "))

num={(5 * X+ 3 ) /  m.sqrt (X**2 -16)}

if X>4 or X<(-4):
    print(f"\nf(x)= {(num)}")
else:
    print('\nNAO PODE SER FEITA')
print('\n')