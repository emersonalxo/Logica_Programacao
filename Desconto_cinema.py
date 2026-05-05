idade = int(input("Qual sua idade?"))
tem_carteirinha = input("Tem carteirinha (s/n)")

if idade <12 or tem_carteirinha == "s":
    print("Você tem direito a meia entrada")
else:
    print("Você não tem direiro a meia entrada")