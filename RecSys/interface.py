import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from PIL import ImageTk, Image
import urllib
import backend
import json
import numpy as np
import pandas as pd
LARGE_FONT= ("Verdana", 12)
ratings_list = []
class RecSys(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        tk.Tk.wm_title(self,'Movie Recommender System')
        container.pack(side="top", fill="both", expand = False)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (StartPage, HomePage, Page2, Page3, FinalPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Movie Recommender System", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Get Started",
                            command=lambda: controller.show_frame(HomePage))
        button.pack()
        button2 = ttk.Button(self, text="Later",
                            command=quit)
        button2.pack()

def on_button(e):
    ratings_list.append(e)

def write_on_file(l):
    fp = open("ratings.txt","w+")
    fp.write(','.join(l))
    fp.close()
    backend.recommend()
    


class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Welcome to the Movie Recommender",font = LARGE_FONT)
        labell = tk.Label(self,text = "Give ratings to the movies according to your taste and get recommedations",font=LARGE_FONT)
        label.grid(row = 0, columnspan = 9,padx=10,pady=10,sticky='ns') 
        labell.grid(row = 1, columnspan = 9,padx=10,pady=10,sticky='ns')
        
        for i in range(1,7):
            img = ImageTk.PhotoImage(Image.open("train/1/"+str(i+2)+".jpeg"))
            label1 = tk.Label(self, image=img)
            label1.image = img
            label1.grid(row = 2,column = 2*(i-1), columnspan = 2,sticky="nw")
            v = StringVar()
            e1 = ttk.Entry(self,textvariable=v)
            b1 = ttk.Button(self,text = "Submit",command=lambda x=v: on_button(x.get()))
            e1.grid(row = 3,column = 2*(i-1), columnspan = 2,sticky="nw")
            b1.grid(row = 4,column = 2*(i-1), columnspan = 2,sticky="n")
        next_button = ttk.Button(self,text = "Next",command=lambda: controller.show_frame(Page2))
        next_button.grid(row=5,column=25,columnspan = 2,sticky="n")

class Page2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Welcome to the Movie Recommender",font = LARGE_FONT)
        labell = tk.Label(self,text = "Give ratings to the movies according to your taste and get recommedations",font=LARGE_FONT)
        label.grid(row = 0, columnspan = 9,padx=10,pady=10,sticky='ns') 
        labell.grid(row = 1, columnspan = 9,padx=10,pady=10,sticky='ns')
        
        for i in range(1,7):
            img = ImageTk.PhotoImage(Image.open("train/2/"+str(i+2)+".jpeg"))
            label1 = tk.Label(self, image=img)
            label1.image = img
            label1.grid(row = 2,column = 2*(i-1), columnspan = 2,sticky="nw")
            v = StringVar()
            e1 = ttk.Entry(self,textvariable=v)
            b1 = ttk.Button(self,text = "Submit",command=lambda x=v: on_button(x.get()))
            e1.grid(row = 3,column = 2*(i-1), columnspan = 2,sticky="nw")
            b1.grid(row = 4,column = 2*(i-1), columnspan = 2,sticky="n")
        next_button = ttk.Button(self,text = "Next",command = lambda: controller.show_frame(Page3))
        next_button.grid(row=5,column=25,columnspan = 2,sticky="n")

class Page3(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Welcome to the Movie Recommender",font = LARGE_FONT)
        labell = tk.Label(self,text = "Give ratings to the movies according to your taste and get recommedations",font=LARGE_FONT)
        label.grid(row = 0, columnspan = 9,padx=10,pady=10,sticky='ns') 
        labell.grid(row = 1, columnspan = 9,padx=10,pady=10,sticky='ns')
        
        for i in range(1,7):
            img = ImageTk.PhotoImage(Image.open("train/3/"+str(i+2)+".jpeg"))
            label1 = tk.Label(self, image=img)
            label1.image = img
            label1.grid(row = 2,column = 2*(i-1), columnspan = 2,sticky="nw")
            v = StringVar()
            e1 = ttk.Entry(self,textvariable=v)
            b1 = ttk.Button(self,text = "Submit",command=lambda x=v: on_button(x.get()))
            e1.grid(row = 3,column = 2*(i-1), columnspan = 2,sticky="nw")
            b1.grid(row = 4,column = 2*(i-1), columnspan = 2,sticky="n")
        save_button = ttk.Button(self,text = "Save Ratings",command =  lambda:write_on_file(ratings_list))
        save_button.grid(row=5,column=20,columnspan = 2,sticky="n")
        next_button = ttk.Button(self,text = "Get Recommedations",command = lambda:controller.show_frame(FinalPage))
        next_button.grid(row=5,column=25,columnspan = 2,sticky="n")

class FinalPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text ="Here are your movie recommendations ",font = LARGE_FONT)
        labell = tk.Label(self,text = "Grab a popcorn, and Enjoy!",font=LARGE_FONT)
        label.grid(row = 0, columnspan = 9,padx=10,pady=10,sticky='ns') 
        labell.grid(row = 1, columnspan = 9,padx=10,pady=10,sticky='ns')
        fq = open("predictions.txt","r+")
        l = fq.read()
        print(l)
        l1 = l.split(",")
        l1[-1] = l1[-1][0]
        print(l1)
        fq.close()
        k = [0 for x in range(18)]
        for i in range(0,5):
            img = ImageTk.PhotoImage(Image.open("recom/"+str(l1[i])+"/"+str(int(k[int(l1[i])])+1)+".jpeg"))
            k[int(l1[i])] = k[int(l1[i])] + 1
            label1 = tk.Label(self, image=img)
            label1.image = img
            label1.grid(row = 2,column = 2*(i), columnspan = 2,sticky="nw",padx=15,pady=15)
            print(k)
        save_button = ttk.Button(self,text = "Quit",command = quit)
        save_button.grid(row=5,column=20,columnspan = 2,sticky="n")

app = RecSys()
app.mainloop()
