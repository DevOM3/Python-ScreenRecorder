from tkinter import *
from screen_recorder_sdk import screen_recorder as sr


def start():
    sr.enable_dev_log()
    sr.init_resources()
    sr.start_video_recording("Video.mp4", 60, 8000000)


def stop():
    sr.stop_video_recording()
    exit()


root = Tk()
root.geometry("350x50")
root.title("MyVideoRecorder")
root.attributes("-alpha", 0.5)

start = Button(text="Start", bg="red", command=start)
start.pack(side=LEFT, padx=11, fill=X, expand=True)

stop = Button(text="Stop", command=stop)
stop.pack(side=LEFT, padx=11, fill=X, expand=True)

root.mainloop()
