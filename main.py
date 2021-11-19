from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

# inicialização
janela = Window(800, 800)
janela.set_title("Pong")

fundo = GameImage("nebulosa-gaivota.jpg")
bola = Sprite("bola.png", 1)

padE = Sprite("padE.png", 1)
padD = Sprite("padD.png", 1)

placarE = 0
placarD = 0


# posicionando ao centro
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 2 - bola.height / 2

# posicionando os paddings
padE.x = 5
padE.y = janela.height / 2 - padE.height / 2

padD.x = janela.width - padD.width - 5
padD.y = janela.height / 2 - padD.height / 2

velBolaX = 400
velBolaY = 380

velPad = 280

# Construtor do objeto teclado
teclado = Window.get_keyboard()

# Atualizando a janela com o loop
while True:
    # entrada de dados
    if teclado.key_pressed("UP") and padD.y >= 0:
        padD.y = padD.y - velPad * janela.delta_time()
    if teclado.key_pressed("DOWN") and (padD.y + padD.height <= janela.height):
        padD.y = padD.y + velPad * janela.delta_time()

    if teclado.key_pressed("w") and padE.y >= 0:
        padE.y = padE.y - velPad * janela.delta_time()
    if teclado.key_pressed("s") and (padE.y + padE.height <= janela.height):
        padE.y = padE.y + velPad * janela.delta_time()

    # update
    bola.x = bola.x + velBolaX * janela.delta_time()  # velocidade fixa baseada no frame rate

    # se a bolinha colidir com o pad
    if padD.collided(bola):
        velBolaX *= -1
        bola.x = janela.width - padD.width - (2 * bola.width)
    if padE.collided(bola):
        velBolaX *= - 1
        bola.x = padE.width + bola.width

    # reposicionar ao centro quando um dos dois pontuam
    if (bola.x + bola.width) >= janela.width:
        bola.x = janela.width / 2 - bola.width / 2
        bola.y = janela.height / 2 - bola.height / 2
        placarE += 1
    if bola.x <= 0:
        bola.x = janela.width / 2 - bola.width / 2
        bola.y = janela.height / 2 - bola.height / 2
        placarD += 1

    bola.y += velBolaY * janela.delta_time()
    if (bola.y + bola.height) >= janela.height:
        bola.y = janela.height - bola.height
        velBolaY *= -1
    if bola.y <= 0:
        bola.y = 0
        velBolaY *= -1

    # desenho
    fundo.draw()
    janela.draw_text(str(placarE), x=janela.width/4, y=10, size=100, color=(255, 255, 255), font_name="monospace",bold = True, italic=False)
    janela.draw_text(str(placarD), x=2.68 * (janela.width/4), y=10, size=100, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
    bola.draw()
    padD.draw()
    padE.draw()
    janela.update()

# Comentários da Aula
# delta_time é um cronometro, é o tempo que demora um frame para ser produzido
# Método collide
