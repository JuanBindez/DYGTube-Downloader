# Release: v2.5.3-rc4
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
import time
import urllib3

from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from src.progress_bar_module import progress_bar


class DownloadInit():
    """This class will receive the url to download the video."""
    def __init__(self, link_url_input):
        self.link_url_input = link_url_input

    def download_audio_mp3(self):
        """Here it will be downloaded in MP3"""
        yt = YouTube(self.link_url_input, on_progress_callback = on_progress)
        #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
        ys = yt.streams.get_audio_only()
        ys.download()
        time.sleep(3)
        progress_bar()

        EXTENSION_MP3 = '.mp3'
        EXTENSION_MP4 = '.mp4'

        try:
            time.sleep(3)
            # renames the file with extension .mp4 to .mp3
            os.rename(str(yt.title + EXTENSION_MP4),str(yt.title + EXTENSION_MP3))
            time.sleep(1)
        except FileNotFoundError:
            messagebox.showerror("DYG Downloader", 
                                 "Erro Ao Salvar Com Extensão .mp3!, Fique Tranquilo Basta Mudar o Nome Do A Extensão Manualmente De .mp4 Para .mp3.")
            pass

    def download_video_mp4(self):
        """Here it will be downloaded in MP4 video."""
        yt = YouTube(self.link_url_input, on_progress_callback = on_progress)
        #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
        ys = yt.streams.get_highest_resolution()
        ys.download()
        time.sleep(2)
        progress_bar()


class DownloadList():
    """Here the url of the playlist to be downloaded will be captured."""
    def __init__(self, url_playlist):    
        self.url_playlist = url_playlist

    def download_playlist_mp3(self):
        """Here the download of the playlist will start."""
        try: 
            pl = Playlist(self.url_playlist)
            for video in pl.videos:
                video.streams.get_audio_only().download()
                progress_bar()
            
                EXTENSION_MP3 = '.mp3'
                EXTENSION_MP4 = '.mp4'
                
                time.sleep(2)
                try:
                    time.sleep(2)
                    # renames the file with extension .mp4 to .mp3
                    os.rename(str(pl.title + EXTENSION_MP4),str(pl.title + EXTENSION_MP3))
                    time.sleep(1)
                except FileNotFoundError:
                    print("arquivo não encontrado")                  # usado em testes.
                    pass
                time.sleep(1)
        
        except:
            messagebox.showerror("DYGTube Downloader",
                                 "Algo deu errado! verifique o link da playlist ")
        messagebox.showinfo("DYG Downloader", 
                            "O download da playlist foi concluído com sucesso!")
        messagebox.showerror("DYG Downloader",
                             "Caso seus downloads estiverem como MP4 você terá que mudar para .MP3 manualmente,é só apagar o .mp4 e colocar .mp3.")

    def download_playlist_mp4(self):
        """Here the download of the playlist will start."""
        try:
            pl = Playlist(self.url_playlist)
            for video in pl.videos:
                video.streams.get_lowest_resolution().download()
                progress_bar()
        except:
            messagebox.showerror("DYG Downloader", "Algo deu errado! verifique o link da playlist.")
        messagebox.showinfo("DYG Downloader", "O download da playlist foi concluído com sucesso!")
