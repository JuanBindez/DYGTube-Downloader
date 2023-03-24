# this is part of the DYGtube Downloader project.
#
# Release: v2.10.3-rc
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


def sobre_software():
   """displays information about the program.

   clicking on the button will open a window with information.
   """
    
   window = Tk()
   window.title("DYGTube Downloader")
   window.geometry("435x200")
   window['background'] = '#373636'
   window.resizable(False, False)
   window.attributes('-alpha',9.1)

   """information:

   website to generate colors in hex:  https://www.rapidtables.com/web/color/RGB_Color.html

   y is height and x is for sides.
   """
  
   GENERAL_BACKGROUND_COLOR = '#373636'
   COLOR_DYGTUBE_NAME = 'white'
   COLOR_VERSION = '#00E9CA'
   COLOR_DESCRIPTION = 'white'
   COLOR_NO_WARRANTY = '#00E9CA'
   COLOR_GPLV2 = 'white'
   COLOR_COPYRIGHT = '#00E9CA'

   label = Label(window,
                text="DYGTube",
                fg=COLOR_DYGTUBE_NAME, 
                bg=GENERAL_BACKGROUND_COLOR).place(x=188, y=10)

   label = Label(window,
                text="v2.10.3-rc",
                fg=COLOR_VERSION,
                bg=GENERAL_BACKGROUND_COLOR).place(x=195, y=29)

   label = Label(window, 
                text="DYGTube downloads MP4 video and audio MP3.", 
                fg=COLOR_DESCRIPTION, 
                bg=GENERAL_BACKGROUND_COLOR).place(x=55, y=80)

   label = Label(window,
                text="This software comes with absolutely no warranty.", 
                fg=COLOR_NO_WARRANTY, 
                bg=GENERAL_BACKGROUND_COLOR).place(x=45, y=110)

   label = Label(window, 
                text="For more details, visit the GNU General Public License, version 2", 
                fg=COLOR_GPLV2,
                bg=GENERAL_BACKGROUND_COLOR).place(x=9, y=150)
                
   label = Label(window,
                text="Copyright (c) 2022-2023  Juan Bindez", 
                fg=COLOR_COPYRIGHT, 
                bg=GENERAL_BACKGROUND_COLOR).place(x=80, y=170)
