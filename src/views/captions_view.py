# this is part of the DYGtube Downloader project.
#
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


from pytubefix.cli import on_progress
from pytubefix import YouTube
from pytubefix.exceptions import AgeRestrictedError
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from src.services.debug_service import DebugInfo
from src.core.mix_core import MixDownload
from src.core.playlist_core import PlaylistDownload


def captions_download():
    """Captions."""
    def get_captions():
        yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
        subtitles = yt.captions

        print(subtitles)

        url = entrada_url_captions.get()
        if url == "":
            messagebox.showerror("DYGTube Downloader", "the field is empty!")
        elif not url == "":
            pass
        
        video = YouTube(url)
        print(video.title)
        
        if var_en.get() == 1:
            caption = video.captions.get_by_language_code('en')
            caption.save_captions("captions.txt")
        elif var_720p.get() == 1:
            caption = video.captions.get_by_language_code('pt-BR')
            caption.save_captions("captions.txt")
        elif var_480p.get() == 1:
            caption = video.captions.get_by_language_code('en')
        elif var_360p.get() == 1:
            caption = video.captions.get_by_language_code('en')
        elif var_240p.get() == 1:
            caption = video.captions.get_by_language_code('en')
        elif var_144p.get() == 1:
            caption = video.captions.get_by_language_code('en')


    window = Tk()
    window.title("DYGTube Downloader")
    window.geometry("600x320")
    window.resizable(False, False)
    window.attributes('-alpha',9.1)

    var_en = IntVar()
    var_720p = IntVar()
    var_480p = IntVar()
    var_360p = IntVar()
    var_240p = IntVar()
    var_144p = IntVar()

    ALTURA = 210

    
    check_en = Checkbutton(window,
                            text="en",
                            bd=0,
                            variable=var_en,).place(x=80, y=ALTURA)
    
    check_720p = Checkbutton(window,
                            text="pt-BR",
                            bd=0,
                            variable=var_720p).place(x=149, y=ALTURA)
    
    check_480p = Checkbutton(window,
                            text="es-ES",
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
        global the_menu_2
        the_menu_2 = Menu(w, tearoff=0)
        the_menu_2.add_command(label="Paste")
    

    def show_menu(e):
        w = e.widget
        the_menu_2.entryconfigure("Paste",
        command=lambda: w.event_generate("<<Paste>>"))
        the_menu_2.tk.call("tk_popup", the_menu_2, e.x_root, e.y_root)

    make_menu(window)
    entrada_url_captions = Entry(window, width=70)
    entrada_url_captions.place(x=8, y=100)
    entrada_url_captions.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

    custom_font = ('Arial', 30)
    label = Label(window,
                text="Captions",
                fg='white',
                font=custom_font,).place(x=210, y=40)
    
    botao_download = Button(window,
                    text="Download Captions",
                    font=('Arial'),
                    command=get_captions,
                    width=65,).place(x=0, y=247)
