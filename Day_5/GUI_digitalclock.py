import tkinter
import time

class Digital_Clock():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(text="")
        self.label.pack()
        self.update_clock()
        self.main_window.mainloop()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.label.configure(text=current_time)
        self.main_window.after(200,self.update_clock)

if __name__ == '__main__':
    digital_clock = Digital_Clock()
