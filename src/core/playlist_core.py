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


import os
import time

from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix import Channel
from pytubefix.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

from src.services.debug_service import DebugInfo


ERROR_01 = False
ERROR_02 = False
ERROR_03 = False
ERROR_04 = False
ERROR_05 = False
ERROR_06 = False


class PlaylistDownload():
    """Here the url of the playlist to be downloaded will be captured."""

    def __init__(self, url_playlist, path_to_save):  
        self.url_playlist = url_playlist
        self.path_to_save = path_to_save

    def download_playlist_mp3(self):
        """Here the download of the playlist will start."""

        try:
            pl = Playlist(self.url_playlist)
            for video in pl.videos:
                try:
                    print(video.title)
                    ys = video.streams.get_audio_only()
                    ys.download(self.path_to_save, mp3=True)
                    DebugInfo.info
                    DebugInfo.logger_info.info("[INFO] (From source playlist) Starting to download audio MP3 from URL: %s",self.url_playlist)
                except Exception as e:
                    global ERROR_03
                    ERROR_03 = True
                    DebugInfo.info
                    DebugInfo.logger_error.error(e, exc_info=True)
                    messagebox.showerror("DYGTube Downloader",
                                        "Something went wrong! check playlist link")
                if not ERROR_03:
                    pass

                DebugInfo.info
                DebugInfo.logger_info.info("[INFO] (From source playlist) Starting to download audio MP3 from URL: %s",self.url_playlist)
               
        except FileNotFoundError:
            messagebox.showerror("DYG Downloader",
                                "If your downloads are as MP4 you will have to change to .MP3 manually, just delete the .mp4 and put .mp3.")

            DebugInfo.logger_info.info("[BUG] exception FileNotFoundError from URL: %s",self.url_playlist)
        except Exception as e:
            global ERROR_04
            ERROR_04 = True
            DebugInfo.logger_error.error(e, exc_info=True)
            messagebox.showerror("DYGTube Downloader",
                                 "Something went wrong! check playlist link")
        if not ERROR_04:
            messagebox.showinfo("DYG Downloader", 
                                "The playlist has been downloaded successfully!")


    def download_playlist_mp4(self):
        """Here the download of the playlist will start."""

        try:
            pl = Playlist(self.url_playlist)
            for video in pl.videos:
                try:
                    print(video.title)
                    video.streams.get_highest_resolution().download(self.path_to_save)
                    DebugInfo.info
                    DebugInfo.logger_info.info("[INFO] (From source playlist) Starting to download video MP4 from URL: %s",self.url_playlist)
                except Exception as e:
                    global ERROR_05
                    ERROR_05 = True
                    DebugInfo.info
                    DebugInfo.logger_error.error(e, exc_info=True)
                    messagebox.showerror("DYGTube Downloader",
                                        "Something went wrong! check playlist link")
            if not ERROR_05:
                messagebox.showinfo("DYG Downloader", 
                            "The playlist has been downloaded successfully!")


        except Exception as e:
            global ERROR_06
            ERROR_06 = True 
            DebugInfo.info
            DebugInfo.logger_error.error(e, exc_info=True)
            messagebox.showerror("DYG Downloader", "Something went wrong! check playlist link.")
        if not ERROR_06:
            messagebox.showinfo("DYG Downloader", "The playlist has been downloaded successfully!")
