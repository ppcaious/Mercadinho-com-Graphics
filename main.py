from graphics import *
from db_manager import *

gui = GraphWin("Simulador de Ecommerce", 1366, 720)

def background():
    bg = Image(Point(683, 360), "background.gif")
    bg.draw(gui)

def mostrar_estoque(gui, x, y, espaco):
    estoque = mostrar()
    for i, item in enumerate(estoque):
        espacamento = y + i * espaco
        itens = Text(Point(x, espacamento), item)
        itens.setTextColor("white")
        itens.setSize(14)
        itens.draw(gui)

background()
mostrar_estoque(gui, 180, 100, 30)

while True:
    key = gui.checkKey()
    if key == "Escape":
        break
