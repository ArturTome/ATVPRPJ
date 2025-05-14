#Itens da loja (lembrete pra não fazer merda)
loja = [
    {"nome": "Katana no insta-counter", "tipo": "Arma", "preco": 50},
    {"nome": "Espada de Diamante", "tipo": "Arma", "preco": 200},
    {"nome": "Armadura de Netherite", "tipo": "Armadura", "preco": 60},
    {"nome": "Poção de Luxúria das algas", "tipo": "Consumível", "preco": 30},
    {"nome": "Anel de Luana", "tipo": "Acessório", "preco": 100},
    {"nome": "Mão de música", "tipo": "Grímorio", "preco": 500},
]

#Login do Player
nome = input("Digite o nome do jogador: ")
ouro = input("Digite a quantidade de ouro inicial: ")
ouro = float(ouro)
inventario = []

#Mostrar loja
def mostrar_loja():
    print("\n--- Loja ---")
    if not loja:
        print("A loja está vazia.")
    else:
        for i, item in enumerate(loja, start=1):
            print(f"{i}. {item['nome']} ({item['tipo']}) - {item['preco']} ouro")

#Comprar item da loja
def comprar_item():
    global ouro
    if not loja:
        print("Não há itens disponíveis para compra.")
        return

    mostrar_loja()
    try:
        escolha = input("Digite o número do item para comprar (0 para cancelar): ")
        escolha = int(escolha)
        if escolha == 0:
            return
        item = loja[escolha - 1]
        if ouro >= item["preco"]:
            ouro -= item["preco"]
            item_comprado = loja.pop(escolha - 1)  # tira o item da loja
            inventario.append(item_comprado)
            print(f"{nome} comprou {item_comprado['nome']} por {item_comprado['preco']} ouro!")
        else:
            print("Ouro insuficiente!")
    except (IndexError, ValueError):
        print("Escolha inválida.")

#Mostrar inventário do player
def mostrar_inventario():
    print(f"\n--- Inventário de {nome} ---")
    if not inventario:
        print("Inventário vazio.")
    else:
        for item in inventario:
            print(f"- {item['nome']} ({item['tipo']})")
        print(f"Ouro restante: {ouro}")

#Menu dessa bagaça
def menu():
    while True:
        print('''
        1. Comprar Item
        2. Ver Inventário
        0. Sair
        ''')

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            comprar_item()
        elif opcao == "2":
            mostrar_inventario()
        elif opcao == "0":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida.")

#Tudo começa com isso, não tira pensando que é inútil (aconteceu 2x)
menu()
