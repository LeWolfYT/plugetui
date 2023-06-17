#plugetui
from pynput.keyboard import Key
import colorama as cl
import requests as r
import cursor as cr
import pynput as pn
import getch as g
import term as t
import math as m
import os
cl.init()
#1. clear the screen
def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")
clear()
#2. set up the window
def resetdisplay(size):
    for i in range(size[1]):
        print(cl.Back.BLUE + " " * size[0], end="\r")
        if not i == size[1]:
            print("\n", end="")
t.pos(0, 0)
def make_window_base(title, type=1):
    clear()
    size = os.get_terminal_size()
    resetdisplay(size)
    #make the top
    #characters we will use:
    #┌─┤├─┐
    #│    │
    #└────┘
    #┼┬┴
    text = " " + title + " "
    t.pos(3, 0)
    
    print(cl.Back.WHITE + cl.Fore.BLACK + "┌" + "─" * m.floor((size[0]-4-len(text))/2) + "┤" + cl.Fore.LIGHTRED_EX + text + cl.Fore.BLACK + "├" + "─" * m.ceil((size[0]-4-len(text))/2) + "┐", end="\r")
    for i in range(4, size[1]-4):
        t.pos(i, 0)
        print(cl.Back.WHITE + "│" + " " * (size[0]-2) + "│", end="\r")
    t.pos(size[1]-4, 0)
    m.floor((size[0]-4-len(text))/2)
    print(cl.Back.WHITE + "└" + "─" * (size[0]-2) + "┘", end="\r")
    t.pos(size[1]-3, 2)
    print(cl.Back.BLACK + " " * (size[0]-1), end="\r")
class ui():
    def __init__(self) -> None:
        self.screen = 0
        self.hoption = 0
        self.all_options = -1
        self.options = [[], [], [], []]
        self.textoptions = [[], [], [], []]
        self.textvalues = [[], [], [], []]
        self.running = False
    def addoption(self, text, x, y, scr, dir, command=None):
        self.options[scr].append([text, x, y, dir["down"], dir["up"], dir["left"], dir["right"], command])
    def renderoptions(self, scr):
        options = self.options[scr]
        for o in range(len(options)):
            t.pos(options[o][2], options[o][1])
            if o != self.hoption:
                t.write(cl.Fore.BLACK + cl.Back.WHITE + options[o][0])
            else:
                t.write(cl.Fore.WHITE + cl.Back.LIGHTRED_EX + options[o][0])
        t.pos(0, 0)
    def exit(self):
        self.ls.stop()
        clear()
        cr.show()
    def main(self):
        self.running = True
        def keyhandler(key):
            if key == Key.down:
                if not self.options[self.screen][self.hoption][3] is None:
                    ho = self.options[self.screen][self.hoption][3]
                    self.hoption = ho if ho > -1 else self.hoption
                    make_window_base("PluGet UI")
                    self.renderoptions(self.screen)
            elif key == Key.up:
                if not self.options[self.screen][self.hoption][4] is None:
                    ho = self.options[self.screen][self.hoption][4]
                    self.hoption = ho if ho > -1 else self.hoption
                    make_window_base("PluGet UI")
                    self.renderoptions(self.screen)
            elif key == Key.left:
                if not self.options[self.screen][self.hoption][5] is None:
                    ho = self.options[self.screen][self.hoption][5]
                    self.hoption = ho if ho > -1 else self.hoption
                    make_window_base("PluGet UI")
                    self.renderoptions(self.screen)
            elif key == Key.right:
                if not self.options[self.screen][self.hoption][6] is None:
                    ho = self.options[self.screen][self.hoption][6]
                    self.hoption = ho if ho > -1 else self.hoption
                    make_window_base("PluGet UI")
                    self.renderoptions(self.screen)
            elif key == Key.enter:
                if not self.options[self.screen][self.hoption][7] is None:
                    self.options[self.screen][self.hoption][7]()
                    make_window_base("PluGet UI")
                    self.renderoptions(self.screen)
            else:
                pass
            t.pos(0, 0)
            t.write(cl.Fore.BLUE + cl.Back.BLUE + "     ")
            t.pos(0, 0)
        cr.hide()
        t.pos(0, 0)
        make_window_base("PluGet UI")
        self.renderoptions(self.screen)
        with pn.keyboard.Listener(on_press=keyhandler) as self.ls:
            try:
                self.ls.join()
            except:
                self.ls.stop()
        
#3. create the base window
size = os.get_terminal_size()

try:
    plui = ui()
    plui.addoption("Search for Mods", 4, 5, 0, {"down": 1, "up": -1, "left": -1, "right": -1})
    plui.addoption("Add an instance", 4, 6, 0, {"down": 2, "up": 0, "left": -1, "right": -1})
    plui.addoption("Remove an instance", 4, 7, 0, {"down": 3, "up": 1, "left": -1, "right": -1})
    plui.addoption("Exit", 4, 8, 0, {"down": 0, "up": 2, "left": -1, "right": -1}, command=plui.exit)
    plui.main()
finally:
    clear()
    cr.show()