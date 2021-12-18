import tkinter as tk
from tkinter import *
import pytube
import re

root = Tk()
root.title("downloader")
root.geometry("400x100")
from tkinter import messagebox

e = Entry(root, width=50)
e.pack()

def downloadvid(link) :
    print("download function called")
    yt = pytube.YouTube('"' + link + '"')
    stream = yt.streams.first()
    stream.download()

def isValidURL(str):
 
    # Regex to check valid URL
    regex = ("^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.be)\/.+$")
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
def myClick() :
    current = e.get()
    print("text entered:",current)
    validity=isValidURL(current)
    if validity== True:
        downloadvid(current)
        print("myclick function trigered")
        return True
    else:
        print("non youtube url")
        
        #messagebox.showerror('invalid url!')
        msg = Message(root, text = "invalid url") 
        msg.pack()
        return False



myButton = Button(root,text="enter url",command=myClick)
myButton.pack()



root.mainloop()
