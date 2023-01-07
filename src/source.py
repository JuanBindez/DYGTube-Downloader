# Release: v2.4.2-rc2
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
from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class DownloadInit():
    """Esta classe irá receber a url para fazer o download do vídeo."""

    def __init__(self, link_url_input):
        self.link_url_input = link_url_input


    def download_audio_mp3(self):
        """Aqui será feito o download em MP3"""

        yt = YouTube(self.link_url_input, on_progress_callback = on_progress)
        #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
        ys = yt.streams.get_audio_only()
        ys.download()
        time.sleep(3)

        extensao_mp3 = '.mp3'
        extensao_mp4 = '.mp4'

        try:
            # renomeia o arquivo com extensão .mp4 para .mp3
            os.rename(str(yt.title + extensao_mp4),str(yt.title + extensao_mp3))
        except FileNotFoundError:
            messagebox.showerror("DYG Downloader", "Erro Ao Salvar Com Extensão .mp3!, Fique Tranquilo Basta Mudar o Nome Do A Extensão Manualmente De .mp4 Para .mp3.")
            pass


    def download_video_mp4(self):
        """Aqui será feito o download em vídeo MP4."""

        
        yt = YouTube(self.link_url_input, on_progress_callback = on_progress)
        #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
        ys = yt.streams.get_highest_resolution()
        ys.download()
        time.sleep(3)