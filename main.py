# Імпорти
import sqlite3
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
import random
from random import randint


class Main(Screen):
    # Готовна ігрова сторінка
    click_sound = None
    button_clicked = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ініціалізуємо звукові ефекти
        if not Main.click_sound:
            Main.click_sound = SoundLoader.load('rigths/sounds/click.mp3')
            Main.screen = SoundLoader.load('rigths/sounds/screen-3.mp3')
            Main.screen.volume = 0.1
            Main.screen_4 = SoundLoader.load('rigths/sounds/screen-4.mp3')
            Main.screen_4.volume = 0.1
            Main.dragon_s = SoundLoader.load('rigths/sounds/dragon.mp3')
            Main.dragon_s.volume = 0.1
            Main.dragon_v = SoundLoader.load('rigths/sounds/dragon-v.mp3')
            Main.dragon_v.volume = 0.1
            Main.demon = SoundLoader.load('rigths/sounds/demon.mp3')
            Main.demon.volume = 0.2
            Main.punch = SoundLoader.load('rigths/sounds/punch.mp3')
            Main.punch.volume = 0.2
            Main.win = SoundLoader.load('rigths/sounds/win.mp3')
            Main.win.volume = 0.3
            Main.papagei = SoundLoader.load('rigths/sounds/papagei.mp3')
            Main.papagei.volume = 0.1

# Для дизайну початкового екрану
class CustomButton(Button):
    pass

class CustomBlock1(Button):
    pass

class CustomBlock2(Button):
    pass

class CustomBlock3(Button):
    pass

class WelcomeScreen(Screen):
    # Початкова сторінка
    player = None  # Зробимо player статичним атрибутом класу
    sound = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file('custom.kv')
        # Відтворюємо відео на початковому екрані 
        layout = FloatLayout()
        if WelcomeScreen.player is None:  # Перевіряємо, чи player вже був створений
            WelcomeScreen.player = VideoPlayer(source='rigths/video.mp4', state='play', options={'allow_stretch': True})
            WelcomeScreen.player.state = 'play'
            WelcomeScreen.player.size_hint = (1, 1)
            WelcomeScreen.player.pos_hint = {'x': 0, 'y': 0}
            WelcomeScreen.player.options = {'eos': 'loop'}
            WelcomeScreen.player.allow_stretch = True
            WelcomeScreen.player.volume = 0.1
        button = CustomButton()
        block1 = CustomBlock1()
        block2 = CustomBlock2()
        block3 = CustomBlock3()
        button.bind(on_release=self.on_button_click)
        layout.add_widget(WelcomeScreen.player)
        layout.add_widget(block1)
        layout.add_widget(block2)
        layout.add_widget(block3)
        layout.add_widget(button)
        self.add_widget(layout)


    def on_button_click(self, instance):
        # Переходимно на готовний екран та відтворюємо музику після натискання кнопки
        self.manager.current = 'main'
        WelcomeScreen.player.state = 'stop'
        if not WelcomeScreen.sound:
            WelcomeScreen.sound = SoundLoader.load('rigths/sounds/BG.mp3')  
            if WelcomeScreen.sound:
                WelcomeScreen.sound.loop = True 
                WelcomeScreen.sound.volume = 0.3
                WelcomeScreen.sound.play()


class GameApp(App):
    title = ""
    # Window.size = (380, 800)
    db_name = "click.db"
    button_state = 0
    perot_button_shown = False
    min_delay = 60  # Мінімальна затримка перед появленням папуги
    max_delay = 120  # Максимальна затримка перед появленням папуги
    hide_delay = 10
    parott = True

    def build(self):
        # self.theme_cls.theme_style = "Dark"  
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome_screen'))  # Додаємо екран вітання перед Main
        sm.add_widget(Main(name='main'))
        return sm
    
    def change_dragon_image(self):
        # При натиску на око дракона відкриваєм рандомно фрази дракона
        dragon_images = ['rigths/img/dragon_img-1.png', 'rigths/img/dragon_img-2.png', 'rigths/img/dragon_img-3.png', 'rigths/img/dragon_img-4.png', 'rigths/img/dragon_img-5.png', 'rigths/img/dragon_img-6.png', 'rigths/img/dragon_img-7.png', 'rigths/img/dragon_img-8.png', 'rigths/img/dragon_img-9.png', 'rigths/img/dragon_img-10.png', 'rigths/img/dragon_img-11.png', 'rigths/img/dragon_img-12.png', 'rigths/img/dragon_img-13.png', 'rigths/img/dragon_img-14.png', 'rigths/img/dragon_img-15.png', 'rigths/img/dragon_img-16.png', 'rigths/img/dragon_img-17.png', 'rigths/img/dragon_img-18.png', 'rigths/img/dragon_img-19.png', 'rigths/img/dragon_img-20.png']
        random_dragon_image = random.choice(dragon_images)
        self.root.get_screen('main').ids.background.source = random_dragon_image
        if Main.button_clicked == True:
            Main.dragon_s.play()
            

    def change_parrot_image(self):
        # При натиску на папугу відкриваєм рандомно сувої які нам приніс папуга
        parrot_images = ['rigths/img/parrot_img-1.png', 'rigths/img/parrot_img-2.png', 'rigths/img/parrot_img-3.png', 'rigths/img/parrot_img-4.png', 'rigths/img/parrot_img-5.png', 'rigths/img/parrot_img-6.png', 'rigths/img/parrot_img-7.png', 'rigths/img/parrot_img-8.png', 'rigths/img/parrot_img-9.png', 'rigths/img/parrot_img-10.png', 'rigths/img/parrot_img-11.png', 'rigths/img/parrot_img-12.png', 'rigths/img/parrot_img-13.png', 'rigths/img/parrot_img-14.png']
        random_parrot_image = random.choice(parrot_images)
        self.root.get_screen('main').ids.background.source = random_parrot_image
        if Main.button_clicked == True:
            Main.dragon_s.play()
        

    def show_perot_button(self, *args):
        # Показуємо папугу після того як ми з ним подружились, він прилітає на 10с кожні 60-120с
        if 1350 <= int(self.root.get_screen('main').ids.coins.text) <= 2550:
            if not self.perot_button_shown:
                self.perot_button_shown = True
                delay = randint(self.min_delay, self.max_delay)
                Clock.schedule_once(self.hide_perot_button, self.hide_delay)  # Показуємо кнопку на 10 секунд
                Clock.schedule_once(self.show_perot_button, delay)  # Запускаємо таймер для наступного появлення кнопки
                self.root.get_screen('main').ids.perot_button.opacity = 1
                self.root.get_screen('main').ids.perot_button.pos_hint = {'center_x': 0.15, 'center_y': 0.93}
                if Main.button_clicked == True:
                    Main.papagei.play()

    def hide_perot_button(self, *args):
        # Папуга зникає
        self.perot_button_shown = False
        self.root.get_screen('main').ids.perot_button.opacity = 0
        self.root.get_screen('main').ids.perot_button.pos_hint = {'center_x': -1, 'center_y': 0.2}

    def on_click(self):
        # Логіка обробки натискання кнопки
        coins_label = self.root.get_screen('main').ids.coins
        coins = int(coins_label.text)
        # Додаткові умови обробки натискання кнопки для відображення зміни історії 
        if 0 <= coins <= 4:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-1.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 5 <= coins <= 30:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 31 <= coins <= 32:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-2.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 33 <= coins <= 40:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-2.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 41 <= coins <= 45:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-3.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 46 <= coins <= 85:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 86 <= coins <= 87:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-4.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.dragon_v.play()
        if 88 <= coins <= 95:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-4.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 96 <= coins <= 250:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 251 <= coins <= 252:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-5.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 253 <= coins <= 260:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-5.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 261 <= coins <= 268:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-6.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 269 <= coins <= 340:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 341 <= coins <= 342:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-7.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen_4.play()
        if 343 <= coins <= 350:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-7.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 351 <= coins <= 358:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-8.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 359 <= coins <= 440:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 441 <= coins <= 442:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-eye.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.dragon_v.play()
        if 443 <= coins <= 450:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-eye.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 451 <= coins <= 495:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 496 <= coins <= 497:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-9.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 498 <= coins <= 502:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-9.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 503 <= coins <= 508:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-10.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 508 <= coins <= 900:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins + 5)
            self.save_click_count(coins_label.text)
        if 901 <= coins <= 902:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-11.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 903 <= coins <= 911:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-11.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 911 <= coins <= 930:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 931 <= coins <= 932:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-12.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 933 <= coins <= 941:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-12.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 942 <= coins <= 948:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-13.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 949 <= coins <= 960:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 961 <= coins <= 962:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-14.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 963 <= coins <= 971:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-14.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 971 <= coins <= 978:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-15.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 979 <= coins <= 1089:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1090 <= coins <= 1091:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-16.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1092 <= coins <= 1100:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-16.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1101 <= coins <= 1102:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-17.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1103 <= coins <= 1108:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-17.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1109 <= coins <= 1115:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-18.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1116 <= coins <= 1122:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-19.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1123 <= coins <= 1124:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-20.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1123 <= coins <= 1130:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-20.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1131 <= coins <= 1138:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-21.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1138 <= coins <= 1280:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1281 <= coins <= 1282:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-22.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1283 <= coins <= 1291:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-22.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1292 <= coins <= 1293:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-23.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1294 <= coins <= 1302:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-23.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1303 <= coins <= 1310:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-24.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1311 <= coins <= 1399:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1400 <= coins <= 1401:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-25.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen_4.play()
        if 1402 <= coins <= 1410:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-25.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1411 <= coins <= 1418:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-26.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1419 <= coins <= 1490:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1491 <= coins <= 1492:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-27.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1493 <= coins <= 1500:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-27.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1501 <= coins <= 1510:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-28.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1511 <= coins <= 1590:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1591 <= coins <= 1592:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-29.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1593 <= coins <= 1601:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-29.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1602 <= coins <= 1612:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-30.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1613 <= coins <= 1614:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-31.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1615 <= coins <= 1620:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-31.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1621 <= coins <= 1630:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-32.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1631 <= coins <= 1700:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1701 <= coins <= 1710:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-33.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1711 <= coins <= 1740:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-f.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1741 <= coins <= 1742:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-34.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 1743 <= coins <= 1750:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-34.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1751 <= coins <= 1760:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-35.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1761 <= coins <= 1800:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-36.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1801 <= coins <= 1850:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-37.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 1851 <= coins <= 2000:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-38.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2001 <= coins <= 2051:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-39.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2051 <= coins <= 2100:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-40.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2101 <= coins <= 2150:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-41.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2151 <= coins <= 2200:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-42.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2201 <= coins <= 2250:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-43.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2251 <= coins <= 2300:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-44.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2301 <= coins <= 2350:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-45.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2351 <= coins <= 2400:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-46.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2401 <= coins <= 2410:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-47.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2411 <= coins <= 2420:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-48.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2421 <= coins <= 2430:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-49.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2431 <= coins <= 2450:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-50.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2451 <= coins <= 2460:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-51.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2461 <= coins <= 2462:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-52.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.demon.play()
        if 2463 <= coins <= 2470:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-52.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2471 <= coins <= 2480:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-53.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2481 <= coins <= 2482:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-54.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.screen.play()
        if 2483 <= coins <= 2490:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-54.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2491 <= coins <= 2500:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-55.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2501 <= coins <= 2590:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-ff.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2591 <= coins <= 2592:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-56.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.punch.play()
        if 2593 <= coins <= 2600:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-56.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2601 <= coins <= 2602:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-57.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.dragon_v.play()
        if 2603 <= coins <= 2610:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-57.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        if 2611 <= coins <= 2612:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-58.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
            if Main.button_clicked == True:
                Main.win.play()
        if 2613 <= coins <= 2620:
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen-58.png'
            coins_label.text = str(coins + 1)
            self.save_click_count(coins_label.text)
        else:
            if 508 <= coins <= 895:
                self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
                coins_label.text = str(coins + 5)
                self.save_click_count(coins_label.text)
            else:
                coins_label.text = str(coins + 1)
                self.save_click_count(coins_label.text)
            
        if coins > 2620:
            # Скидання гри якшо ми вже пройшли все
            self.root.get_screen('main').ids.background.source = 'rigths/img/screen.png'
            coins_label.text = str(coins - 2620)
            self.save_click_count(coins_label.text)

        if self.button_state == 0:
            # Анімація кнопки
            anim = Animation(size_hint=(0.25, 1),pos_hint={'center_x': 0.5, 'center_y': 0.5}, duration=0.1)
            self.button_state = 1
        else:
            anim = Animation(size_hint=(0.2, 1), duration=0.1)
            self.button_state = 0

        anim.start(coins_label)

        # Запуск функції з папугою в певний час
        if 1350 <= coins <= 2550:
            if self.parott == True:
                self.show_perot_button()
                self.parott = False

        # Обробка звуків при натиску на кнопку
        if Main.button_clicked == True:
            Main.click_sound.volume = 0.1
            Main.click_sound.play()
        if Main.button_clicked == False:
            Main.button_clicked = True
        

    def save_click_count(self, count):
        # Зберігаємо кількість натискань у базу даних
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM clicks")
        c.execute("INSERT INTO clicks VALUES (?)", (count,))
        conn.commit()
        conn.close()

    def load_click_count(self):
        # Завантажуємо кількість натискань з бази даних
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM clicks")
        result = c.fetchone()
        conn.close()
        return str(result[0]) if result else "0"
    

    def on_start(self):
        # Викликається при старті додатку
        coins_label = self.root.get_screen('main').ids.coins
        coins_label.text = self.load_click_count()
    
if __name__ == '__main__':
    # Реєстрація шрифту та запуск додатку
    LabelBase.register(name="Press Start 2P",
                    fn_regular='./font/PressStart2P-Regular.ttf')
    app = GameApp()
    app.run()