from tkinter import *
import pytube

root = Tk()
root.title("downloader")


e = Entry(root, width=50)
e.pack()

def downloadvid(link) :
    print("download function called")
    yt = pytube.YouTube('"' + link + '"')
    stream = yt.streams.first()
    stream.download()


def myClick() :
    current = e.get()
    print("text entered:",current)
    downloadvid(current)
    print("myclick function trigered")



myButton = Button(root,text="enter url",command=myClick)
myButton.pack()


root.mainloop()