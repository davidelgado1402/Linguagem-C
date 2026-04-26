def imprimir_tabuleiro(tabela):
    print()
    for i in range(3):
        linha = [str(celula) if celula!=-1 else " " for celula in tabela[i]]
        print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
        if i<2:
            print("---|---|---")
    print()

def main():
    tabela = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]

    jogador = 0
    jogadas = 0
    vencedor = -1

    while jogadas<9 and vencedor==-1:
        imprimir_tabuleiro(tabela)

        print(f"Agora é a vez do jogador {jogador}.")
        
        try:
            posicao = int(input("Insira uma posição de 1 a 9: "))
            
            if posicao<1 or posicao>9:
                print("Essa posição não existe! Tente de 1 a 9.")
                continue

            lin = (posicao - 1) // 3
            col = (posicao - 1) % 3

            if tabela[lin][col] != -1:
                print("Lamento, essa posição já está ocupada!")
                continue
                
            tabela[lin][col] = jogador
            jogadas += 1

            for i in range(3):
                if tabela[i][0]==tabela[i][1]==tabela[i][2]==jogador:
                    vencedor = jogador
                if tabela[0][i]==tabela[1][i]==tabela[2][i]==jogador:
                    vencedor = jogador
            if tabela[0][0]==tabela[1][1]==tabela[2][2]==jogador:
                vencedor = jogador
            if tabela[0][2]==tabela[1][1]==tabela[2][0]==jogador:
                vencedor = jogador

            jogador = 1 if jogador == 0 else 0

        except ValueError:
            print("Por favor, digite apenas números inteiros!")

    imprimir_tabuleiro(tabela)

    if vencedor!=-1:
        print(f"O jogador {vencedor} venceu! Parabéns!")
    else:
        print("Empate, vocês deixaram a velha vencer!")

if __name__ == "__main__":
    main()