import math as m

ang=float(input('\nDigite o angulo em graus: '))
Rang=ang* m.pi /180
if (Rang > m.pi/2 and Rang <= m.pi) or (Rang > 3*m.pi/2 and Rang <= 2*m.pi):
    print(f'\nseno: {m.sin(Rang)}')
else:
    print(f'\nco-seno: {m.cos(Rang)}')
print('\n')