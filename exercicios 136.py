nome = str(input('\nEntre com o Nome: '))
idade = int(input('\nEntre com a Idade: '))
if idade <= 10:
    print(f"\n{nome} pagará R$ 30")
elif idade <= 29:
    print(f"\n{nome} pagará R$ 60")
elif idade <= 45:
    print(f"\n{nome} pagará R$ 120")
elif idade <= 59:
    print(f"\n{nome} pagará R$ 150")
elif idade <= 65:
    print(f"\n{nome} pagará R$ 250")
else:
    print(f"\n{nome} pagará R$ 400")