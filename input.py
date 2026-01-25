import pygame

# Key pad mapping is as so: 

# 1 2 3 C      1 2 3 4      0 1 2 3 
# 4 5 6 D  =>  q w e r  =>  4 5 6 7
# 7 8 9 E  =>  a s d f  =>  8 9 10 11
# A 0 B F      z x c v      12 13 14 15

class controls:
    def __init__(self):
        self.keys = [False for _ in range(16)]

    def input_handler(self, cpu):

        pygame.init()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cpu.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("W pressed")