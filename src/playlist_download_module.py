# this is part of the DYGtube Downloader project.
#
# Release: v3.0-rc6
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


from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from src.source import MixDownload, PlaylistDownload


def download_playlist():
    """Here the url of the playlist will be captured and passed to the DownloadList class to download it."""
    def captura_playlist_mp3():
        url = entrada_url_playlist.get()
        if url == "":
            messagebox.showerror("DYGTube Downloader", "the field is empty!")
        elif not url == "":
            pass
        save_path = filedialog.askdirectory()
        messagebox.showinfo("DYG Downloader", "download will start... please wait")
        DP = PlaylistDownload(url, save_path)
        DP.download_playlist_mp3()

    def captura_playlist_mp4():
        url = entrada_url_playlist.get()
        if url == "":
            messagebox.showerror("DYGTube Downloader", "the field is empty!")
        elif not url == "":
            pass
        save_path = filedialog.askdirectory()
        messagebox.showinfo("DYG Downloader", "download will start... please wait")
        DP = PlaylistDownload(url, save_path)
        DP.download_playlist_mp4()

    window = Tk()
    window.title("DYGTube Downloader")
    window.geometry("455x320")
    window.resizable(False, False)
    window.attributes('-alpha',9.1)
    

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
    entrada_url_playlist = Entry(window, width=58)
    entrada_url_playlist.place(x=2, y=100)
    entrada_url_playlist.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

    botao_download = Button(window,
                    text="Download Video",
                    command=captura_playlist_mp4,
                    width=55,).place(x=0, y=200)
    
    botao_download = Button(window,
                    text="Download MP3",
                    command=captura_playlist_mp3,
                    width=55,).place(x=0, y=247)
