# Functions for menu creation are defined here to avoid clutter in CovidBlaster
from pygame import font
import pygame_menu

# Global variables for theme and font
# FONT = './assets/font/m5x7.ttf'
FONT = 'javanesetext'

THEME = pygame_menu.themes.THEME_DEFAULT
THEME.title_font = FONT
THEME.widget_font = FONT


def create_main_menu(resolution: tuple, choice: tuple) -> pygame_menu.Menu:
    x, y = resolution
    main_menu = pygame_menu.Menu('COVID BLASTER',800,600 , theme=THEME)
    main_menu.add.button('Play', choice[0])
    main_menu.add.button('High Scores', choice[1])
    main_menu.add.button('Settings', choice[2])
    main_menu.add.button('Quit', choice[3])
    return main_menu


def create_play_menu(resolution: tuple, choice: tuple) -> pygame_menu.Menu:
    x, y = resolution
    play_menu = pygame_menu.Menu('COVID BLASTER', 800, 600, theme=THEME)
    play_menu.add.button('BACK', choice[1])
    return play_menu


def create_hs_menu(resolution: tuple, choice: callable) -> pygame_menu.Menu:
    x, y = resolution
    hs_menu = pygame_menu.Menu('HIGH SCORES', 800,600, theme=THEME)
    for i in range(10): hs_menu.add.label('')
    hs_menu.add.button('BACK', choice)
    return hs_menu


def create_settings_menu(resolution: tuple, choice: tuple) -> pygame_menu.Menu:
    x, y = resolution
    settings_menu = pygame_menu.Menu('SETTINGS',800,600, theme=THEME)
    settings_menu.add.button('BACK', choice[1])
    return settings_menu
