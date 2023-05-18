# this is part of the DYGtube Downloader project.
#
# Release: v2.12.1
#
# Copyright (c) 2022 - 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez


import os
import logging
import urllib3
import time
import base64
import webbrowser

from pytube import YouTube
from pytube.cli import on_progress
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


from src.source import MixDownload
from src.playlist_download_module import download_playlist
from src.mix_module import choice_mix
from src.about_module import sobre_software
from src.channel_module import download_channel
from src.progress_bar_module import progress_bar
from src.images import *
from src.debug import DebugInfo
from src.notify_module import *


ERROR_001 = False
ERROR_002 = False
ERROR_003 = False


def page_web():
    webbrowser.open("https://github.com/JuanBindez/DYGTube-Downloader-v2.12-rc1")
    pass
    

def check_quality():
    """this function checks the available resolution of a video."""

    link = entrada_de_dados.get()
    if link == "":
        messagebox.showinfo("DYG Downloader", "The field is empty, paste a URL and see the available resolutions for the video you want to download.")
    else:
        pass

    try:
        video = YouTube(link)
        resolucoes = [stream.resolution for stream in video.streams if stream.resolution]
        messagebox.showinfo(title="DYGTUbe", message="The resolutions available for the video, " + video.title + ", ".join(resolucoes))
    except Exception as e:
        DebugInfo.info
        DebugInfo.bug_tag
        DebugInfo.logger_error.error(e, exc_info=True)
    
def download_video():
    """Here the video is downloaded.
      the link variable receives the url.
    """

    link = entrada_de_dados.get()
    if link == "":
        messagebox.showerror("DYG Downloader", "the field is empty!")
    elif not link == "":
        pass
    
    save_path = filedialog.askdirectory()
    video = YouTube(link)

    try:
        video_stream = None 

        if var_1080p.get() == 1:
            video_stream = video.streams.filter(res="1080p").first()
        elif var_720p.get() == 1:
            video_stream = video.streams.filter(res="720p").first()
        elif var_480p.get() == 1:
            video_stream = video.streams.filter(res="480p").first()
        elif var_360p.get() == 1:
            video_stream = video.streams.filter(res="360p").first()
        elif var_240p.get() == 1:
            video_stream = video.streams.filter(res="240p").first()
        elif var_144p.get() == 1:
            video_stream = video.streams.filter(res="144p").first()

        if video_stream is not None:
            DebugInfo.info
            DebugInfo.logger_info.info("[INFO] (From main.py ) Starting to download video from URL: %s",link)
            video_stream.download(save_path)
            notify_info()
        else:
            try:
                yt = YouTube(link, on_progress_callback = on_progress)
                ys = yt.streams.get_highest_resolution()
                ys.download(save_path)
                notify_info()
                DebugInfo.info
                DebugInfo.logger_info.info("[INFO] (From main.py ) Starting to download video from URL: %s",link)
            except Exception as e:
                global ERROR_001
                ERROR_001 = True
                messagebox.showerror("DYG Downloader", "Something went wrong!")
                DebugInfo.info
                DebugInfo.bug_tag
                DebugInfo.logger_error.error(e, exc_info=True)
                
            if not ERROR_001:
                notify_info()
            else:
                pass

    except KeyError:
            DebugInfo.info
            DebugInfo.bug_tag
            DebugInfo.logger_info.info("(Error from in main.py) Error KeyError found in download video MP4 from URL: %s",link)
            messagebox.showerror("DYG Downloader", "Unable to download, this is caused by some change on Youtube, try another video.")
            DebugInfo.logger_error.error(KeyError, exc_info=True)
    except Exception as e:
            global ERROR_002
            ERROR_002 = True
            messagebox.showerror("DYG Downloader", "Something went wrong!")
            DebugInfo.info
            DebugInfo.bug_tag
            DebugInfo.logger_error.error(e, exc_info=True)

  
def download_mp3():
    """This function downloads audio only."""

    link = entrada_de_dados.get()
    if link == "":
        messagebox.showerror("DYG Downloader", "the field is empty!")
    elif not link == "":
        pass

    save_path = filedialog.askdirectory()

    try:
        EXTENSION_MP3 = '.mp3'
        EXTENSION_MP4 = '.mp4'

        yt = YouTube(link, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()
        ys.download(save_path)
        downloaded_file_path = os.path.abspath(ys.default_filename)
        new_file_path = os.path.splitext(downloaded_file_path)[0] + EXTENSION_MP3
        os.rename(downloaded_file_path, new_file_path)

        DebugInfo.info
        DebugInfo.logger_info.info("[INFO] (From main) Starting to download audio MP3 from URL: %s",link)
        time.sleep(3)
        
    except Exception as e:
            global ERROR_003
            ERROR_003 = True
            messagebox.showerror("DYG Downloader", "Something went wrong!")
            DebugInfo.info
            DebugInfo.bug_tag
            DebugInfo.logger_error.error(e, exc_info=True)
    if not ERROR_003:
        notify_info()
    else:
        pass


"""
information:

website to generate colors in hex:  https://www.rapidtables.com/web/color/RGB_Color.html
y ishei ght and x is for sides.
"""


window = Tk()
window.title("DYGTube Downloader")
window.geometry("500x370")
window['background'] = '#373636'  
window.resizable(False, False)# False for non-responsive window and True for responsive.
window.attributes('-alpha',9.1)
foto_icon = PhotoImage(data=base64.b64decode(ICON_LOGO))
window.iconphoto(True, foto_icon)

bg = PhotoImage(data=base64.b64decode(BANNER_LOGO))
label = Label(window, image=bg, bd=0)
label.place(x = 220,y = 60)

"""
bg2 = PhotoImage(data=base64.b64decode(GUAXINIM))
label = Label(window, image=bg2)
label.place(x = 7,y = 310)
"""

button_quality = PhotoImage(data=base64.b64decode(ICON_QUALITY_VIDEO))
botao_mix = Button(window,
                image=button_quality,
                command=check_quality,
                width=16,
                height=17).place(x=423, y=170)


COLOR_FRAME = '#585757'
COLOR_BUTTON = '#191A1A'
COLOR_LETTER = '#00E9CA'

frame = Frame(window, width=600, height=35, bg=COLOR_FRAME)
frame.grid(row=0, column=0)
label = Label(window,
                text="URL*",
                fg=COLOR_LETTER,
                bg="#373636").place(x=40, y=170)

def make_menu(w):
    global the_menu_1
    the_menu_1 = Menu(w, tearoff=0)
    the_menu_1.add_command(label="Colar")
    
    
def show_menu(e):
    w = e.widget
    the_menu_1.entryconfigure("Colar",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu_1.tk.call("tk_popup", the_menu_1, e.x_root, e.y_root)


var_1080p = IntVar()
var_720p = IntVar()
var_480p = IntVar()
var_360p = IntVar()
var_240p = IntVar()
var_144p = IntVar()

check_1080p = Checkbutton(window,
                         text="1080p",
                         fg=COLOR_LETTER,
                         bg="#373636",
                         bd=0,
                         variable=var_1080p,)

check_720p = Checkbutton(window,
                        text="720p",
                        fg=COLOR_LETTER,
                        bg="#373636",
                        bd=0,
                        variable=var_720p)

check_480p = Checkbutton(window,
                        text="480p",
                        fg=COLOR_LETTER,
                        bg="#373636",
                        bd=0,
                        variable=var_480p)

check_360p = Checkbutton(window,
                        text="360p",
                        fg=COLOR_LETTER,
                        bg="#373636",
                        bd=0,
                        variable=var_360p)

check_240p = Checkbutton(window,
                        text="240p",
                        fg=COLOR_LETTER,
                        bg="#373636",
                        bd=0,
                        variable=var_240p)

check_144p = Checkbutton(window,
                        text="144p",
                        fg=COLOR_LETTER,
                        bg="#373636",
                        bd=0,
                        variable=var_144p)

check_1080p.place(x=80, y=220)
check_720p.place(x=149, y=220)
check_480p.place(x=210, y=220)
check_360p.place(x=270, y=220)
check_240p.place(x=330, y=220)
check_144p.place(x=390, y=220)

make_menu(window)
entrada_de_dados = Entry(window, width=40)
entrada_de_dados.place(x=95, y=170)
entrada_de_dados.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
lbl = Label(window, text = "")

# version label
label = Label(window,
                text="v2.12.1",
                fg=COLOR_LETTER,
                bg="#373636").place(x=4, y=345)

# button that starts the download.
botao = Button(window,
                text="Download Video",
                command=download_video,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,).place(x=120, y=270)

# button to start downloading only the audio of the video.
botao_mp3 = Button(window,
                text="Download MP3",
                command=download_mp3,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,).place(x=270, y=270)


# button to display information about the program.
botao_sobre = Button(window,
                text="Help",
                command=sobre_software,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,
                width=3,).place(x=165, y=2)

# button to playlist download.
botao_playlist = Button(window,
                text="Playlist",
                command=download_playlist,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,
                width=4,).place(x=104, y=2)

# button to channel download.
botao_channel = Button(window,
                text="Channel",
                command=download_channel,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,
                width=4,).place(x=45, y=2) 

# mix option button.                     
botao_mix = Button(window,
                text="Mix",
                command=choice_mix,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,
                width=2,).place(x=2, y=2)


botao_logo = Button(window,
                text="Github",
                command=page_web,
                fg=COLOR_LETTER,
                bg="#373636",
                bd=0,
                width=2,
                height=1).place(x=450, y=342)


if __name__ == "__main__":
  window.mainloop()
