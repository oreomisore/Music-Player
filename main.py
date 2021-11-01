import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvasPadding = 20
canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x400")
canvas.config(bg='floralwhite')
canvas['padx'] = canvasPadding


canvas.columnconfigure(0, weight=1)
canvas.columnconfigure(1, weight=1)
canvas.columnconfigure(2, weight=1)
canvas.columnconfigure(3, weight=1)
canvas.columnconfigure(4, weight=1)
canvas.columnconfigure(5, weight=1)
canvas.columnconfigure(6, weight=1)

canvas.rowconfigure(0, weight=1)
canvas.rowconfigure(1, weight=1)
canvas.rowconfigure(2, weight=1)
canvas.rowconfigure(3, weight=1)
canvas.rowconfigure(4, weight=1)


rootpath = "/Users/oreomisore/Desktop/Music"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file='Previous.png')
next_img = tk.PhotoImage(file='Next.png')
play_img = tk.PhotoImage(file='Play.png')
stop_img = tk.PhotoImage(file='Stop.png')
pause_img = tk.PhotoImage(file='Pause.png')
vol_up_img = tk.PhotoImage(file='VolUp.png')
vol_down_img = tk.PhotoImage(file='VolDown.png')


def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "/" + listBox.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listBox.select_clear('active')


def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "/" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def play_prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text=prev_song_name)

    mixer.music.load(rootpath + "/" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)


def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] == "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] == "Pause"


def vol_up():
    mixer.music.set_volume(min(1.0, mixer.music.get_volume()+0.1))


def vol_down():
    mixer.music.set_volume(max(0.0, mixer.music.get_volume()-0.1))


listBox = tk.Listbox(canvas, fg='black', bg='floralwhite', width=100, font=('poppins', 14))
listBox.grid(row=0, column=0, columnspan=4, sticky='')
listBox.configure(border=2, relief='sunken')


listBoxScroll = tk.Scrollbar(canvas, orient=tk.VERTICAL, command=listBox.yview)
# command - how actions are associated with widgets and UI events.
listBoxScroll.grid(row=0, column=5, sticky='nes')
listBox['yscrollcommand'] = listBoxScroll.set


label = tk.Label(canvas, text=" ", bg='tan', fg='white', font=('poppins', 18))
label.grid(row=1, column=0, columnspan=4, sticky='')

buttonFrame = tk.Frame(canvas, bg='floralwhite')
buttonFrame.grid(row=2, column=0, columnspan=5, sticky='')


prevButton = tk.Button(buttonFrame, text="Prev", image=prev_img, bg='floralwhite', borderwidth=0, command=play_prev)
prevButton.grid(row=2, column=0, sticky="ne")

stopButton = tk.Button(buttonFrame, text="Stop", image=stop_img, bg='floralwhite', borderwidth=0, command=stop)
stopButton.grid(row=2, column=1, sticky="new")

playButton = tk.Button(buttonFrame, text="Play", image=play_img, bg='floralwhite', borderwidth=0, command=select)
playButton.grid(row=2, column=2, sticky="new")

pauseButton = tk.Button(buttonFrame, text="Pause", image=pause_img, bg='floralwhite', borderwidth=0, command=pause_song)
pauseButton.grid(row=2, column=3, sticky="new")

nextButton = tk.Button(buttonFrame, text="Next", image=next_img, bg='floralwhite', borderwidth=0, command=play_next)
nextButton.grid(row=2, column=4, sticky="nw")

volButtonFrame = tk.Frame(canvas, bg="floralwhite")
volButtonFrame.grid(row=3, column=0, columnspan=5, sticky='')

volumeDownButton = tk.Button(volButtonFrame, text="--", image=vol_down_img, bg='floralwhite', borderwidth=0,
                             command=vol_down)
volumeDownButton.grid(row=0, column=1, sticky="nw")

volumeUpButton = tk.Button(volButtonFrame, text="++", image=vol_up_img, bg='floralwhite', borderwidth=0,
                           command=vol_up)
volumeUpButton.grid(row=0, column=2, sticky="nw")




for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)


# # making sure screen does not expand too small or too large
canvas.update()
canvas.minsize(listBox.winfo_width() + listBoxScroll.winfo_width() + label.winfo_width() + volButtonFrame.winfo_width()
               + canvasPadding,label.winfo_height() + listBoxScroll.winfo_height() + buttonFrame.winfo_height() +
               listBox.winfo_height() + volButtonFrame.winfo_height())
canvas.maxsize(listBox.winfo_width() + 50 + listBoxScroll.winfo_width() + 50 + label.winfo_width() + 50 + canvasPadding,
               label.winfo_height() + 50 + listBoxScroll.winfo_height() + 50 + buttonFrame.winfo_height() + 50 +
               listBox.winfo_height() + 50 + volButtonFrame.winfo_height() +50)


canvas.mainloop()
