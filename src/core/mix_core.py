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

class MixDownload():
    """This class will receive the url to download the video."""

    def __init__(self, link_url_input, save_path):
        self.link_url_input = link_url_input
        self.save_path = save_path

    def download_audio_mp3(self):
        """Here it will be downloaded in MP3"""

        try:
            if self.link_url_input == "":
                pass
            elif not self.link_url_input == "":
                pass

            EXTENSION_MP3 = '.mp3'
            EXTENSION_MP4 = '.mp4'

            yt = YouTube(self.link_url_input, on_progress_callback=on_progress)
            ys = yt.streams.get_audio_only()
            ys.download(self.save_path)

            downloaded_file_path = os.path.abspath(ys.default_filename)

            new_file_path = os.path.splitext(downloaded_file_path)[0] + EXTENSION_MP3
            os.rename(downloaded_file_path, new_file_path)

            DebugInfo.logger_info.info("[INFO] (From main) Starting to download audio MP3 from URL: %s",self.link_url_input)
            time.sleep(3)
        except KeyError:
            DebugInfo.logger_error.error(KeyError, exc_info=True)
            messagebox.showerror("DYG Downloader", "Unable to download, this is caused by some change on Youtube, try another video.")
        except Exception as e:
            global ERROR_01
            ERROR_01 = True
            DebugInfo.logger_error.error(e, exc_info=True)
        if not ERROR_01:
            messagebox.showinfo("DYG Downloader", "process concluded!")


    def download_video_mp4(self):
        """Here it will be downloaded in MP4 video."""

        try:
            if self.link_url_input == "":
                pass
            elif not self.link_url_input == "":
                pass

            yt = YouTube(self.link_url_input, on_progress_callback = on_progress)
            ys = yt.streams.get_highest_resolution()
            ys.download(self.save_path)
            DebugInfo.info
            DebugInfo.logger_info.info("([INFO] From source Init) Starting to download video MP4 from URL: %s",self.link_url_input)
            time.sleep(2)
        except KeyError:
            DebugInfo.info
            DebugInfo.logger_info.info("(Error from source Init) Error KeyError found in download video MP4 from URL: %s",self.link_url_input)
            DebugInfo.logger_error.error(KeyError, exc_info=True)
            messagebox.showerror("DYG Downloader", "Unable to download, this is caused by some change on Youtube, try another video.")
        except Exception as e:
            global ERROR_02
            ERROR_02 = True
            DebugInfo.info
            DebugInfo.logger_error.error(e, exc_info=True)
        if not ERROR_02:
            messagebox.showinfo("DYG Downloader", "process concluded!")
