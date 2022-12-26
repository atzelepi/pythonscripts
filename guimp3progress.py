import tkinter as tk
import tkinter.filedialog
import pygame
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.player = pygame.mixer
        self.player.init()
        self.title("MP3 Player")
        self.openFile()
        self.addButtons()
        self.addProgressBar()
        self.update()

    def openFile(self):
        fileName = tk.filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*")])
        if fileName:
            self.player.music.load(fileName)
            self.duration = self.player.Sound(fileName).get_length()

    def addButtons(self):
        self.startButton = tk.Button(self, text="Start", command=self.start)
        self.startButton.pack()
        self.pauseButton = tk.Button(self, text="Pause", command=self.pause)
        self.pauseButton.pack()
        self.stopButton = tk.Button(self, text="Stop", command=self.stop)
        self.stopButton.pack()
        self.resumeButton = tk.Button(self, text="resume", command=self.unpause)
        self.resumeButton.pack()

    def addProgressBar(self):
        self.progress = tk.DoubleVar()
        self.progressBar = ttk.Progressbar(self, variable=self.progress, maximum=self.duration)
        self.progressBar.pack()

    def start(self):
        self.player.music.play()
        self.update()

    def pause(self):
        self.player.music.pause()

    def stop(self):
        self.player.music.stop()
        self.progress.set(0)

    def unpause(self):
        self.player.music.unpause()

    def update(self):
        if self.player.music.get_busy():
            
            self.after(100, self.update)
        self.progress.set(self.player.music.get_pos() / 1000)

if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()