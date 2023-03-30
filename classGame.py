import pygame, classBaloon
pygame.init()


class Game():
    def __init__(self):
        self.font = pygame.font.SysFont('DOCKER THREE', 40)

        self.FPS = 30
        self.clock = pygame.time.Clock()

        self.over = False
        self.display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.background = pygame.image.load('backgroundsky.jpg')

        self.clap_sound = pygame.mixer.Sound("clap.wav")

        self.group = pygame.sprite.LayeredUpdates()
        self.speed = 7

        self.score = 0

    def update(self):

        self.clock.tick(self.FPS)
        self.display.blit(self.background, (0, 0))
        self.group.draw(self.display)
        self.group.update()
        self.show_score()
        for e in self.group:
            if e.rect.y < -2520:
                e.kill()

        pygame.display.update()

    def spawnbaloon(self):
        self.baloon = classBaloon.Baloon(self.speed)
        self.group.add(self.baloon)

    def checkclick(self, pos):
        sprtlist = self.group.get_sprites_at(pos)
        
        if sprtlist:
            self.play_clap_sound()

        for k in sprtlist:
            k.kill()
            self.score = self.score + 1
        
    def play_clap_sound(self):
        pygame.mixer.Sound.play(self.clap_sound)

    def show_score(self):
        score = self.font.render("Score : " + str(self.score), True, (255, 255, 255))
        self.display.blit(score, (10, 10))

    def speedup(self):
        self.speed += 2

