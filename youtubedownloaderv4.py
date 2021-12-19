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

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)

def downloadvid(link) :
    chunk_size = 1024
    print("download function called")
    yt = pytube.YouTube('"' + link + '"')
    video = yt.streams.get_highest_resolution()
    yt.register_on_progress_callback(on_progress)
    print(f"Fetching \"{video.title}\"..")
    print(f"Fetching successful\n")
    print(f"Information: \n"
          f"File size: {round(video.filesize * 0.000001, 2)} MegaBytes\n"
          f"Highest Resolution: {video.resolution}\n"
          f"Author: {yt.author}")
    print("Views: {:,}\n".format(yt.views))

    print(f"Downloading \"{video.title}\"..")
    video.download()

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