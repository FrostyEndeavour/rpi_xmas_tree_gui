from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info, Slider,TextBox, Window, ListBox
from tree import RGBXmasTree
from colorzero import Color
from time import sleep
import random
import keyboard

tree = RGBXmasTree()
y=0

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def brightness():
    tree.brightness = 0
    tree.on()
    tree.brightness = listbox.value

def length():
    n=slider.value

def run_tree():
    #t=0
    #n=t
    n=slider.value
    while 0 < n < 21:
        print("Starting")
        counter = 0
        z=0
        for counter in range(25):
            if z%2 == 0:
                tree[z].color = (0,1,0)
                z += 1
                sleep(y)
            else:
                tree[z].color = (1,0,0)
                z += 1
                sleep(y)
        z=0
        for counter in range(25):
            if z%2 == 0:
                tree[z].color = (1,0,0)
                z += 1
                sleep(y)
            else:
                tree[z].color = (0,1,0)
                z += 1
                sleep(y)
        n -= 1
    else:
        print("Finished.")

def random_tree():
    n=slider.value
    while 0 < n < 21:
        pixel = random.choice(tree)
        pixel.color = random_color()
        n -= 0.025
        sleep(0.01)
    else:
        print("Finished")

def light_show():
    s=0
    while s < 4:
        tree.brightness = 1
        tree.color = (0,1,0)
        sleep(0.15)
        tree.brightness = 0
        sleep(0.225)
        s += 1
    while s < 8:
        tree.brightness = 1
        tree.color = (1,0,0)
        sleep(0.15)
        tree.brightness = 0
        sleep(0.225)
        s += 1
    while s < 11:
        tree.brightness = 1
        tree.color = (0,0,1)
        sleep(0.15)
        tree.brightness = 0
        sleep(0.225)
        s += 1


app = App(title="Tree controller", width=500, height=500,layout="grid")
#window = Window(app)
intro = Text(app, text="Control the XMas Tree!",grid=[1,0],width="fill")
slider = Slider(app, start=0, end=20,grid=[1,2])
text = Text(app,text="Brightness", align="left",grid=[0,1])
text = Text(app,text="Length", align="left", grid=[0,2])
listbox = ListBox(app, items=[0,0.25,0.5,0.75,1], command=brightness,grid=[1,1])
button = PushButton(app, command=run_tree,text="Red & Green",grid=[1,3])
random1 = PushButton(app, command=random_tree, text="Random",grid=[1,4])
lightshow = PushButton(app, command=light_show, text="Light Show",grid=[1,5])


app.display()