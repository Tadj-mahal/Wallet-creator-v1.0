import pyautogui
import pytesseract
import cv2
import keyboard
import numpy as np
from PIL import Image
import re
from random import choices
from string import ascii_letters, digits


def screen1():#Обычный скриншот
    pyautogui.screenshot('screenshot.png',region=(42, 235 + x, 95, 25))
def screen2_9():#Обычный скриншот
    pyautogui.screenshot('screenshot.png',region=(45, 235 + x, 95, 25))

def screen10_12():#Обычный скриншот
    pyautogui.screenshot('screenshot.png',region=(50, 235 + x, 95, 25))

def screen11():#Обычный скриншот
    pyautogui.screenshot('screenshot.png',region=(47, 235 + x, 95, 25))

def detect():#Считывает слова на экране без лишних символов
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Папка с тессерактом
    custom_config = r"--oem 3 --psm 10"
    text = pytesseract.image_to_string(img, config = custom_config)
    nex_text = re.sub("[^a-z]", "", text)
    #new_text = nex_text.replace("\n", " ")
    return nex_text
def txtcreator():
    filename = ''.join(choices(ascii_letters + digits, k = 10)) + '.txt'
    open('#' + (filename),'a+').close()
    filepa = '#' + (filename) #Путь, куда будут сохранятся текстовики с паролями
    return filepa

while keyboard.is_pressed('esc') == False:
    pathtext = txtcreator()

    pyautogui.click(270, 735)
    pyautogui.hotkey('ctrl', 'shift', 'p')
    pyautogui.sleep(1.5)
    pyautogui.hotkey('win', 'left')
    pyautogui.sleep(1.5)


    pyautogui.click(225, 75)
    pyautogui.write('jaxx.sh')
    pyautogui.press('enter')
    pyautogui.sleep(20)
    pyautogui.click(320, 600)
    pyautogui.sleep(2)
    pyautogui.click(335, 680)
    pyautogui.sleep(20)
    pyautogui.click(340, 475)#Back Up Now
    pyautogui.click(220, 340)# No one's looking
    pyautogui.sleep(0.5)
    pyautogui.click(315, 415) #Start Backup
    pyautogui.sleep(2)

    fp = open(pathtext, 'a+') #чтение и внесение изменений

    # 1st word
    x = 0
    screen1()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())

    # 2nd word
    x = 25
    screen2_9()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    #3rd word
    x = 50
    screen2_9()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    #4th word
    x = 75
    screen2_9()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    pyautogui.click(340,413)

    # 5 word
    x = 0
    screen2_9()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    # 6 word
    x = 25
    screen2_9()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    #7 word
    x = 50
    screen2_9()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    #8 word
    x = 75
    screen2_9()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    pyautogui.click(340,413)

    #9 word
    x = 0
    screen2_9()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    #10 word
    x = 25
    screen10_12()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    #11 word
    x = 50
    screen11()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    #12 word
    x = 75
    screen10_12()
    img = Image.open('screenshot.png')
    fp.write(detect() + " ")
    print(detect())


    pyautogui.click(340,413)


    fp.write("\n")
    fp.close()

    #Если необходимо сменить слова
    print("Do you want to change some words?(y/n)")
    changerword = input()

    while(changerword == "y" or changerword == "Y"):
        with open(pathtext, 'r') as f:
            text = f.read()
            kext = text.split()
            print("Which words?(Number of word 1-12)")
            numword = int(input())
            print("How you want to change word(word)")
            modifiedword = input()
            kext[numword - 1] = modifiedword
            f = open(pathtext, 'w')
            for i in range(12):
                f.write(kext[i] + ' ')
            f.close()

        print("Your .txt now: ")
        with open(pathtext, 'r') as f:
            print(f.read())
        print("Are you need change one more word?")
        changerword = input()


    with open(pathtext, 'r') as f:
        text = f.read()
        kext = text.split()

    x1 = 35
    y1 = 310
    xmov = 600
    ymov = 395

    green = [120, 216, 56] #Цвет выделенного текста

    pyautogui.click(100,500) #координаты свободного участка на странице
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.click(320,700) #координаты поля Подсветить всё
    for i in range(12):
        pyautogui.click(100,705) # координаты поля для ввода
        pyautogui.write(kext[i])
        pyautogui.sleep(2)

        pyautogui.screenshot('screen.png', region = (x1, y1, xmov - x1, ymov - y1))
        im = cv2.imread('screen.png')
        yc,xc = np.where(np.all(im == green, axis = 2))
        print(xc[1], yc[1])
        pyautogui.click(xc[1] + x1,yc[1]+y1)

        pyautogui.click(100,705)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.click(325, 495)
    pyautogui.sleep(5)

    pyautogui.click(655, 700) #Закрыть Найти на странице
    pyautogui.click(320, 335) #Continue
    pyautogui.click(320, 585) #Нажать на Jaxx Liberty Home
    pyautogui.sleep(5)

    pyautogui.click(450, 540) #Клик на эфир
    pyautogui.click(380, 350) #Receive
    pyautogui.click(315, 535) #Скопировать адрес эфира
    pyautogui.sleep(2)

    pyautogui.click(285, 25) # +Вкладка
    pyautogui.click(225, 75) #Ввод рефки
    pyautogui.write('https://etherrock.net/airdrop/9BGL89V/')
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.click(465,25)
    pyautogui.write('https://unixswap.io/C597CF')
    pyautogui.press('enter')
    pyautogui.sleep(4)

    pyautogui.click(105, 295) #Клик на свободное место
    pyautogui.click(670, 225) #Клик на прокрутку
    pyautogui.sleep(2)
    pyautogui.click(240, 340) #Клик на Airdrop
    pyautogui.sleep(1)
    pyautogui.click(70, 280) #Your Eth-Address
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(1)
    pyautogui.click(610, 275) #Claim
    pyautogui.click(430, 30) #Закрыть вкладку

    pyautogui.click(300, 25) #Click $ROCK
    pyautogui.sleep(1)
    pyautogui.doubleClick(670, 700)
    pyautogui.sleep(1)
    pyautogui.click(140, 675)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.sleep(1)
    pyautogui.click(80, 695)
    pyautogui.click(670, 700, 4)
    pyautogui.sleep(1)
    pyautogui.click(520, 625)
    pyautogui.click(650, 10)
