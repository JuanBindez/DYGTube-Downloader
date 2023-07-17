# this is part of the DYGtube Downloader project.
#
# Release: v3.0.0
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


import time

from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def notify_dowload():

    root = Tk()
    root.withdraw()

    top = Toplevel()
    top.title("DYGTube Downloader")
    label = Label(top, text="Download Complete.")
    label.pack(padx=40, pady=40)

    tempo_espera = 400

    def fechar_tela():
        root.destroy()

    top.after(tempo_espera, fechar_tela)

    root.mainloop()
