from graphics import *
from db_manager import *

gui = GraphWin("Simulador de Ecommerce", 1366, 720)

def background():
    bg = Image(Point(683, 360), "AED1_Trabalho/background.gif")
    bg.draw(gui)
    
itens_desenhados = []
def mostrar_estoque(gui, x, y, espaco):
    global itens_desenhados
    for item in itens_desenhados:
        item.undraw()

    estoque = mostrar()
    for i, item in enumerate(estoque):
        espacamento = y + i * espaco
        texto_item = Text(Point(x, espacamento), item)
        texto_item.setTextColor("white")
        texto_item.setSize(14)
        texto_item.draw(gui)
        itens_desenhados.append(texto_item)

background()
mostrar_estoque(gui, 180, 100, 30)

botoes = {
    "adicionar_produto": ((706, 274), (1008, 405)),
    "adicionar_quantidade": ((1034, 274), (1333, 405)),
    "remover": ((706, 432), (1008, 562)),
    "comprar": ((1034, 432), (1333, 562)),
    "ver estoque": ((870, 573),(1171 ,703)),
    "sair": ((1250, 20), (1340, 65))
}

while True:
    mouse = gui.getMouse()
    x = mouse.getX()
    y = mouse.getY()
    print(f"Coordenadas clicadas: {x}, {y}")

    for nome, ((x1, y1), (x2, y2)) in botoes.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            print(f"Botão '{nome}' clicado!")
            if nome == 'sair':
                gui.close()
            if nome == 'ver estoque':
                mostrar_estoque(gui, 180, 100, 30)
            if nome == 'remover':
                removergui = GraphWin("Remover produto", 400, 200)
                removergui.setBackground("purple")
                texto = Text(Point(200, 50), "Digite o nome do produto que deseja remover:")
                texto.setSize(12)
                texto.draw(removergui)
                entrada = Entry(Point(200, 100), 20)
                entrada.draw(removergui)
                sairtexto = Text(Point(200, 150), "Clique aqui para remover o produto e sair.")
                sairtexto.draw(removergui)
                rect = Rectangle(Point(48, 140), Point(355, 157))
                rect.draw(removergui)
                cancelar = Text(Point(200, 180), "Clique aqui para cancelar.")
                cancelar.draw(removergui)
                cancelarrect = Rectangle(Point(48, 170), Point(355, 187))
                cancelarrect.draw(removergui)

                while True:
                    mouse = removergui.getMouse()
                    if 48 <= mouse.getX() <= 355 and 140 <= mouse.getY() <= 157:
                        produto = entrada.getText()
                        remove(produto)
                        removergui.close()
                        break
                    if 48 <= mouse.getX() <= 355 and 170 <= mouse.getY() <= 187:
                        removergui.close()
                        break
            if nome == 'comprar':
                comprargui = GraphWin("Comprar produto", 400, 200)
                comprargui.setBackground("purple")
                texto = Text(Point(200, 50), "Digite o nome e quantidade (separados por vírgula) do produto que deseja comprar:")
                texto.setSize(8)
                texto.draw(comprargui)
                entrada = Entry(Point(200, 100), 20)
                entrada.draw(comprargui)
                sairtexto = Text(Point(200, 150), "Clique aqui para comprar o produto e sair.")
                sairtexto.draw(comprargui)
                rect = Rectangle(Point(48, 140), Point(355, 157))
                rect.draw(comprargui)
                cancelar = Text(Point(200, 180), "Clique aqui para cancelar.")
                cancelar.draw(comprargui)
                cancelarrect = Rectangle(Point(48, 170), Point(355, 187))
                cancelarrect.draw(comprargui)

                while True:
                    mouse = comprargui.getMouse()
                    if 48 <= mouse.getX() <= 355 and 140 <= mouse.getY() <= 157:
                        produto = entrada.getText()
                        produtolista = produto.split(',')
                        print(produtolista)
                        compras(produtolista[0].lower(), int(produtolista[1]))
                        comprargui.close()
                        break
                    if 48 <= mouse.getX() <= 355 and 170 <= mouse.getY() <= 187:
                        comprargui.close()
                        break
            if nome == 'adicionar_quantidade':
                addqtdgui = GraphWin("Adicionar produto existente", 400, 200)
                addqtdgui.setBackground("purple")
                texto = Text(Point(200, 50), "Digite o nome e quantidade (separados por vírgula) do produto que deseja adicionar:")
                texto.setSize(8)
                texto.draw(addqtdgui)
                entrada = Entry(Point(200, 100), 20)
                entrada.draw(addqtdgui)
                sairtexto = Text(Point(200, 150), "Clique aqui para adicionar o produto e sair.")
                sairtexto.draw(addqtdgui)
                rect = Rectangle(Point(48, 140), Point(355, 157))
                rect.draw(addqtdgui)
                cancelar = Text(Point(200, 180), "Clique aqui para cancelar.")
                cancelar.draw(addqtdgui)
                cancelarrect = Rectangle(Point(48, 170), Point(355, 187))
                cancelarrect.draw(addqtdgui)

                while True:
                    mouse = addqtdgui.getMouse()
                    if 48 <= mouse.getX() <= 355 and 140 <= mouse.getY() <= 157:
                        produto = entrada.getText()
                        produtolista = produto.split(',')
                        print(produtolista)
                        adicionar(produtolista[0], int(produtolista[1]), "add quantidade")
                        addqtdgui.close()
                        break
                    if 48 <= mouse.getX() <= 355 and 170 <= mouse.getY() <= 187:
                        addqtdgui.close()
                        break
            if nome== 'adicionar_produto':
                addgui = GraphWin("Adicionar novo produto", 400, 200)
                addgui.setBackground("purple")
                texto = Text(Point(200, 50), "Digite o nome e quantidade (separados por vírgula) do produto que deseja adicionar:")
                texto.setSize(8)
                texto.draw(addgui)
                entrada = Entry(Point(200, 100), 20)
                entrada.draw(addgui)
                sairtexto = Text(Point(200, 150), "Clique aqui para adicionar o produto e sair.")
                sairtexto.draw(addgui)
                rect = Rectangle(Point(48, 140), Point(355, 157))
                rect.draw(addgui)
                cancelar = Text(Point(200, 180), "Clique aqui para cancelar.")
                cancelar.draw(addgui)
                cancelarrect = Rectangle(Point(48, 170), Point(355, 187))
                cancelarrect.draw(addgui)
                
                while True:
                    mouse = addgui.getMouse()
                    if 48 <= mouse.getX() <= 355 and 140 <= mouse.getY() <= 157:
                        produto = entrada.getText()
                        produtolista = produto.split(',')
                        print(produtolista)
                        adicionar(produtolista[0].lower(), int(produtolista[1]), "add produto")
                        addgui.close()
                        break
                    if 48 <= mouse.getX() <= 355 and 170 <= mouse.getY() <= 187:
                        addgui.close()
                        break