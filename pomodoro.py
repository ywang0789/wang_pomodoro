# orz orz orz save me plz

import tkinter  # GUI
from tkinter import messagebox
import time


class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("make_me_productive.exe")

        self.workTime = 1 * 5  # work time
        self.breakTime = 5 * 60  # break time
        self.isBreak = False
        self.isRunning = False

        self.timeRemaining = self.workTime

        # time display--
        self.label = tkinter.Label(
            self.master, text=self.formatTime(self.timeRemaining), font=("Arial", 48)
        )
        self.label.pack(padx=50, pady=50)

        # buttons!!!
        self.start_button = tkinter.Button(
            self.master,
            text="   ▶️   ",
            font=("Segoe UI Emoji", 12),
            command=self.start,
        )
        self.start_button.pack()
        self.stop_button = tkinter.Button(
            self.master, text="   ⏸️   ", font=("Segoe UI Emoji", 12), command=self.stop
        )
        self.stop_button.pack()
        self.quit_button = tkinter.Button(
            self.master,
            text="   ❌   ",
            font=("Segoe UI Emoji", 12),
            command=self.master.quit,
        )
        self.quit_button.pack()

    # format time to 00:00
    def formatTime(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02}:{secs:02}"  # 00:00

    # update teh text displayed
    def updateLabel(self):
        self.label["text"] = self.formatTime(self.timeRemaining)

    # start it!
    def start(self):
        if not self.isRunning:
            self.isRunning = True
            self.startTimer()

    # stop it!
    def stop(self):
        self.isRunning = False

    # start the timer
    def startTimer(self):
        if self.isRunning and self.timeRemaining > 0:
            self.timeRemaining -= 1
            self.updateLabel()
            self.master.after(1000, self.startTimer)
        elif self.isRunning and self.timeRemaining == 0:
            if self.isBreak:
                self.isBreak = False
                self.timeRemaining = self.workTime
                messagebox.showinfo("Info", "GET YO ASS BACK TO WORK!!!")
            else:
                self.isBreak = True
                self.timeRemaining = self.breakTime
                messagebox.showinfo("Info", "Time to BING CHILLIN🍦")
            self.updateLabel()
            self.startTimer()


if __name__ == "__main__":
    main = tkinter.Tk()
    timer = PomodoroTimer(main)
    main.mainloop()
