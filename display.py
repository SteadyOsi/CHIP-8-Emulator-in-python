import pygame

class Graphics:
    def __init__(self):
        self.scale = 0
        self.WIDTH = 64
        self.HEIGHT = 32
        self.screen = 0
        self.cpuFrameBuffer = [[False for _ in range(64)]for _ in range(32)]

    

    def init_display(self, scale):

        self.scale = scale

        pygame.init()

        screen = pygame.display.set_mode((self.WIDTH * self.scale, self.HEIGHT * self.scale))
        pygame.display.set_caption("CHIP-8-PY")

        return screen
        

    def render(self, cpu, screen):

        self.cpuFrameBuffer = cpu.display 

        # Rendering
        y = 0
        while y < self.HEIGHT: 
            x = 0
            while x < self.WIDTH:
                if cpu.display[y][x] == 1:
                    pygame.draw.rect(screen, "green", pygame.Rect(x*self.scale, y*self.scale, self.scale, self.scale))
                x += 1
            y += 1

        pygame.display.flip()

        cpu.draw_Dirty = False