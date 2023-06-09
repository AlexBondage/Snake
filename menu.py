import pygame_menu
from pygame_menu.examples import create_example_window


surface = create_example_window('Snake-menu', (800, 600))





def start_the_game():
    print(f'{user_pass.get_value()}, - пароль',f'{user_name.get_value()}, - имя')
    import main

menu = pygame_menu.Menu(
    height=600,
    theme=pygame_menu.themes.THEME_GREEN,

    title='Snake',
    width=800
)

user_name = menu.add.text_input('Имя: ', default='User', maxchar=10)
user_pass = menu.add.text_input('Пароль: ', default='123', maxchar=10)
menu.add.button('Играть', start_the_game)
menu.add.button('Выйти', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)