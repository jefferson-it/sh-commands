from os import system
import sys

args = sys.argv[1:]

action = None

if not args:
    print("""
    |-----------------------------------------------|
    | Execute as ações usando os seguintes comando: |
    |-----------------------------------------------|
    | 0 - Limpar tela
    | 1 - Desligar 
    | 1f - Desligar (forçar) 
    | 2 - Reiniciar
    | 2f - Reiniciar (forçar)
    | 3 - Atualizar
    | 4 - Fechar
    |-----------------------------------------------|
    """)

    action = input("Qual ação desejas completar?\n")
else:
    action = args[0]

if action == "0":
    system("c")
elif action == "1" and args[1] == "-y":
    system("poweroff")
elif action == "1f":
    system("sudo poweroff -f")
elif action == "2":
    system("reboot")
elif action == "2f":
    system("sudo reboot")
elif action == "3":
    system("apt update && apt upgrade -y")
elif action == "4":
    print("BYE! ^-^")