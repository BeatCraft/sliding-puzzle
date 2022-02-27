#! /usr/bin/python
# -*- coding: utf-8 -*-
#
import os, sys, time, math
import random
import csv
import uuid

import tkinter as tk

sys.setrecursionlimit(10000)

def csv_to_list(path):
    print("csv_to_list(%s)" % (path))
    data_list = []
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row)
                f = row[0]
                e = row[1]
                j = row[2]
                if int(row[0])>0:
                    data_list.append([e, j])
                #
            #
        #
    except Exception as e:
        print("error: %s" % e)
    #
    return data_list

def find_word(data_list, word):
    size = len(data_list)
    for i in range(size):
        if word==data_list[i][0]:
            return i
        #
    #
    return -1

class Label():
    def __init__(self, parent):
        self.parent = parent
        self.width = 90
        self.height = 90
        self.offset_x = 0
        self.offset_y = 0
        self.tag = str(uuid.uuid4())
        self.name = ""
        self.text = ""
        self.color_mode = 0 # gray, yellow, green
    
    def getRect(self):
        lelf_top = (self.offset_x, self.offset_y)
        right_bottom = (self.offset_x+self.width, self.offset_y+self.height)
        return lelf_top, right_bottom
    
    def setColorMode(self, mode):
        self.color_mode = mode
        
    def setText(self, text):
        self.text = text
    
    def getText(self):
        return self.text
    
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name
    
    def setPosition(self, x, y):
        self.offset_x = x
        self.offset_y = y
    
    def show(self):
        if self.color_mode==0:
            self.parent.create_rectangle(self.offset_x, self.offset_y, self.offset_x+self.width , self.offset_y+self.height, tag=self.tag)
        elif self.color_mode==1:
            self.parent.create_rectangle(self.offset_x, self.offset_y, self.offset_x+self.width , self.offset_y+self.height, tag=self.tag, fill="yellow")
        elif self.color_mode==2:
            self.parent.create_rectangle(self.offset_x, self.offset_y, self.offset_x+self.width , self.offset_y+self.height, tag=self.tag, fill="green")
        #
        elif self.color_mode==3:
            self.parent.create_rectangle(self.offset_x, self.offset_y, self.offset_x+self.width , self.offset_y+self.height, tag=self.tag, fill="red")
        #
        
        if self.text!="":
            center_x = self.offset_x + self.width/2
            center_y = self.offset_y + self.height/2
            self.parent.create_text(center_x, center_y, text=self.text, anchor="center", font=("",30), tag=self.tag)
        #
    
    def hide(self):
        self.parent.delete(self.tag)
        
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("320x320")
        self.title("Sliding Puzzle")
        self.widget_list = []
        #self.num = 0
        #
        #self.word_list = csv_to_list("./words2.csv")
        #self.answer_index = random.randrange(len(self.word_list))
        #self.answer = self.word_list[self.answer_index][0]
        #self.dump_answer()
    
    def findWidgetByText(self, text):
        for w in self.widget_list:
            if text==w.getText():
                return w
            #
        #
        return None
    
    def findWidget(self, name):
        for w in self.widget_list:
            if name==w.getName():
                return w
            #
        #
        return None
        
    def findWidget(self, x, y):
        for w in self.widget_list:
            lt, rb = w.getRect()
            #print(lt)
            if lt[0]<x and x<rb[0]:
                if lt[1]<y and y<rb[1]:
                    return w
                #
            #
        #
        return None
    
    def addWidget(self, w):
        self.widget_list.append(w)
        
    def prepare(self):
        self.canvas = tk.Canvas(self, width=320, height=320)
        self.canvas.place(x=0, y=0)
        self.canvas.bind("<Button-1>", self.mouseDown)

        # words
        texts = ["1", "2", "3", "4", "5", "6", "7", "8", ""]
        random.shuffle(texts)
        random.shuffle(texts)
        start_x = 15
        start_y = 15
        gap_x = 100
        gap_y = 100
        num = 0
        for y in range(3):
            for x in range(3):
                sx = start_x + gap_x*x
                sy = start_y + gap_y*y
                a = Label(self.canvas)
                a.setPosition(sx, sy)
                name = "%d-%d" % (x, y)
                a.setName(name)
                a.setText(texts[num])
                #if num<9:
                #    a.setText(str(num))
                #
                self.addWidget(a)
                a.show()
                num = num + 1
            #
        #

        
        
        
        

    def mouseDown(self, e):
        print("App::mouseDown(%d, %d)" % (e.x, e.y))
        
        w = self.findWidget(e.x, e.y)
        if w:
            pass
            #print(w.getName())
        else:
            print("none")
            return
        #
        em = self.findWidgetByText("")
        if em:
            pass
            #print(em.getName())
        else:
            return
        #
        p0 = (int(w.getName()[0]), int(w.getName()[2]))
        p1 = (int(em.getName()[0]), int(em.getName()[2]))
        #print(p0)
        #print(p1)
        t = abs(p1[0]-p0[0]) + abs(p1[1]-p0[1])
        #print(t)
        if t==1: # swap
            #print("swap")
            em.hide()
            em.setText(w.getText())
            #em.setName("k")
            em.show()
            w.hide()
            w.setText("")
            w.show()
        #

    def start(self):
        self.mainloop()


def main():
    argvs = sys.argv
    argc = len(argvs)
    #print(argc)
    
    app = App()
    app.prepare()
    app.start()
    
    return 0
#
#
#
if __name__=='__main__':
    print(">> start")
    sts = main()
    print(">> end")
    print("\007")
    sys.exit(sts)
#
#
#
