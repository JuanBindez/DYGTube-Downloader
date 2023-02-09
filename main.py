# Release: v2.6.0-rc2
#
# Copyright (c) 2022-2023  Juan Bindez  <juanbindez780@gmail.com>
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
    
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from src.source import DownloadInit
from src.playlist_download_module import download_playlist
from src.escolha_mix_module import escolha_mix
from src.sobre_module import sobre_software


# Configure the logging system
#logging.basicConfig(filename="DYGTUbe_main.log", level=logging.INFO, format='%(asctime)s %(message)s')
#logger = logging.getLogger()


def download_video():
    """Here the video is downloaded.
      the link variable receives the url.
    """
    link = entrada_de_dados.get()
    #logger.info("(From main)Starting to download video MP4 from URL: %s", link)
    di = DownloadInit(link)
    di.download_video_mp4()
    
  
def download_mp3():
    """This function downloads audio only."""
    link = entrada_de_dados.get()
    #logger.info("(From main)Starting to download audio MP3 from URL: %s", link)
    di = DownloadInit(link)
    di.download_audio_mp3()

"""information:

website to generate colors in hex:  https://www.rapidtables.com/web/color/RGB_Color.html

 y ishei ght and x is for sides.
"""

window = Tk()
window.title("DYGTube Downloader")
window.geometry("500x370")
window['background'] = '#4E4E4E'             
window.resizable(False, False)                       # False for non-responsive window and True for responsive.
window.attributes('-alpha',9.1)
foto_icon = PhotoImage(file = 'logo_icon.png')
window.iconphoto(True, foto_icon)

file_img = Image.open('logo.png')
bg = ImageTk.PhotoImage(file_img)
label = Label(window, image=bg)
label.place(x = 50,y = 60)

COLOR_FRAME = '#585757'
COLOR_BUTTON = '#3D3D3D'
COLOR_LETTER = '#09AF30'

frame = Frame(window, width=600, height=35, bg=COLOR_FRAME)
frame.grid(row=0, column=0)
label = Label(window,
                text="URL*",
                fg=COLOR_LETTER,
                bg="#4E4E4E").place(x=40, y=190)

def make_menu(w):
    global the_menu_1
    the_menu_1 = Menu(w, tearoff=0)
    the_menu_1.add_command(label="Colar")
    
    
def show_menu(e):
    w = e.widget
    the_menu_1.entryconfigure("Colar",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu_1.tk.call("tk_popup", the_menu_1, e.x_root, e.y_root)


make_menu(window)
entrada_de_dados = Entry(window, width=40)
entrada_de_dados.place(x=95, y=190)
entrada_de_dados.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
lbl = Label(window, text = "")

# button that starts the download.
botao = Button(window,
                text="Download Vídeo",
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
                text="Sobre",
                command=sobre_software,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,
                width=3,).place(x=103, y=2)

# button to playlist download.
botao_playlist = Button(window,
                text="playlist",
                command=download_playlist,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,
                width=4,).place(x=45, y=2) 

# mix option button.                     
botao_mix = Button(window,
                text="mix",
                command=escolha_mix,
                fg=COLOR_LETTER,
                bg=COLOR_BUTTON,
                width=2,).place(x=2, y=2)

if __name__ == "__main__":
  window.mainloop()
