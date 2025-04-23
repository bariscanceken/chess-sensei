#Chess Main
import pygame as p
import chess_engine

width = height = 512
dimension = 8
square_size = height // dimension
max_fps = 15
images = {}

def load_images():
    images['wp'] = p.transform.scale(p.image.load("materials/wp.png") , (square_size , square_size))
    images['wR'] = p.transform.scale(p.image.load("materials/wR.png") , (square_size , square_size))
    images['wN'] = p.transform.scale(p.image.load("materials/wN.png") , (square_size , square_size))
    images['wB'] = p.transform.scale(p.image.load("materials/wB.png") , (square_size , square_size))
    images['wQ'] = p.transform.scale(p.image.load("materials/wQ.png") , (square_size , square_size))
    images['wK'] = p.transform.scale(p.image.load("materials/wK.png") , (square_size , square_size))
    images['bp'] = p.transform.scale(p.image.load("materials/bp.png") , (square_size , square_size))
    images['bR'] = p.transform.scale(p.image.load("materials/bR.png") , (square_size , square_size))
    images['bN'] = p.transform.scale(p.image.load("materials/bN.png") , (square_size , square_size))
    images['bB'] = p.transform.scale(p.image.load("materials/bB.png") , (square_size , square_size))
    images['bQ'] = p.transform.scale(p.image.load("materials/bQ.png") , (square_size , square_size))
    images['bK'] = p.transform.scale(p.image.load("materials/bK.png") , (square_size , square_size))

def main():
    p.init()
    screen = p.display.set_mode((width,height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess_engine.game_state()
    load_images()
    running = True
    while running : 
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen,gs)
        clock.tick(max_fps)
        p.display.flip()

def draw_game_state(screen,gs):
    draw_board(screen)
    draw_materials(screen,gs.board)

def draw_board(screen):
    colors = [p.Color('#EEEED2') , p.Color('#769656')] 
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*square_size , r*square_size , square_size  , square_size))

def draw_materials(screen,board):
    for r in range(dimension):
        for c in range(dimension):
            material = board[r][c]
            if material != "--":
                screen.blit(images[material], p.Rect(c*square_size , r*square_size , square_size , square_size))








if __name__ == "__main__":
    main()
