from tkinter import *
import pytube
import re

root = Tk()
root.title("downloader")


e = Entry(root, width=50)
e.pack()

def downloadvid(link) :
    print("download function called")
    yt = pytube.YouTube('"' + link + '"')
    stream = yt.streams.first()
    stream.download()

def isValidURL(str):
 
    # Regex to check valid URL
    regex = ("((http|https)://)(www.youtube)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
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
        result="video downloading"
        return True
    else:
        print("non youtube url")
        result="non youtube url"
        return False



myButton = Button(root,text="enter url",command=myClick)
myButton.pack()


root.mainloop()