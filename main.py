import pygame

pygame.init()


def setup_screen(size, color):
    print("Display Setup:   size {}, color {}".format(size, color))
    flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
    new_screen = pygame.display.set_mode(size, flags)
    background = pygame.Surface(size)
    background.fill(color)
    background = background.convert(background)
    new_screen.blit(background, (0, 0))
    return new_screen


info = pygame.display.Info()
window_size = (info.current_w, info.current_h)
white = (255, 255, 255)
screen = setup_screen(window_size, white)
clock = pygame.time.Clock()

mainLoop = True

while mainLoop:
    runtime = 0
    FPS = 60
    milliseconds = clock.tick(FPS)  # do not go faster than this framerate
    runtime += milliseconds / 1000.0

    text = "Symmetry    FPS: {0:.2f}   Runtime: {1:.2f}".format(clock.get_fps(), runtime)
    pygame.display.set_caption(text)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            break

        print(event)
        if event.type == pygame.QUIT:
            mainLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainLoop = False
        elif event.type == pygame.VIDEORESIZE:
            screen = setup_screen(event.size, white)
            print(screen.get_size())

pygame.quit()
