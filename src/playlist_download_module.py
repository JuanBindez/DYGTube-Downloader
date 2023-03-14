# this is part of the DYGtube Downloader project.
#
# Release: v2.9.0-alpha
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


from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from src.source import DownloadInit, PlaylistDownload


def download_playlist():
    """Here the url of the playlist will be captured and passed to the DownloadList class to download it."""
    def captura_playlist_mp3():
        url = entrada_url_playlist.get()
        DP = PlaylistDownload(url)
        DP.download_playlist_mp3()

    def captura_playlist_mp4():
        url = entrada_url_playlist.get()
        DP = PlaylistDownload(url)
        DP.download_playlist_mp4()

    window = Tk()
    window.title("DYGTube Downloader")
    window.geometry("455x320")
    window['background'] = '#373636'
    window.resizable(False, False)
    window.attributes('-alpha',9.1)
    
    """information:

    website to generate colors in hex:  https://www.rapidtables.com/web/color/RGB_Color.html

    y is height and x is for sides
    """

    def make_menu(w):
      global the_menu_2
      the_menu_2 = Menu(w, tearoff=0)
      the_menu_2.add_command(label="Colar")
      
    def show_menu(e):
        w = e.widget
        the_menu_2.entryconfigure("Colar",
        command=lambda: w.event_generate("<<Paste>>"))
        the_menu_2.tk.call("tk_popup", the_menu_2, e.x_root, e.y_root)

    COLOR_FRAME = '#585757'
    COLOR_BUTTON = '#191A1A'
    LETTER_COLOR = '#00E9CA'

    frame = Frame(window, width=600, height=35, bg=COLOR_FRAME)
    frame.grid(row=0, column=0)
    label = Label(window,
                  text="URL Playlist*",
                  fg='#00E9CA',
                  bg="#373636").place(x=6, y=100)

    make_menu(window)
    entrada_url_playlist = Entry(window, width=40)
    entrada_url_playlist.place(x=95, y=100)
    entrada_url_playlist.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    lbl = Label(window, text = "")

    botao_download = Button(window,
                    text="Download Video",
                    command=captura_playlist_mp4,
                    fg=LETTER_COLOR,
                    bg=COLOR_BUTTON,).place(x=90, y=200)
    
    botao_download = Button(window,
                    text="Download MP3",
                    command=captura_playlist_mp3,
                    fg=LETTER_COLOR,
                    bg=COLOR_BUTTON,).place(x=230, y=200)
