SaldoM= int (input('\ndigite saldo medio:  '))

if SaldoM<501:
    print(f"\nComo seu saldo era de: {SaldoM},saldomedio,bvoce nao tera nenhum credito")
elif SaldoM<1001:
    print(f"\nComo seu saldo era de: {SaldoM},saldomedio,seu credito sera de: {SaldoM*0.3},credito")
elif SaldoM<3001:
    print(f"\nComo seu saldo era de: {SaldoM},saldomedio,seu credito sera de: {SaldoM*0.4},credito")
else:
    print(f"\nComo seu saldo era de: {SaldoM},saldomedio,seu credito sera de: {SaldoM*0.5},credito")
print('\n')