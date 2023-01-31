# Release: v2.6.0-rc1
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
   window.geometry("440x200")
   window['background'] = '#4E4E4E'
   window.resizable(False, False)
   window.attributes('-alpha',9.1)

   """information:

   website to generate colors in hex:  https://www.rapidtables.com/web/color/RGB_Color.html

   y is height and x is for sides.
   """
  
   GENERAL_BACKGROUND_COLOR = '#4E4E4E'
   COLOR_DYGTUBE_NAME = 'white'
   COLOR_VERSION = 'white'
   COLOR_DESCRIPTION = 'white'
   COLOR_NO_WARRANTY = '#09AF30'
   COLOR_GPLV2 = 'white'
   COLOR_COPYRIGHT = '#09AF30'

   label = Label(window,
                text="DYGTube",
                fg=COLOR_DYGTUBE_NAME, 
                bg=GENERAL_BACKGROUND_COLOR).place(x=188, y=10)

   label = Label(window,
                text="v2.6.0-rc1",
                fg=COLOR_VERSION,
                bg=GENERAL_BACKGROUND_COLOR).place(x=195, y=29)

   label = Label(window, 
                text="O DYGTube faz download de video e audio MP3 do Youtube.", 
                fg=COLOR_DESCRIPTION, 
                bg=GENERAL_BACKGROUND_COLOR).place(x=27, y=80)

   label = Label(window,
                text="Este programa vem com absolutamente nenhuma garantia.", 
                fg=COLOR_NO_WARRANTY, 
                bg=GENERAL_BACKGROUND_COLOR).place(x=21, y=110)

   label = Label(window, 
                text="Para mais detalhes, visite Licença Pública Geral GNU, versão 2", 
                fg=COLOR_GPLV2,
                bg=GENERAL_BACKGROUND_COLOR).place(x=15, y=150)
                
   label = Label(window,
                text="Copyright (c) 2022-2023  Juan Bindez", 
                fg=COLOR_COPYRIGHT, 
                bg=GENERAL_BACKGROUND_COLOR).place(x=80, y=170)
