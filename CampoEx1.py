ultimo = 10
fila = list(range(1, ultimo +1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"fila atual: {fila}")
    print(f"Digite F para adicionar clientes no fim da fila")
    print(f"ou A para realizar o atendimento. S para sair.")
    operação = str(input("Operação (F, A ou S):")).strip().upper()[0]
    while operação not in "FAS":
        print("\033[31mERRO!\033[m\033[34mDigite operção correta\033[m")
        operação = str(input("Operação (F, A ou S):")).strip().upper()[0]
    if len(fila) > 0:
        if operação in "A":
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
    else:
        print("Fila vazia! Ninguém para atender.")

    if operação in "F":
        ultimo += 1
        fila.append(ultimo)
        print("Foi adicionada novo cliente na fila")
    if operação in "S":
        print("OBRIGA PELA PREFERÊNCIA, VOLTE SEMPRE!")
        break