# this is part of the DYGtube Downloader project.
#
# Release: v2.9.2-alpha
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

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def convert_avi():
    window = Tk()
    window.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4')])

    if file_path:
        video_clip = VideoFileClip(file_path)
        new_file_path = filedialog.asksaveasfilename(defaultextension='.avi', filetypes=[('Video Files', '*.avi')])

        if new_file_path:
            video_clip.write_videofile(new_file_path, codec='mpeg4')

        video_clip.close()

    window.mainloop()
