#! /usr/bin/python
# -*- coding: utf-8 -*-
#
import os, sys, time, math
import random
import csv
import uuid

import tkinter as tk

class Block():
    def __init__(self, parent):
        self.parent = parent
        self.width = 90
        self.height = 90
        self.offset_x = 0
        self.offset_y = 0
        self.tag = str(uuid.uuid4())
        self.name = ""
        self.text = ""
    
    def getRect(self):
        lelf_top = (self.offset_x, self.offset_y)
        right_bottom = (self.offset_x+self.width, self.offset_y+self.height)
        return lelf_top, right_bottom
        
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
        self.parent.create_rectangle(self.offset_x, self.offset_y, self.offset_x+self.width , self.offset_y+self.height, tag=self.tag)
        
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

        # blocks
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
                a = Block(self.canvas)
                a.setPosition(sx, sy)
                name = "%d-%d" % (x, y)
                a.setName(name)
                a.setText(texts[num])
                self.addWidget(a)
                a.show()
                num = num + 1
            #
        #
        
    def mouseDown(self, e):
        print("App::mouseDown(%d, %d)" % (e.x, e.y))
        # clicked block
        clicked_block = self.findWidget(e.x, e.y)
        if clicked_block:
            pass
        else:
            print("none")
            return
        #
    
        # empty block
        empty_block = self.findWidgetByText("")
        if empty_block:
            pass
        else:
            return
        #
        p0 = (int(clicked_block.getName()[0]), int(clicked_block.getName()[2]))
        p1 = (int(empty_block.getName()[0]), int(empty_block.getName()[2]))
        d = abs(p1[0]-p0[0]) + abs(p1[1]-p0[1])
        if d==1: # swap
            empty_block.hide()
            empty_block.setText(clicked_block.getText())
            empty_block.show()
            clicked_block.hide()
            clicked_block.setText("")
            clicked_block.show()
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
