def mostrar():
    with open('estoque.csv', 'r') as estoque:
        linhas = estoque.readlines()
    for linha in linhas:
        produto, quantidade = linha.split(',')
        print(f'Produto: {produto}, Quantidade: {quantidade}')
        
def remove(produto):
    with open('estoque.csv', 'r') as estoque:
        linhas = estoque.readlines()
    if produto == '':
        linhas_filtradas = [linha for linha in linhas]
    else:
        linhas_filtradas = [linha for linha in linhas if produto != linha.split(',')[0]]
            

    with open('estoque.csv','w') as estoque:
        estoque.writelines(linhas_filtradas)

def compras(produto, comprado):
    with open('estoque.csv', 'r') as estoque:
        linhas = estoque.readlines()
    cabeçalho = linhas[0]
    linhas_atualizadas = [cabeçalho]  
    produto_encontrado = False

    for linha in linhas[1:]:  
        nome, quantidade_str = linha.strip().split(',')
        quantidade = int(quantidade_str)

        if nome == produto:
            produto_encontrado = True
            if comprado < 0:
                nova_quantidade = quantidade + comprado
            else:
                nova_quantidade = quantidade - comprado
            if nova_quantidade > 0:
                linhas_atualizadas.append(f"{nome},{nova_quantidade}\n")
            elif nova_quantidade == 0:
                print(f"Produto '{produto}' removido do estoque.")
            elif nova_quantidade < 0:
                print(f'produto com falta de estoque! Temos apenas {quantidade} no estoque.')
                linhas_atualizadas.append(f"{nome},{quantidade}\n")
        else:
            linhas_atualizadas.append(linha)

    if not produto_encontrado:
        print(f"Produto '{produto}' não encontrado no estoque.")
            

    with open('trabalho_AED/estoque.csv', 'w') as estoque:
        estoque.writelines(linhas_atualizadas)

def adicionar(produto, quantidade, menu):
    with open('estoque.csv', 'r') as estoque:
        linhas = estoque.readlines()
        if menu == 'add produto':
            repetido = False
            for linha in linhas:
                estoque = linha.split(',')[0]
                if produto == estoque:
                    print('Esse produto já está no estoque caso queira adionar mais\nquantidades, por favor selecionar add quantidade no menu!')
                    repetido = True
                    break
            if not repetido: 
                if len(linhas) == 1:
                    linhas.append(f'{produto},{quantidade}')
                else:
                    linhas.append(f'\n{produto},{quantidade}')
                with open('estoque.csv', 'w') as estoque:
                    estoque.writelines(linhas)
        elif menu == 'add quantidade':
            linhas_atualizadas = []
            for linha in linhas:
                estoque, nova_quantidade = linha.strip().split(',')
                if produto == estoque:
                    numero = int(nova_quantidade)
                    numero += quantidade
                    nova_linha = (f'{estoque},{str(numero)}')
                    linhas_atualizadas.append(nova_linha)
                else:
                    linhas_atualizadas.append(linha)
                with open('estoque.csv', 'w') as estoque:
                    estoque.writelines(linhas_atualizadas)
               
                      
print('''Olá! Opções:
[ver estoque] para ver os produtos e as quantidades que já estão no
estoque,
[add produto] para adicionar produto,
[add quantidade] para adicionar quantidade em um produto já existente,
[remover] para remover produto do estoque,
[comprar] para tirar automaticamente do estoque devido a uma compra,
[sair] Para sair do programa.''')   
while True:
    gerenciamento = input()

    if gerenciamento == 'sair':
        print('Fechando o programa...')
        break
    elif gerenciamento == 'remover':
        produto_remover = input('digite o produto que quer remover: ')
        remove(produto_remover)
    elif gerenciamento == 'comprar':
        produto_comprado = input('digite o produto que quer comprar: ')
        quantos = int(input('Digite a quantidade: '))
        compras(produto_comprado, quantos)
    elif gerenciamento == 'add quantidade' or gerenciamento == 'add produto':
        produto_adicionado = input('Digite o produto que quer adicionar: ') 
        adicionar_quantidade = int(input('Digite a quantidade para adiocionar no estoque: '))
        adicionar(produto_adicionado,adicionar_quantidade, gerenciamento)
    elif gerenciamento == 'ver estoque':
        mostrar()














        

