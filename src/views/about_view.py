# this is part of the DYGtube Downloader project.
#
#
# Copyright ©  2022 - 2024  Juan Bindez  <juanbindez780@gmail.com>
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


import base64

from pytubefix.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from src.views.version import *


def about_software():
   """displays information about the program.

   clicking on the button will open a window with information.
   """
    
   window = Tk()
   window.title("DYGTube Downloader")
   window.geometry("435x300")
   window.resizable(False, False)
   window.attributes('-alpha',9.1)

   custom_font_name = ('Arial', 15)
   label = Label(window,
                text="DYGTube",
                font=custom_font_name).place(x=178, y=27)
   
   custom_font_version = ('Arial', 14)
   label = Label(window,
                text=VERSION,
                font=custom_font_version).place(x=192, y=50)
   
   label = Label(window, 
                text="(MPEG-4 AAC audio codec)", ).place(x=128, y=110)

   label = Label(window, 
                text="DYGTube: downloads MP4 video and audio MP3.", ).place(x=55, y=147)

   label = Label(window,
                text="This software comes with absolutely no warranty.", ).place(x=45, y=177)

   label = Label(window, 
                text="For more details, visit the GNU General Public License, version 2", ).place(x=9, y=194)
                
   label = Label(window,
                text="Copyright © 2022 - 2024  Juan Bindez",).place(x=80, y=257)