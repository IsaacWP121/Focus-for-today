import pygame
width, height = 550, 400
WHITE = (255, 255, 255)
class Button:
    def __init__(self, screen, wdiv, hdiv, color):
        self.wdiv = wdiv
        self.hdiv = hdiv
        self.color = color
        self.font_size = 20
        self.width = width
        self.height = height
        self.screen = screen
        self.Words = "Focus for today"
        self.update_size()
    
    def update_size(self):
        self.bw, self.bh = round(self.screen.get_width()/self.wdiv), round(self.screen.get_width()/self.hdiv)
        self.x = self.screen.get_width()/2-self.bw/2
        self.y = self.screen.get_height()/2-self.bh/2
        pygame.draw.rect(self.screen, self.color, (self.x, self.y,self.bw, self.bh))
        self.addText()
    
    def addText(self):
        def render(self):
            self.font = pygame.font.SysFont('Arial', round(self.font_size))
            self.text = self.font.render(self.Words, True, WHITE)
        render(self)
        while self.text.get_rect()[2] < self.bw-self.bw/7 and self.text.get_rect()[3] < self.bh-self.bw/8:
            self.font_size += 1
            render(self)
        while self.text.get_rect()[2] > round(self.bw-self.bw/7) and self.text.get_rect()[3] > round(self.bh-self.bw/8):
            self.font_size -= 2
            render(self)
        text_rect = self.text.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.screen.blit(self.text, text_rect)