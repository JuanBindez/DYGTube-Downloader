# this is part of the DYGtube Downloader project.
#
# Release: v4.1.1
#
# Copyright ©  2022 - 2023  Juan Bindez  <juanbindez780@gmail.com>
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

from pytubefix import YouTube
from pytubefix.cli import on_progress
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from src.views.playlist_download_view import download_playlist
from src.views.mix_view import choice_mix
from src.views.about_view import sobre_software
from src.services.images_service import *
from src.services.debug_service import DebugInfo
from src.services.check_update_service import check_new_version
from src.views.version import *


ERROR_001 = False
ERROR_002 = False
ERROR_003 = False


def source_code_page():
    webbrowser.open("https://github.com/JuanBindez/DYGTube-Downloader")


def check_quality():
    """this function checks the available resolution of a video."""
    link = entrada_de_dados.get()
    if link == "":
        messagebox.showinfo("DYGTube Downloader", "The field is empty, paste a URL and see the available resolutions for the video you want to download.")
    else:
        pass

    try:
        video = YouTube(link)
        resolucoes = [stream.resolution for stream in video.streams if stream.resolution]
        messagebox.showinfo(title="DYGTUbe", message="The resolutions available for the video, " + video.title + ", ".join(resolucoes))
    except Exception as e:
        DebugInfo.info
        DebugInfo.logger_error.error(e, exc_info=True)
    
def download_video():
    """Here the video is downloaded.
      the link variable receives the url.
    """
    link = entrada_de_dados.get()
    if link == "":
        messagebox.showwarning("DYGTube Downloader", "the field is empty!")
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
            messagebox.showinfo("DYG Downloader", "Download Completed")
        else:
            try:
                yt = YouTube(link, on_progress_callback = on_progress)
                ys = yt.streams.get_highest_resolution()
                ys.download(save_path)
                messagebox.showinfo("DYG Downloader", "Download Completed")
                DebugInfo.info
                DebugInfo.logger_info.info("[INFO] (From main.py ) Starting to download video from URL: %s",link)
            except Exception as e:
                global ERROR_001
                ERROR_001 = True
                messagebox.showwarning("DYG Downloader", "Something went wrong!")
                DebugInfo.info
                DebugInfo.bug_tag
                DebugInfo.logger_error.error(e, exc_info=True)
                
            if not ERROR_001:
                messagebox.showinfo("DYG Downloader", "Download Completed")
            else:
                pass

    except KeyError:
            DebugInfo.info
            DebugInfo.bug_tag
            DebugInfo.logger_info.info("(Error from in main.py) Error KeyError found in download video MP4 from URL: %s",link)
            messagebox.showwarning("DYG Downloader", "Unable to download, this is caused by some change on Youtube, try another video.")
            DebugInfo.logger_error.error(KeyError, exc_info=True)
    except Exception as e:
            global ERROR_002
            ERROR_002 = True
            messagebox.showwarning("DYG Downloader", "Something went wrong!")
            DebugInfo.logger_error.error(e, exc_info=True)

  
def download_mp3():
    """This function downloads audio only."""
    link = entrada_de_dados.get()
    if link == "":
        messagebox.showwarning("DYG Downloader", "the field is empty!")
    elif not link == "":
        pass

    save_path = filedialog.askdirectory()

    try:
        yt = YouTube(link, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()
        ys.download(save_path, mp3=True)

        DebugInfo.info
        DebugInfo.logger_info.info("[INFO] (From main) Starting to download audio MP3 from URL: %s",link)
        time.sleep(3)
        
    except Exception as e:
            global ERROR_003
            ERROR_003 = True
            messagebox.showwarning("DYG Downloader", "Something went wrong!")
            DebugInfo.info
            DebugInfo.logger_error.error(e, exc_info=True)
    if not ERROR_003:
        messagebox.showinfo("DYG Downloader", "Download Completed")
    else:
        pass

window = Tk()
window.title("DYGTube Downloader")
window.geometry("530x375")
#window['background'] = '#373636'  
window.resizable(False, False)# False for non-responsive window and True for responsive.
window.attributes('-alpha',9.1)
foto_icon = PhotoImage(data=base64.b64decode(ICON_LOGO))
window.iconphoto(True, foto_icon)

bg = PhotoImage(data=base64.b64decode(BANNER_LOGO))
label = Label(window, image=bg, bd=0)
label.place(x = 0,y = 0)

COLOR_FRAME = '#585757'
COLOR_BUTTON = '#191A1A'
COLOR_LETTER = '#00E9CA'


var_1080p = IntVar()
var_720p = IntVar()
var_480p = IntVar()
var_360p = IntVar()
var_240p = IntVar()
var_144p = IntVar()

ALTURA = 210

check_1080p = Checkbutton(window,
                         text="1080p",
                         bd=0,
                         variable=var_1080p,).place(x=80, y=ALTURA)

check_720p = Checkbutton(window,
                        text="720p",
                        bd=0,
                        variable=var_720p).place(x=149, y=ALTURA)

check_480p = Checkbutton(window,
                        text="480p",
                        bd=0,
                        variable=var_480p).place(x=210, y=ALTURA)

check_360p = Checkbutton(window,
                        text="360p",
                        bd=0,
                        variable=var_360p).place(x=270, y=ALTURA)

check_240p = Checkbutton(window,
                        text="240p",
                        bd=0,
                        variable=var_240p).place(x=330, y=ALTURA)

check_144p = Checkbutton(window,
                        text="144p",
                        bd=0,
                        variable=var_144p).place(x=390, y=ALTURA)


def make_menu(w):
    global the_menu_1
    the_menu_1 = Menu(w, tearoff=0)
    the_menu_1.add_command(label="Paste")
    

def show_menu(e):
    w = e.widget
    the_menu_1.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu_1.tk.call("tk_popup", the_menu_1, e.x_root, e.y_root)

 
button_quality = PhotoImage(data=base64.b64decode(ICON_QUALITY_VIDEO))
botao_mix = Button(window,
                image=button_quality,
                command=check_quality,
                width=16,
                height=17).place(x=498, y=150)

make_menu(window)
entrada_de_dados = Entry(window, width=61)
entrada_de_dados.place(x=8, y=150)
entrada_de_dados.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)


label = Label(window,
                text=VERSION,).place(x=4, y=345)

botao_video = Button(window,
                text="Download MP4",
                font=('Arial'),
                command=download_video,
                width=57,).place(x=0, y=260)

botao_mp3 = Button(window,
                text="Download MP3",
                command=download_mp3,
                font=('Arial'),
                width=57,).place(x=0, y=300)

menu_barra = Menu(window)

menu_arquivo = Menu(menu_barra, tearoff=0)
menu_arquivo.add_command(label="Mix", command=choice_mix, font=('Arial'))
menu_arquivo.add_command(label="Playlist", command=download_playlist, font=('Arial'))
menu_arquivo.add_command(label="Source code", command=source_code_page, font=('Arial'))
menu_arquivo.add_command(label="Help", command=sobre_software, font=('Arial'))

menu_barra.add_cascade(label="Menu", menu=menu_arquivo)
window.config(menu=menu_barra)


if __name__ == "__main__":
  check_new_version(CHECK_VERSION)
  window.mainloop()
