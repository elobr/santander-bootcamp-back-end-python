import time
nome = input("Digite seu nome:\n ")
time.sleep(1)

print(f"\nOlá, {nome}!")
time.sleep(2)

idade = int(input("\nQuantos anos você tem?\n"))
time.sleep(1)
print(f"\n{idade}? Que legal!")
time.sleep(1)

resposta = input(f"\nGostaria de saber quantos anos terá daquia 5 anos? sim/não\n").strip().lower()
time.sleep(1)

if resposta == "sim":
    print(f"\nCerto! Então vamos lá!\n")
    time.sleep(2)
    print(f"\nDaqui a 5 anos você terá {idade + 5} anos de idade.\n")

else:
    print(f"\nTudo bem! Se mudar de ideia estarei aqui.\n")
time.sleep(1)