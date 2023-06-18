import random
import pygame
import sys
from data import *
import moviepy.editor
import os
import time


class Game:
    def __init__(self):
        super().__init__()
        # Initialize pygame and set up the game window
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Found Happiness")

        # Create instances of other classes
        self.cut_scene = CutScene()
        self.start_screen = StartScreen()
        self.settings = Settings()
        self.level_selection = LevelSelection()
        self.level1 = Level('graphics/pictures/рис1 (1).png')
        self.level2 = Level('graphics/pictures/рис2 (2).png')
        self.level3 = Level('graphics/pictures/рис3 (3).png')
        self.sound = Sound()
        self.timer = Timer()
        self.button = Button()
        self.current_scene = self.start_screen
        self.done1, self.done2, self.done3 = None, None, None
        # Set the current scene to the start screen

    def run(self):
        # Main game loop
        while True:
            # Handle events
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.current_scene == self.start_screen:
                    #self.cut_scene.draw()
                    self.current_scene.draw(self.screen)
                    
                    if self.button.pressed(self.current_scene.play_rect, event):
                        self.current_scene = self.level_selection
                        
                elif self.current_scene == self.level_selection:
                    self.current_scene.update()
                    self.current_scene.draw(self.screen)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.current_scene = self.start_screen
                    if self.button.pressed(self.level_selection.level1_rect, event):
                        self.current_scene = self.level1
                    if self.button.pressed(self.level_selection.level2_rect, event):
                        self.current_scene = self.level2
                    if self.button.pressed(self.level_selection.level3_rect, event):
                        self.current_scene = self.level3
                
                elif self.current_scene == self.level1:
                    self.current_scene.draw(self.screen, event)
                    if self.current_scene.end():
                        self.done1 = True
                        self.current_scene = self.level_selection
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.current_scene = self.level_selection
                        self.current_scene.draw(self.screen)
                    
                    
                elif self.current_scene == self.level2:
                    self.current_scene.draw(self.screen, event)
                    if self.current_scene.end():
                        self.done2 = True
                        self.current_scene = self.level_selection
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.current_scene = self.level_selection
                        self.current_scene.draw(self.screen)
                        
                    
                elif self.current_scene == self.level3:
                    self.current_scene.draw(self.screen, event)
                    if self.current_scene.end():
                        self.done3 = True
                        self.current_scene = self.level_selection
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.current_scene = self.level_selection
                        self.current_scene.draw(self.screen)
                        
                if self.done1 and self.done2 and self.done3:
                    self.screen.fill('black')
                    #self.cut_scene.ending()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                        
            pygame.display.update()


class Scene:
    def __init__(self):
        pass


class StartScreen(Scene):
    def __init__(self):
        super().__init__()
        w, h = pygame.display.get_surface().get_size()
        self.background = pygame.image.load('graphics/pictures/background.jpg').convert_alpha()
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.flag = pygame.image.load('graphics/flags/русск3.png').convert_alpha()
        self.flag_rect = self.flag.get_rect()
        self.settings = pygame.image.load('graphics/other/настр.png').convert_alpha()
        self.settings_rect = self.settings.get_rect()
        self.play = pygame.image.load('graphics/other/пуск2.png').convert_alpha()
        self.play_rect = self.play.get_rect(center=(w//2 + w/5, h//2))
        self.caption = pygame.image.load('graphics/other/логотип3.png').convert_alpha()
        self.caption_rect = self.caption.get_rect(center=(w//3, h//2))
        self.exit = pygame.image.load('graphics/other/выкл3.png').convert_alpha()
        self.exit_rect = self.exit.get_rect()
    def update(self):
        # Update the start screen
        pass

    def draw(self, screen):
        screen.blit(self.background, self.background_rect)
        screen.blit(self.caption, self.caption_rect)
        screen.blit(self.play, self.play_rect)


class Settings(Scene):
    def __init__(self):
        super().__init__()
        # Initialize the settings screen

    def update(self):
        # Update the settings screen
        pass

    def draw(self, screen):
        # Draw the settings screen
        pass


class LevelSelection(Scene):
    def __init__(self):
        super().__init__()
        w, h = pygame.display.get_surface().get_size()
        self.background = pygame.image.load('graphics/pictures/background.jpg').convert_alpha()
        self.background_rect = self.background.get_rect(topleft=(0, 0))
        self.level1 = pygame.image.load('graphics/pictures/рис1 (1).png')
        self.level1 = pygame.transform.scale(self.level1, (480, 270))
        self.level1_rect = self.level1.get_rect(center=(w//4 - w//10, h//2))
        self.level2 = pygame.image.load('graphics/pictures/рис2 (2).png')
        self.level2 = pygame.transform.scale(self.level2, (480, 270))
        self.level2_rect = self.level2.get_rect(center=(w//2, h//2))
        self.level3 = pygame.image.load('graphics/pictures/рис3 (3).png')
        self.level3 = pygame.transform.scale(self.level3, (480, 270))
        self.level3_rect = self.level3.get_rect(center=(w//4 + w//4 + w//4 + w//10, h//2))

    def update(self):
        # Update the level selection screen
        pass

    def draw(self, screen):
        screen.blit(self.background, self.background_rect)
        screen.blit(self.level1, self.level1_rect)
        screen.blit(self.level2, self.level2_rect)
        screen.blit(self.level3, self.level3_rect)


class CutScene(Scene):
    def __init__(self):
        super().__init__()
        self.movie = moviepy.editor.VideoFileClip("video/пушки акимбо 2.mp4")
        self.end = moviepy.editor.VideoFileClip("video/супер конец.mp4")
        
    def draw(self):
        if pygame.time.get_ticks() / 1000 < self.movie.end:
            self.movie.preview()
            
    def ending(self):
        self.end.preview()
        pygame.quit()
        sys.exit()

class Level(Scene):
    def __init__(self, picture):
        super().__init__()
        self.Surface = pygame.Surface((1920, 1080))
        self.picture = pygame.image.load(picture).convert_alpha()
        self.crystall = pygame.image.load('graphics/other/осколок3 (1).png')
        self.w, self.h = pygame.display.get_surface().get_size()
        self.crystals = []
        self.radius = 20
        self.last_click_time = 0
        self.mouse_clicked = False
        for i in range(5): # создаем 20 кристаллов
            crystal_x = random.randint(0, self.w - self.crystall.get_width())
            crystal_y = random.randint(0, self.h - self.crystall.get_height())
            self.crystals.append((crystal_x, crystal_y))
    def update(self):
        # Update the level
        pass

    def draw(self, screen, event):
        sound = Sound()
        picture_rect = self.picture.get_rect(center=(self.w//2, self.h//2))
        self.Surface.blit(self.picture, picture_rect)
        for crystal in self.crystals:
            crystal_rect = self.crystall.get_rect(center=crystal)
            self.Surface.blit(self.crystall, crystal_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if crystal_rect.collidepoint(event.pos):
                    self.crystals.remove(crystal)
                    self.last_click_time = time.time() + time.time()
                else:
                    self.last_click_time = time.time()
                    self.mouse_clicked = True
                        
            if self.mouse_clicked:
                if time.time() - self.last_click_time >=3:
                    sound.play()
                    self.mouse_clicked = False
                
        screen.blit(self.Surface, (0,0))
        
    def end(self):
        if self.crystals == []:
            return True
            
        



class Object:
    def __init__(self, picture):
        super().__init__()
        self.w, self.h = pygame.display.get_surface().get_size()
        self.picture = pygame.image.load(picture).convert_alpha()
    
    def draw(self, screen):
        picture_rect = self.picture.get_rect(center=(self.w//2, self.h//2))
        screen.blit(self.picture, picture_rect)
        
    def get_rects(self):
        return self.picture.get_rect(center=(self.w//2, self.h//2))

class Button:
    def __init__(self):
        super().__init__()
    
    def pressed(self, rect, event):
        if event.type == pygame.MOUSEBUTTONDOWN:           
            if rect.collidepoint(pygame.mouse.get_pos()):
                return True


class Sound:
    def __init__(self):
        super().__init__()
        self.sound_list = os.listdir('audio')
        
    def play(self):
        sound = pygame.mixer.Sound(f'audio/{random.choice(self.sound_list)}')
        sound.play()


class Timer:
    def __init__(self):
        pass
    
    
game = Game()
game.run()
