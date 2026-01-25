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
        self.keys = [False for _ in range(16)]


        pygame.init()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cpu.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: 
                    self.keys[0x1] = 1
                elif event.key == pygame.K_2:
                    self.keys[0x2] = 1
                elif event.key == pygame.K_3:
                    self.keys[0x3] = 1
                elif event.key == pygame.K_4:
                    self.keys[0xC] = 1
                elif event.key == pygame.K_q:
                    self.keys[0x5] = 1
                elif event.key == pygame.K_w:
                    self.keys[0x6] = 1
                elif event.key == pygame.K_e:
                    self.keys[0x7] = 1
                elif event.key == pygame.K_r:
                    self.keys[0x8] = 1
                elif event.key == pygame.K_a:
                    self.keys[0x9] = 1
                elif event.key == pygame.K_s:
                    self.keys[0xA] = 1
                elif event.key == pygame.K_d:
                    self.keys[0xB] = 1
                elif event.key == pygame.K_f:
                    self.keys[0xC] = 1
                elif event.key == pygame.K_z:
                    self.keys[0xD] = 1
                elif event.key == pygame.K_x:
                    self.keys[0xE] = 1
                elif event.key == pygame.K_c:
                    self.keys[0xF] = 1
                elif event.key == pygame.K_v:
                    self.keys[0x0] = 1

        cpu.keys = self.keys
                    