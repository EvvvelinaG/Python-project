# -*- coding: utf-8 -*-

# import tkinter
from tkinter import *
# from tkinter.ttk import *
import tkinter.ttk

import tkvideo
import random
import pygame

pygame.init()


def v_click():
    root.destroy()


class GameSettings:
    def matrix(column, line):
        GameSettings.buttons_Map = [0] * line
        for i in range(line):
            GameSettings.buttons_Map[i] = [0] * column
        for i in range(line):
            for j in range(column):
                GameSettings.buttons_Map[i][j] = Label(root, activebackground='lightgray',  # relief='flat',
                                                       image=GameSettings.pictures[GameSettings.field[i][j]], bd=0,
                                                       bg='black')

        return GameSettings.buttons_Map

    volume = 1
    music = True
    right_answers = 0
    m_clicked = True
    help_or_settings = True
    column = 20
    line = 11
    height = 50
    field = [0] * column
    buttons_Map = matrix(column, line)
    reserve_i = 0
    reserve_j = 0

    release_moderator = 0
    menu_moderator = 0
    boss_moderator = 0
    coordinates_lock = 0
    mob_hp_const = 100
    mob_hp = mob_hp_const
    hero_hp = 99

    hits_min = [90, 40, 20]
    mob_min = 10
    hits_max = [101, 60, 30]
    mob_max = 30
    chances = [90, 50, 20, 50, 70, 50]

    attack_value = 1.1
    defense_value = 1
    dodge_chance = 1
    damage = 1.1
    lvl = 0

    attack_lvl = 0
    defense_lvl = 0
    dodge_lvl = 0

    blindness = 1
    unstable = 1
    disarmed = 1

    location = 1
    frags = 0
    question_number = 0
    answer_number = 0
    comment_number = 0

    game_start = False
    boss_fight = False
    knowledge = False

    start_game_button = Button()
    settings_game_button = Button()
    volume_game_button_0 = Button()
    volume_game_button_0_25 = Button()
    volume_game_button_0_5 = Button()
    volume_game_button_0_75 = Button()
    volume_game_button_1 = Button()
    mob_hp_bar = Label()
    label_help = Label()
    label_help2 = Label()
    label_help3 = Label()
    label_about = Label()
    menu_window = Label()
    hero_hp_bar = Label()
    volume_game_label = Label()
    fighting_label = Label()
    defeat_l = Label()
    back_game_button = Button()
    help_game_button = Button()
    exit_game_button = Button()
    again_game_button = Button()
    opening_close = Button()
    about = Button()
    small_exit_button = Button()

    Ground = tkinter.PhotoImage(file='Ground.png')
    Character = tkinter.PhotoImage(file='Character.png')
    Flashback = tkinter.PhotoImage(file='Flashback.png')
    Door = tkinter.PhotoImage(file='Door.png')
    Character_Revers = tkinter.PhotoImage(file='Character_Revers.png')
    Character_Back = tkinter.PhotoImage(file='Character_Back.png')
    Character_Front = tkinter.PhotoImage(file='Character_Front.png')
    Boss_pic = tkinter.PhotoImage(file='Boss.png')
    Mob = tkinter.PhotoImage(file='Mob.png')
    pictures = [Ground, Ground, Character, Flashback, Door, Boss_pic, Character_Revers, Character_Back,
                Character_Front, Mob]

    Fighting_Head = tkinter.PhotoImage(file='Fighting_Head.png')
    Fighting_Body = tkinter.PhotoImage(file='Fighting_Body.png')
    Fighting_Legs = tkinter.PhotoImage(file='Fighting_Legs.png')
    Fight_Pictures = [Fighting_Head, Fighting_Body, Fighting_Legs]


Number_Of_Questions = 11
Number_Of_Comments = 11
Height = 50

Damage = 1.1

for i in range(GameSettings.column):
    GameSettings.field[i] = [0] * GameSettings.line

Comments = [''] * Number_Of_Comments
Questions = [''] * Number_Of_Questions
Answers = [''] * Number_Of_Questions * 3
Speech = [''] * 2

root = Tk()
root.title("")
root.state('zoomed')
# root.geometry('1600x900')
root["bg"] = '#3c3c3c'

Background_Image_Forest = tkinter.PhotoImage(file='Map.png')
Background_Image_Ladder = tkinter.PhotoImage(file='Map2.png')
Background_Image_Desert = tkinter.PhotoImage(file='Map3.png')
Fighting = tkinter.PhotoImage(file='Fighting.png')
Fighting2 = tkinter.PhotoImage(file='Fighting_Boss.png')
Fighting_Head_Boss = tkinter.PhotoImage(file='Fighting_Boss_Head.png')
Fighting_Body_Boss = tkinter.PhotoImage(file='Fighting_Boss_Body.png')
Fighting_Legs_Boss = tkinter.PhotoImage(file='Fighting_Boss_Legs.png')
Journal_Bg = tkinter.PhotoImage(file='Journal.png')

Upper_Main_Menu = Menu(root)
root.config(menu=Upper_Main_Menu)

filemenu = Menu(Upper_Main_Menu, tearoff=0)

Ground2 = tkinter.PhotoImage(file='Ground2.png')
Small_Exit = tkinter.PhotoImage(file='Small_Exit.png')
Skeleton = tkinter.PhotoImage(file='Skeleton.png')
Skeleton2 = tkinter.PhotoImage(file='Skeleton2.png')
About_Img = tkinter.PhotoImage(file='мы.jpg')
About_Lbl = tkinter.PhotoImage(file='Разработчики.png')
Help_Page = tkinter.PhotoImage(file='H_P.png')
Help_Page2 = tkinter.PhotoImage(file='H_F.png')
Help_Page3 = tkinter.PhotoImage(file='H_Q.png')
Menu_Background = tkinter.PhotoImage(file='Background.png')
Close = tkinter.PhotoImage(file='Закрыть Заставку.png')
Back = tkinter.PhotoImage(file='Назад.png')
Start = tkinter.PhotoImage(file='Начать.png')
Return = tkinter.PhotoImage(file='Вернуться в игру.png')
Settings = tkinter.PhotoImage(file='Настройки.png')
Help = tkinter.PhotoImage(file='Помощь.png')
Exit = tkinter.PhotoImage(file='Выход.png')
Again = tkinter.PhotoImage(file='Начать Заново.png')

Comrade = tkinter.PhotoImage(file='Fresco.png')
Guts = tkinter.PhotoImage(file='Guts.png')

Background = tkinter.PhotoImage(file='Bg.png')
Main_Background = Label(root, image=Background, bd=0)
Main_Background.place(x=0, y=0)
Background_Label = Label(root, image=Background_Image_Forest, bg='gray')

# Получение первой локации
Text_Map = open('Forest.txt', 'r')
for i in range(GameSettings.line):
    Lines = Text_Map.readline()
    s = Lines.split()
    for j in range(GameSettings.column):
        GameSettings.field[j][i] = int(s[j])
Text_Map.close()

# Текстовый файл с вопросами
Text_Question = open('Questions.txt', 'r')
for i in range(Number_Of_Questions):
    Questions[i] = Text_Question.readline()
Text_Question.close()

Text_Comments = open('Comments.txt', 'r')
for i in range(Number_Of_Comments):
    Comments[i] = Text_Comments.readline()
Text_Comments.close()

# Текстовый файл с ответами
Text_Answers = open('Answers.txt', 'r')
for i in range(Number_Of_Questions * 3):
    Answers[i] = Text_Answers.readline()
Text_Answers.close()

Text_Boss = open('Boss.txt', 'r')
for i in range(2):
    Speech[i] = Text_Boss.readline()
Text_Boss.close()


# выбор ответа на вопрос
def options():
    Comrade_Label.place(x=1268, y=20)
    Label_Comments.place_forget()
    Label_Question['text'] = Questions[GameSettings.question_number]
    first_option = random.randint(0, 2)
    second_option = first_option
    third_option = first_option
    while second_option == first_option or second_option == third_option:
        second_option = random.randint(0, 2)
    while third_option == first_option or third_option == second_option:
        third_option = random.randint(0, 2)

    First_Answer_Button['text'] = Answers[first_option + GameSettings.answer_number]
    Second_Answer_Button['text'] = Answers[second_option + GameSettings.answer_number]
    Third_Answer_Button['text'] = Answers[third_option + GameSettings.answer_number]

    First_Answer_Button.place(x=1250, y=450)
    Second_Answer_Button.place(x=1250, y=500)
    Third_Answer_Button.place(x=1250, y=550)
    Label_Question.place(x=1250, y=220)
    # First_Answer_Button.place(x=1225, y=500)
    # Second_Answer_Button.place(x=1325, y=550)
    # Third_Answer_Button.place(x=1425, y=600)

    GameSettings.buttons_Map[GameSettings.reserve_i + 1][GameSettings.reserve_j]['state'] = 'disabled'
    GameSettings.buttons_Map[GameSettings.reserve_i - 1][GameSettings.reserve_j]['state'] = 'disabled'
    GameSettings.buttons_Map[GameSettings.reserve_i][GameSettings.reserve_j + 1]['state'] = 'disabled'
    GameSettings.buttons_Map[GameSettings.reserve_i][GameSettings.reserve_j - 1]['state'] = 'disabled'
    GameSettings.coordinates_lock = 1


# бой с боссом
def boss():
    GameSettings.boss_fight = True
    GameSettings.boss_moderator = 1
    Boss_Label.place(x=1268, y=20)
    First_Boss_Button['text'] = 'Начать сражение'
    First_Boss_Button.place(x=1250, y=650)
    if GameSettings.right_answers > 9:
        Second_Boss_Button['text'] = 'Я всё понял'
        Second_Boss_Button.place(x=1250, y=700)
    Label_Boss.place_forget()
    Label_Boss['text'] = Speech[0]
    Label_Boss.place(x=1250, y=220)
    GameSettings.buttons_Map[GameSettings.reserve_i + 2][GameSettings.reserve_j]['state'] = 'disabled'
    GameSettings.buttons_Map[GameSettings.reserve_i + 1][GameSettings.reserve_j + 1]['state'] = 'disabled'
    GameSettings.buttons_Map[GameSettings.reserve_i + 1][GameSettings.reserve_j - 1]['state'] = 'disabled'
    GameSettings.coordinates_lock = 1


# проверка правильности ответа
def checking_the_answer(num):
    result_of_checking = False
    if num == 1 and First_Answer_Button['text'] == Answers[1 + GameSettings.answer_number]:
        result_of_checking = True
    elif num == 2 and Second_Answer_Button['text'] == Answers[1 + GameSettings.answer_number]:
        result_of_checking = True
    elif num == 3 and Third_Answer_Button['text'] == Answers[1 + GameSettings.answer_number]:
        result_of_checking = True
    if result_of_checking:
        GameSettings.right_answers += 1
        Journal['fg'] = '#47402c'
        if GameSettings.hero_hp < 100:
            GameSettings.hero_hp = 100
            Journal['text'] = 'Здоровье восстановлено'
        elif GameSettings.attack_lvl < 4:
            for i in range(len(GameSettings.chances)):
                GameSettings.chances[i] = int(GameSettings.chances[i] // GameSettings.attack_value)
            Journal['text'] = 'Атака повышена'
            GameSettings.lvl += 1
            GameSettings.attack_lvl += 1
        elif GameSettings.dodge_lvl == 0 and GameSettings.attack_lvl > 3:
            GameSettings.dodge_chance = 0.8
            Journal['text'] = 'Вероятность уклонения повышена'
            GameSettings.lvl += 1
            GameSettings.dodge_lvl += 1
        elif GameSettings.dodge_lvl > 0:
            GameSettings.defense_value = 0.8
            Journal['text'] = 'Защита повышена'
            GameSettings.lvl += 1
            GameSettings.defense_lvl += 1
        else:
            Journal['text'] = 'Вы достигли максимального уровня!'
    else:
        Journal['fg'] = '#989898'

    GameSettings.coordinates_lock = 0
    Label_Question.place_forget()
    First_Answer_Button.place_forget()
    Second_Answer_Button.place_forget()
    Third_Answer_Button.place_forget()
    GameSettings.question_number += 1
    GameSettings.answer_number += 3
    Comrade_Label.place_forget()
    Label_Comments['text'] = Comments[GameSettings.comment_number]
    GameSettings.buttons_Map[GameSettings.reserve_i + 1][GameSettings.reserve_j]['state'] = 'normal'
    GameSettings.buttons_Map[GameSettings.reserve_i - 1][GameSettings.reserve_j]['state'] = 'normal'
    GameSettings.buttons_Map[GameSettings.reserve_i][GameSettings.reserve_j + 1]['state'] = 'normal'
    GameSettings.buttons_Map[GameSettings.reserve_i][GameSettings.reserve_j - 1]['state'] = 'normal'


# проверка ответа на вопрос босса
def boss_answer(num):
    if num == 1:
        GameSettings.fighting_label['image'] = Fighting2
        GameSettings.mob_min = 20
        GameSettings.mob_max = 40
        if GameSettings.knowledge:
            GameSettings.mob_min = 5
            GameSettings.mob_max = 15
        First_Boss_Button.place_forget()
        Label_Boss.place_forget()
        Boss_Label.place_forget()
        Second_Boss_Button.place_forget()
        GameSettings.Fight_Pictures = [Fighting_Head_Boss, Fighting_Body_Boss, Fighting_Legs_Boss]
        fight()
    elif num == 2:
        Achivement_4['text'] = 'ПОБЕСЕДОВАТЬ ПЕРЕД БИТВОЙ: УСПЕХ'
        Boss_Label['image'] = Skeleton2
        Label_Boss['text'] = Speech[1]
        First_Boss_Button.place(x=1250, y=400)
        Second_Boss_Button.place_forget()
        GameSettings.knowledge = True


# перемещение на следующую локацию
def change_location():
    GameSettings.location += 1
    hide(GameSettings.column, GameSettings.line)
    if GameSettings.location == 1:
        Journal['fg'] = '#989898'
        pygame.mixer.music.load('OST1.mp3')
        pygame.mixer.music.play(-1)
        GameSettings.mob_hp_const = 100
        Background_Label['image'] = Background_Image_Forest
        lab = open('Forest.txt', 'r')
        for i in range(GameSettings.line):
            lines = lab.readline()
            s = lines.split()
            for j in range(GameSettings.column):
                GameSettings.field[j][i] = int(s[j])
        lab.close()
    if GameSettings.location == 2:
        GameSettings.question_number = 6
        GameSettings.answer_number = GameSettings.question_number * 3
        GameSettings.mob_hp_const = 200
        pygame.mixer.music.load('OST2.mp3')
        pygame.mixer.music.play(-1)
        Background_Label['image'] = Background_Image_Ladder
        lab = open('Ladder.txt', 'r')
        for i in range(GameSettings.line):
            lines = lab.readline()
            s = lines.split()
            for j in range(GameSettings.column):
                GameSettings.field[j][i] = int(s[j])
        lab.close()
    elif GameSettings.location == 3:
        GameSettings.mob_hp_const = 600
        pygame.mixer.music.load('OST3.mp3')
        pygame.mixer.music.play(-1)
        Background_Label['image'] = Background_Image_Desert
        lab = open('Third.txt', 'r')
        for i in range(GameSettings.line):
            lines = lab.readline()
            s = lines.split()
            for j in range(GameSettings.column):
                GameSettings.field[j][i] = int(s[j])
        lab.close()
    elif GameSettings.location == 4:
        pygame.mixer.music.load('Fly me to the moon.mp3')
        pygame.mixer.music.play(-1)
    GameSettings.buttons_Map = GameSettings.matrix(GameSettings.column, GameSettings.line)
    output(GameSettings.column, GameSettings.line)
    destroying()
    create()


# поражение героя
def defeat():
    GameSettings.right_answers = 0
    GameSettings.frags = 0
    GameSettings.Fight_Pictures = [GameSettings.Fight_Head, GameSettings.Fight_Body, GameSettings.Fight_Legs]
    GameSettings.knowledge = False
    GameSettings.boss_fight = False
    Boss_Label['image'] = Skeleton
    GameSettings.mob_min = 10
    GameSettings.mob_max = 30
    Journal['fg'] = '#47402c'
    Journal['text'] = 'Герой погиб'
    GameSettings.again_game_button.place(x=540, y=100)
    menu_output()
    GameSettings.start_game_button.place_forget()
    First_Fighting_Button.place_forget()
    Second_Fighting_Button.place_forget()
    Third_Fighting_Button.place_forget()
    Forth_Fighting_Button.place_forget()
    Fifth_Fighting_Button.place_forget()
    Sixth_Fighting_Button.place_forget()
    Seventh_Fighting_Button.place_forget()
    GameSettings.mob_hp_bar.place_forget()
    GameSettings.hero_hp_bar.place_forget()
    GameSettings.defeat_l.place(x=650, y=45)
    GameSettings.hero_hp_bar['text'] = 0
    Enemy_Journal.place_forget()
    GameSettings.location = 0
    GameSettings.hero_hp = 99
    GameSettings.hits_min = [90, 40, 20]
    GameSettings.hits_max = [101, 60, 30]
    GameSettings.chances = [90, 50, 20, 50, 70, 50]
    GameSettings.defense_value = 1
    GameSettings.dodge_chance = 1
    GameSettings.lvl = 0
    GameSettings.question_number = 0
    GameSettings.answer_number = 0
    GameSettings.comment_number = 0
    GameSettings.dodge_lvl = 0
    GameSettings.attack_lvl = 0
    GameSettings.defense_lvl = 0
    pygame.mixer.music.load('OST4.mp3')
    pygame.mixer.music.play(-1)


# атака моба
def fight_back():
    if GameSettings.mob_hp > 0:
        mob_hit = int(random.randint(GameSettings.mob_min,
                                     GameSettings.mob_max) * GameSettings.defense_value * GameSettings.disarmed)
        mob_chance = random.randint(0, 100) * GameSettings.dodge_chance * GameSettings.blindness
        if mob_chance >= 60:
            GameSettings.hero_hp = int(GameSettings.hero_hp - mob_hit)
            GameSettings.hero_hp_bar['text'] = GameSettings.hero_hp
            Enemy_Journal['text'] = 'Скелет нанёс ' + str(mob_hit) + ' урона'
            if GameSettings.hero_hp <= 0:
                if GameSettings.boss_fight:
                    First_Fighting_Button.place_forget()
                    Second_Fighting_Button.place_forget()
                    Third_Fighting_Button.place_forget()
                    Forth_Fighting_Button.place_forget()
                    Fifth_Fighting_Button.place_forget()
                    Sixth_Fighting_Button.place_forget()
                    Seventh_Fighting_Button.place_forget()
                    GameSettings.small_exit_button.place(x=1250, y=706)
                    Achivement_1['text'] = 'ОТВЕТИТЬ ПРАВИЛЬНО НА ВСЕ ВОПРОСЫ: ПРОВАЛ'
                    Achivement_2['text'] = 'УБИТЬ ВСЕХ ОБЫЧНЫХ СКЕЛЕТОВ: ПРОВАЛ'
                    Achivement_3['text'] = 'УБИТЬ БОССА: ПРОВАЛ'
                    if GameSettings.right_answers > 10:
                        Achivement_1['text'] = 'ОТВЕТИТЬ ПРАВИЛЬНО НА ВСЕ ВОПРОСЫ: УСПЕХ'
                    if GameSettings.frags > 14:
                        Achivement_2['text'] = 'УБИТЬ ВСЕХ ОБЫЧНЫХ СКЕЛЕТОВ: УСПЕХ'
                    Achivement_1.place(x=1250, y=106)
                    Achivement_2.place(x=1250, y=206)
                    Achivement_3.place(x=1250, y=306)
                    Achivement_4.place(x=1250, y=406)
                    Journal['text'] = 'Герой погиб'
                    pygame.mixer.music.load('End_OST.mp3')
                    pygame.mixer.music.play(0)
                    GameSettings.mob_hp_bar.place_forget()
                    GameSettings.hero_hp_bar.place_forget()
                    my_label2 = Label(root, bg='gray')  # , bd=6, relief='raised')
                    my_label2.place(x=0, y=0)
                    player2 = tkvideo.tkvideo("Bad_End.mp4", my_label2, loop=0, size=(1200, 700))
                    player2.play()
                else:
                    defeat()
            elif GameSettings.hero_hp <= 30:
                GameSettings.hero_hp_bar['fg'] = 'red'
        else:
            Enemy_Journal['text'] = 'Скелет промахнулся'


# атака героя
def attack(num):
    Forth_Fighting_Button.place_forget()
    if num < 4:
        Fifth_Fighting_Button.place_forget()
        Sixth_Fighting_Button.place_forget()
        Seventh_Fighting_Button.place_forget()
        hit_min = GameSettings.hits_min[num]
        hit_max = GameSettings.hits_max[num]
        chance = GameSettings.chances[num]
        GameSettings.fighting_label['image'] = GameSettings.Fight_Pictures[num]
        Fighting_Buttons[num].place(x=1268, y=420)
    Forth_Fighting_Button.place(x=1268, y=320)
    random_chance = random.randint(0, 100)
    if num == 5:
        Sixth_Fighting_Button.place_forget()
        Seventh_Fighting_Button.place_forget()
        r_blind = random.randint(0, 100)
        Journal['text'] = 'Не удалось ослепить скелета'
        if r_blind > GameSettings.chances[3]:
            GameSettings.blindness = 0.8
            Fifth_Fighting_Button['state'] = 'disabled'
            Journal['text'] = 'Скелет ослеплён'
        fight_back()

    elif num == 6:
        Fifth_Fighting_Button.place_forget()
        Seventh_Fighting_Button.place_forget()
        r_disarmed = random.randint(0, 100)
        Journal['text'] = 'Не удалось обезоружить скелета'
        if r_disarmed > GameSettings.chances[4]:
            GameSettings.disarmed = 0.5
            Sixth_Fighting_Button['state'] = 'disabled'
            Journal['text'] = 'Скелет обезоружен'
        fight_back()

    elif num == 7:
        Fifth_Fighting_Button.place_forget()
        Sixth_Fighting_Button.place_forget()
        r_stable = random.randint(0, 100)
        Journal['text'] = 'Не удалось обездвижить скелета'
        if r_stable > GameSettings.chances[5]:
            GameSettings.unstable = 0.7
            First_Fighting_Button['text'] = 'Мощная ' + str(
                100 - int(GameSettings.chances[num - 7] * GameSettings.unstable)) + '%'
            Second_Fighting_Button['text'] = 'Обычная ' + str(
                100 - int(GameSettings.chances[num - 6] * GameSettings.unstable)) + '%'
            Third_Fighting_Button['text'] = 'Быстрая ' + str(
                100 - int(GameSettings.chances[num - 5] * GameSettings.unstable)) + '%'
            Seventh_Fighting_Button['state'] = 'disabled'
            Journal['text'] = 'Скелет обездвижен'
        fight_back()

    elif num == 4:

        if random_chance >= (chance * GameSettings.unstable):
            random_hit = random.randint(hit_min, hit_max)
            GameSettings.mob_hp = GameSettings.mob_hp - random_hit
            GameSettings.mob_hp_bar['text'] = GameSettings.mob_hp
            Journal['text'] = 'Нанесён урон скелету ' + str(random_hit)
        else:
            Journal['text'] = 'Ваша атака прошла безуспешно'
        fight_back()

    if GameSettings.mob_hp <= 0 < GameSettings.hero_hp:
        if GameSettings.boss_fight:
            First_Fighting_Button.place_forget()
            Second_Fighting_Button.place_forget()
            Third_Fighting_Button.place_forget()
            Forth_Fighting_Button.place_forget()
            Fifth_Fighting_Button.place_forget()
            Sixth_Fighting_Button.place_forget()
            Seventh_Fighting_Button.place_forget()
            GameSettings.small_exit_button.place(x=1250, y=706)
            pygame.mixer.music.load('End_OST.mp3')
            pygame.mixer.music.play(-1)
            GameSettings.mob_hp_bar.place_forget()
            GameSettings.hero_hp_bar.place_forget()
            my_label2 = Label(root, bg='gray')  # , bd=6, relief='raised')
            my_label2.place(x=0, y=0)
            player2 = tkvideo.tkvideo("../Учеба/Death.mp4", my_label2, loop=0, size=(1200, 700))
            player2.play()
            Achivement_1['text'] = 'ОТВЕТИТЬ ПРАВИЛЬНО НА ВСЕ ВОПРОСЫ: ПРОВАЛ'
            Achivement_2['text'] = 'УБИТЬ ВСЕХ ОБЫЧНЫХ СКЕЛЕТОВ: ПРОВАЛ'
            Achivement_3['text'] = 'УБИТЬ БОССА: УСПЕХ'
            if GameSettings.right_answers > 10:
                Achivement_1['text'] = 'ОТВЕТИТЬ ПРАВИЛЬНО НА ВСЕ ВОПРОСЫ: УСПЕХ'
            if GameSettings.frags > 14:
                Achivement_2['text'] = 'УБИТЬ ВСЕХ ОБЫЧНЫХ СКЕЛЕТОВ: УСПЕХ'
            Achivement_1.place(x=1250, y=106)
            Achivement_2.place(x=1250, y=206)
            Achivement_3.place(x=1250, y=306)
            Achivement_4.place(x=1250, y=406)

        else:
            GameSettings.frags += 1
            GameSettings.lvl += 1
            for i in range(len(GameSettings.hits_min)):
                GameSettings.hits_min[i] = int(GameSettings.hits_min[i] * ((3 / GameSettings.hits_min[i]) + 1))
                GameSettings.hits_max[i] = int(GameSettings.hits_max[i] * ((3 / GameSettings.hits_max[i]) + 1))
            Journal['text'] = 'Скелет погиб. Урон повышен'
            Enemy_Journal.place_forget()
            GameSettings.fighting_label['image'] = Fighting
            GameSettings.menu_moderator = 0
            GameSettings.fighting_label.place_forget()
            First_Fighting_Button.place_forget()
            Second_Fighting_Button.place_forget()
            Third_Fighting_Button.place_forget()
            Forth_Fighting_Button.place_forget()
            Fifth_Fighting_Button.place_forget()
            Sixth_Fighting_Button.place_forget()
            Seventh_Fighting_Button.place_forget()
            GameSettings.mob_hp_bar.place_forget()
            GameSettings.hero_hp_bar.place_forget()
            GameSettings.field[GameSettings.reserve_i][GameSettings.reserve_j] = 0
            GameSettings.buttons_Map[GameSettings.reserve_i][GameSettings.reserve_j].configure(
                image=GameSettings.pictures[0])


# выбор атаки
def fight():
    Journal['fg'] = '#47402c'
    Journal['text'] = 'Бой начался'
    Enemy_Journal['text'] = 'Ход атак противника'
    Enemy_Journal.place(x=770, y=725)
    GameSettings.blindness = 1
    GameSettings.unstable = 1
    GameSettings.disarmed = 1
    First_Fighting_Button['text'] = 'Мощная ' + str(100 - GameSettings.chances[0]) + '%'
    Second_Fighting_Button['text'] = 'Обычная ' + str(100 - GameSettings.chances[1]) + '%'
    Third_Fighting_Button['text'] = 'Быстрая ' + str(100 - GameSettings.chances[2]) + '%'
    Fifth_Fighting_Button['text'] = 'Ослепить ' + str(100 - GameSettings.chances[3]) + '%'
    Sixth_Fighting_Button['text'] = 'Обезоружить ' + str(100 - GameSettings.chances[4]) + '%'
    Seventh_Fighting_Button['text'] = 'Обездвижить ' + str(100 - GameSettings.chances[5]) + '%'
    if GameSettings.hero_hp > 30:
        GameSettings.hero_hp_bar['fg'] = '#292929'
    GameSettings.fighting_label.place(x=0, y=0)
    GameSettings.menu_moderator = 1
    First_Fighting_Button.place(x=1268, y=20)
    Second_Fighting_Button.place(x=1268, y=120)
    Third_Fighting_Button.place(x=1268, y=220)
    Fifth_Fighting_Button['state'] = 'normal'
    Sixth_Fighting_Button['state'] = 'normal'
    Seventh_Fighting_Button['state'] = 'normal'
    GameSettings.mob_hp = GameSettings.mob_hp_const
    GameSettings.mob_hp_bar['text'] = GameSettings.mob_hp
    GameSettings.hero_hp_bar['text'] = GameSettings.hero_hp
    GameSettings.mob_hp_bar.place(x=720, y=100)
    GameSettings.hero_hp_bar.place(x=320, y=100)


# нажатие стрелки на клавиатуре
def move(event):
    for i in range(GameSettings.line):
        for j in range(GameSettings.column):
            if GameSettings.field[j][i] == 2 or GameSettings.field[j][i] == 7:
                x = j
                y = i
    if GameSettings.release_moderator + GameSettings.menu_moderator + GameSettings.boss_moderator == 0:

        if event.keysym == 'Right':
            if GameSettings.coordinates_lock == 0:
                GameSettings.reserve_i = x + 1
                GameSettings.reserve_j = y
            if GameSettings.field[x + 1][y] != 1 and GameSettings.buttons_Map[x + 1][y]['state'] == 'normal':
                if GameSettings.field[x + 1][y] == 3:
                    options()
                    GameSettings.field[x + 1][y] = 2
                    GameSettings.buttons_Map[x][y].configure(image=GameSettings.pictures[0])
                    GameSettings.buttons_Map[x + 1][y].configure(image=GameSettings.pictures[2])
                elif GameSettings.field[x + 1][y] == 4:
                    change_location()
                elif GameSettings.field[x + 1][y] == 5:
                    boss()
                elif GameSettings.field[x + 1][y] == 9:
                    fight()
                else:
                    GameSettings.field[x][y] = 0
                    GameSettings.field[x + 1][y] = 2
                    GameSettings.buttons_Map[x][y].configure(image=GameSettings.pictures[0])
                    GameSettings.buttons_Map[x + 1][y].configure(image=GameSettings.pictures[2])
            GameSettings.release_moderator = 1

        if event.keysym == 'Left':
            if GameSettings.coordinates_lock == 0:
                GameSettings.reserve_i = x - 1
                GameSettings.reserve_j = y
            if GameSettings.field[x - 1][y] != 1 and GameSettings.buttons_Map[x - 1][y]['state'] == 'normal':
                if GameSettings.field[x - 1][y] == 3:
                    options()
                    GameSettings.field[x][y] = 0
                    GameSettings.field[x - 1][y] = 2
                    GameSettings.buttons_Map[x][y].configure(image=GameSettings.pictures[0])
                    GameSettings.buttons_Map[x - 1][y].configure(image=GameSettings.pictures[6])
                elif GameSettings.field[x - 1][y] == 4:
                    change_location()
                elif GameSettings.field[x - 1][y] == 5:
                    boss()
                elif GameSettings.field[x - 1][y] == 9:
                    fight()
                else:
                    GameSettings.field[x][y] = 0
                    GameSettings.field[x - 1][y] = 2
                    GameSettings.buttons_Map[x][y].configure(image=GameSettings.pictures[0])
                    GameSettings.buttons_Map[x - 1][y].configure(image=GameSettings.pictures[6])
            GameSettings.release_moderator = 1

        if event.keysym == 'Down':
            if GameSettings.coordinates_lock == 0:
                GameSettings.reserve_i = x
                GameSettings.reserve_j = y + 1
            if GameSettings.field[x][y + 1] != 1 and GameSettings.buttons_Map[x][y + 1]['state'] == 'normal':
                if GameSettings.field[x][y + 1] == 3:
                    options()
                    GameSettings.field[x][y] = 0
                    GameSettings.field[x][y + 1] = 2
                    GameSettings.buttons_Map[x][y].configure(image=GameSettings.pictures[0])
                    GameSettings.buttons_Map[x][y + 1].configure(image=GameSettings.pictures[8])
                elif GameSettings.field[x][y + 1] == 4:
                    change_location()
                elif GameSettings.field[x][y + 1] == 5:
                    boss()
                elif GameSettings.field[x][y + 1] == 9:
                    fight()
                else:
                    GameSettings.field[x][y] = 0
                    GameSettings.field[x][y + 1] = 2
                    GameSettings.buttons_Map[x][y].configure(image=GameSettings.pictures[0])
                    GameSettings.buttons_Map[x][y + 1].configure(image=GameSettings.pictures[8])
            GameSettings.release_moderator = 1

        if event.keysym == 'Up':
            if GameSettings.coordinates_lock == 0:
                GameSettings.reserve_i = x
                GameSettings.reserve_j = y - 1
            if GameSettings.field[x][y - 1] != 1 and GameSettings.buttons_Map[x][y - 1]['state'] == 'normal':
                if GameSettings.field[x][y - 1] == 3:
                    options()
                    GameSettings.field[x][y] = 0
                    GameSettings.field[x][y - 1] = 2
                    GameSettings.buttons_Map[x][y].configure(image=GameSettings.pictures[0])
                    GameSettings.buttons_Map[x][y - 1].configure(image=GameSettings.pictures[7])
                elif GameSettings.field[x][y - 1] == 4:
                    change_location()
                elif GameSettings.field[x][y - 1] == 5:
                    boss()
                elif GameSettings.field[x][y - 1] == 9:
                    fight()
                else:
                    GameSettings.field[x][y] = 0
                    GameSettings.field[x][y - 1] = 2
                    GameSettings.buttons_Map[x][y].configure(image=GameSettings.pictures[0])
                    GameSettings.buttons_Map[x][y - 1].configure(image=GameSettings.pictures[7])
            GameSettings.release_moderator = 1


def release(event):
    GameSettings.release_moderator = 0


# начало игры
def start_game_fun():
    GameSettings.m_clicked = True
    menu_hide()
    GameSettings.game_start = True
    GameSettings.menu_moderator = 0
    if GameSettings.music:
        pygame.mixer.music.load('OST1.mp3')
        pygame.mixer.music.play(-1)
        filemenu.add_command(label="Меню", command=exit_to_menu)
    GameSettings.music = False
    output(GameSettings.column, GameSettings.line)


# начать заново
def restart():
    destroying()
    change_location()
    create()
    GameSettings.menu_moderator = 0


# настройка звука
def settings_game_fun():
    GameSettings.help_or_settings = False
    menu_hide()
    GameSettings.volume_game_button_0.place(x=540, y=200)
    GameSettings.volume_game_button_0_25.place(x=633, y=200)
    GameSettings.volume_game_button_0_5.place(x=726, y=200)
    GameSettings.volume_game_button_0_75.place(x=819, y=200)
    GameSettings.volume_game_button_1.place(x=912, y=200)
    GameSettings.back_game_button.place(x=540, y=400)
    GameSettings.volume_game_label.place(x=545, y=130)
    GameSettings.release_moderator = 0


# руководство игры
def start_help_fun():
    GameSettings.help_or_settings = False
    menu_hide()
    GameSettings.label_help.place(x=120, y=30)
    GameSettings.label_help3.place(x=1010, y=30)
    GameSettings.label_help2.place(x=540, y=30)
    GameSettings.back_game_button.place(x=540, y=650)


# раздел разработчиков
def start_about_fun():
    GameSettings.help_or_settings = False
    menu_hide()
    GameSettings.label_about.place(x=120, y=30)
    GameSettings.back_game_button.place(x=540, y=650)


# установка громкости
def volume_game_fun(v):
    GameSettings.volume = v
    pygame.mixer.music.set_volume(GameSettings.volume)


# нажатие назад
def back_game_fun():
    if not GameSettings.help_or_settings or not GameSettings.game_start:
        GameSettings.help_or_settings = True

        GameSettings.volume_game_button_0.place_forget()
        GameSettings.volume_game_button_0_25.place_forget()
        GameSettings.volume_game_button_0_5.place_forget()
        GameSettings.volume_game_button_0_75.place_forget()
        GameSettings.volume_game_button_1.place_forget()
        GameSettings.back_game_button.place_forget()
        GameSettings.volume_game_label.place_forget()
        GameSettings.label_help.place_forget()
        GameSettings.label_help2.place_forget()
        GameSettings.label_help3.place_forget()
        GameSettings.label_about.place_forget()

        menu_output()
    else:
        menu_hide()
        GameSettings.m_clicked = True
        GameSettings.menu_moderator = 0


# выод главного меню
def menu_output():
    GameSettings.start_game_button.place(x=540, y=100)
    GameSettings.settings_game_button.place(x=540, y=200)
    GameSettings.help_game_button.place(x=540, y=300)
    GameSettings.about.place(x=540, y=400)
    GameSettings.exit_game_button.place(x=540, y=500)


# скрытие главного меню
def menu_hide():
    GameSettings.start_game_button.place_forget()
    GameSettings.again_game_button.place_forget()
    GameSettings.settings_game_button.place_forget()
    GameSettings.help_game_button.place_forget()
    GameSettings.about.place_forget()
    GameSettings.exit_game_button.place_forget()


# закрытие заставки
def opening_hide():
    pygame.mixer.music.load('Gates.mp3')
    pygame.mixer.music.play(-1)

    my_label.pack_forget()
    GameSettings.opening_close.place_forget()
    menu_output()


# выход в меню
def exit_to_menu():
    if GameSettings.help_or_settings and GameSettings.game_start:
        if GameSettings.m_clicked:
            GameSettings.start_game_button['image'] = Return
            menu_output()
            GameSettings.menu_moderator = 1
            GameSettings.m_clicked = False
        else:
            start_game_fun()


Label_Question = Label(root, bg='#f1d78d', font='Times 15', bd=3, relief='raised',
                       fg='#47402c', text="", wraplength=242)
Label_Boss = Label(root, bg='#f1d78d', font='Times 15', bd=3, relief='raised',
                   fg='#47402c', text="", wraplength=242)
Label_Character = Label(root, bg='#3c3c3c', image=Guts)
Label_Journal = Label(root, bg='#3c3c3c', image=Journal_Bg)
Label_Comments = Label(root, bg='#f1d78d', font='Times 15', fg='#47402c', text=Comments[GameSettings.comment_number],
                       bd=3, relief='raised', wraplength=1000)
Journal = Label(root, bg='#f1d78d', font='Times 15', fg='#47402c', text='Ход игры')
Enemy_Journal = Label(root, bg='lightgray', font='Times 15', fg='#47402c', text='Ход атак противника')
Comrade_Label = Label(root, bd=0, image=Comrade)
Boss_Label = Label(root, bd=0, image=Skeleton)

Achivement_1 = Label(root, bg='#f1d78d', font='Times 15', bd=3, relief='raised',
                     fg='#47402c', text="", wraplength=242)
Achivement_2 = Label(root, bg='#f1d78d', font='Times 15', bd=3, relief='raised',
                     fg='#47402c', text="", wraplength=242)
Achivement_3 = Label(root, bg='#f1d78d', font='Times 15', bd=3, relief='raised',
                     fg='#47402c', text="", wraplength=242)
Achivement_4 = Label(root, bg='#f1d78d', font='Times 15', bd=3, relief='raised',
                     fg='#47402c', text='ПОБЕСЕДОВАТЬ ПЕРЕД БИТВОЙ: ПРОВАЛ', wraplength=242)
First_Boss_Button = Button(root, text='', bd=6, height=1, bg='#a3863e', font='Times 13', fg='black',
                           width=25, relief='raised', activebackground='#f1d78d',
                           command=lambda num=1: boss_answer(num))
Second_Boss_Button = Button(root, text='', bd=6, height=1, bg='#a3863e', font='Times 13', fg='black',
                            width=25, relief='raised', activebackground='#f1d78d',
                            command=lambda num=2: boss_answer(num))
First_Answer_Button = Button(root, text='', bd=6, height=1, bg='#a3863e', font='Times 13', fg='black',
                             width=25, relief='raised', activebackground='#f1d78d',
                             command=lambda num=1: checking_the_answer(num))
Second_Answer_Button = Button(root, text='', bd=6, height=1, bg='#a3863e', font='Times 13', fg='black',
                              width=25, relief='raised', activebackground='#f1d78d',
                              command=lambda num=2: checking_the_answer(num))
Third_Answer_Button = Button(root, text='', bd=6, height=1, bg='#a3863e', font='Times 13', fg='black',
                             width=25, relief='raised', activebackground='#f1d78d',
                             command=lambda num=3: checking_the_answer(num))

First_Fighting_Button = Button(root, bd=6, height=2, bg='#a3863e', font='Times 13',
                               fg='black', width=15, wraplength=120,
                               relief='raised', activebackground='#f1d78d',
                               command=lambda num=0: attack(num))
Second_Fighting_Button = Button(root, bd=6, height=2, bg='#a3863e', font='Times 13',
                                fg='black', width=15, wraplength=150,
                                relief='raised', activebackground='#f1d78d',
                                command=lambda num=1: attack(num))
Third_Fighting_Button = Button(root, bd=6, height=2, bg='#a3863e', font='Times 13',
                               fg='black', width=15, wraplength=120,
                               relief='raised', activebackground='#f1d78d',
                               command=lambda num=2: attack(num))
Forth_Fighting_Button = Button(root, text='Атаковать', bd=6, height=2, bg='#a35b3e', font='Times 13', fg='black',
                               width=15, wraplength=120,  # state='disabled',
                               relief='raised', activebackground='#f1d78d',
                               command=lambda num=4: attack(num))
Fifth_Fighting_Button = Button(root, text='Ослепить', bd=6, height=2, bg='#a35b3e', font='Times 13', fg='black',
                               width=15, wraplength=120,  # state='disabled',
                               relief='raised', activebackground='#f1d78d',
                               command=lambda num=5: attack(num))
Sixth_Fighting_Button = Button(root, text='Обезоружить', bd=6, height=2, bg='#a35b3e', font='Times 13', fg='black',
                               width=15, wraplength=120,  # state='disabled',
                               relief='raised', activebackground='#f1d78d',
                               command=lambda num=6: attack(num))
Seventh_Fighting_Button = Button(root, text='Обездвижить', bd=6, height=2, bg='#a35b3e', font='Times 13', fg='black',
                                 width=15, wraplength=120,  # state='disabled',
                                 relief='raised', activebackground='#f1d78d',
                                 command=lambda num=7: attack(num))

Fighting_Buttons = [Fifth_Fighting_Button, Sixth_Fighting_Button, Seventh_Fighting_Button]


# очистка интерфейса
def destroying():
    GameSettings.menu_window.destroy()
    GameSettings.start_game_button.destroy()
    GameSettings.settings_game_button.destroy()
    GameSettings.volume_game_button_0.destroy()
    GameSettings.volume_game_button_0_25.destroy()
    GameSettings.volume_game_button_0_5.destroy()
    GameSettings.volume_game_button_0_75.destroy()
    GameSettings.volume_game_button_1.destroy()
    GameSettings.volume_game_label.destroy()
    GameSettings.back_game_button.destroy()
    GameSettings.help_game_button.destroy()
    GameSettings.exit_game_button.destroy()
    GameSettings.label_help.destroy()
    GameSettings.label_help2.destroy()
    GameSettings.label_help3.destroy()
    GameSettings.label_about.destroy()
    GameSettings.about.destroy()
    GameSettings.fighting_label.destroy()
    GameSettings.mob_hp_bar.destroy()
    GameSettings.hero_hp_bar.destroy()
    GameSettings.defeat_l.destroy()
    GameSettings.again_game_button.destroy()
    GameSettings.opening_close.destroy()


# Создание и настройка виджетов и окон игры
def create():
    GameSettings.fighting_label = Label(root, image=Fighting, bg='gray')

    GameSettings.mob_hp_bar = Label(root, bg='#f1d78d', bd=3, relief='raised',
                                    text=str(GameSettings.mob_hp), font='Book 30', fg='#292929', width=10)
    GameSettings.hero_hp_bar = Label(root, bg='#f1d78d', bd=3, relief='raised',
                                     text=str(GameSettings.hero_hp), font='Book 30', fg='#292929', width=10)
    GameSettings.defeat_l = Label(root, bg='#f1d78d', bd=3, relief='raised',
                                  text='Герой погиб', font='Book 30', fg='#292929', width=10)

    GameSettings.menu_window = Label(root, bd=0, image=Menu_Background)
    GameSettings.start_game_button = Button(root, image=Start, bd=6, relief='raised',
                                            bg='#f1d78d', activebackground='#6e6240', command=start_game_fun)
    GameSettings.again_game_button = Button(root, image=Again, bd=6, relief='raised',
                                            bg='#f1d78d', activebackground='gray72', command=restart)
    GameSettings.label_help = Label(root, bg='white', image=Help_Page)
    GameSettings.label_help2 = Label(root, bg='white', image=Help_Page2)
    GameSettings.label_help3 = Label(root, bg='white', image=Help_Page3)
    GameSettings.label_about = Label(root, bg='white', image=About_Img)

    GameSettings.settings_game_button = Button(root, image=Settings, bd=6, relief='raised',
                                               bg='#f1d78d', activebackground='gray72', command=settings_game_fun)

    # Звук
    GameSettings.volume_game_button_0 = Button(root, bg='#a3863e', text='0', font='Times 30', fg='#292929',
                                               bd=6, relief='raised', width=3, height=1,
                                               activebackground='gray72', command=lambda v=0: volume_game_fun(v))
    GameSettings.volume_game_button_0_25 = Button(root, bg='#a3863e', text='0.25', font='Times 30', fg='#292929',
                                                  bd=6, relief='raised', width=3, height=1,
                                                  activebackground='gray72', command=lambda v=0.25: volume_game_fun(v))
    GameSettings.volume_game_button_0_5 = Button(root, bg='#a3863e', text='0.5', font='Times 30', fg='#292929',
                                                 bd=6, relief='raised', width=3, height=1,
                                                 activebackground='gray72', command=lambda v=0.5: volume_game_fun(v))
    GameSettings.volume_game_button_0_75 = Button(root, bg='#a3863e', text='0.75', font='Times 30', fg='#292929',
                                                  bd=6, relief='raised', width=3, height=1,
                                                  activebackground='gray72', command=lambda v=0.75: volume_game_fun(v))
    GameSettings.volume_game_button_1 = Button(root, bg='#a3863e', text='1', font='Times 30', fg='#292929',
                                               bd=6, relief='raised', width=3, height=1,
                                               activebackground='gray72', command=lambda v=1: volume_game_fun(v))

    GameSettings.volume_game_label = Label(root, bg='#f1d78d', bd=3, relief='raised',
                                           text='Громкость музыки', font='Book 30', fg='#292929', width=19)

    GameSettings.back_game_button = Button(root, image=Back, bd=6, relief='raised',
                                           bg='#f1d78d', activebackground='gray72', command=back_game_fun)

    GameSettings.help_game_button = Button(root, image=Help, bd=6, relief='raised',
                                           bg='#f1d78d', activebackground='gray72', command=start_help_fun)
    GameSettings.about = Button(root, image=About_Lbl, bd=6, relief='raised',
                                bg='#f1d78d', activebackground='gray72', command=start_about_fun)
    GameSettings.exit_game_button = Button(root, image=Exit, bd=6, relief='raised',
                                           bg='#f1d78d', activebackground='gray72', command=v_click)
    GameSettings.small_exit_button = Button(root, image=Small_Exit, bd=3, relief='raised',
                                            bg='#f1d78d', activebackground='gray72', command=v_click)
    GameSettings.opening_close = Button(root, image=Close, bd=6, relief='raised',
                                        bg='#f1d78d', activebackground='gray72', command=opening_hide)


create()

Upper_Main_Menu.add_cascade(label="Игра", menu=filemenu)


# Скрытие кнопок в игровом поле
def hide(n, m):
    for i in range(n):
        for j in range(m):
            if GameSettings.field[i][j] != 1:
                GameSettings.buttons_Map[i][j].place_forget()


# отображение игрового поля
def output(n, m):
    Background_Label.place(x=0, y=0)
    # Label_Comments.place(x=100, y=720)
    Label_Journal.place(x=250, y=710)
    Journal.place(x=350, y=725)
    # Label_Character.place(x=15, y=706)
    for i in range(n):
        for j in range(m):
            if GameSettings.field[i][j] == 2:
                i1 = i
                j1 = j
    for i in range(n):
        for j in range(m):
            if GameSettings.field[i][j] != 1:
                btn = GameSettings.buttons_Map[i][j]
                btn.place(x=1.2 * Height * i, y=1.2 * Height * j)


pygame.mixer.music.load('Lilium.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(GameSettings.volume)

my_label = Label(root, bg='#a3863e', bd=6, relief='raised')
my_label.pack()
player = tkvideo.tkvideo("Заставка.mp4", my_label, loop=0, size=(1100, 600))
player.play()

GameSettings.opening_close.place(x=540, y=650)

root.bind('<KeyPress>', move)
root.bind('<KeyRelease>', release)
root.bind('m', lambda e: exit_to_menu())

root.bind('<Escape>', lambda e: back_game_fun())

root.mainloop()
pygame.quit()
