import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pygame.init()

# Size of screen
_size = [500, 500]
_screen = pygame.display.set_mode(_size)

# We will use y = mx + c for each x & y in _lines to set boundaries on what we change
_lines = [[3, 100], [-0.3, 400], [0.4, 200], [-2, 300], [1, -100]]

# Colours the plane one pixel at a time.
# Only pixels below each line will be coloured
# Any pixel that is black will be changed white. The opposite is also true
def colourplane(lines, screen):
    screen.fill(white)
    for line in lines:
        for i in range(500):
            for j in range(500):
                if j < (line[0] * i + line[1]):
                    if screen.get_at((i, j)) == white:
                        screen.set_at((i, j), black)
                    else:
                        screen.set_at((i, j), white)


# Prevents the window from closing
_running = True

# Main application loop
while _running:
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == pygame.QUIT:
            _running = False
        if event.type == pygame.KEYDOWN:
            colourplane(_lines, _screen)

    pygame.display.update()

pygame.quit()
