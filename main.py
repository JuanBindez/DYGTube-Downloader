# Release: v2.5.3-rc3
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
import urllib3
import time
    
from tkinter import *
from tkinter import ttk
from src.source import DownloadInit
from src.playlist_download_module import download_playlist
from src.escolha_mix_module import escolha_mix
from src.sobre_module import sobre_software


def download_video():
  """Aqui é feito o download do video.
     a variavel link recebe a url.
  """

  link = entrada_de_dados.get()

  DI = DownloadInit(link)
  DI.download_video_mp4()
  
  
def download_mp3():
  """Esta função faz download apenas do áudio."""

  link = entrada_de_dados.get()
  
  DI = DownloadInit(link)
  DI.download_audio_mp3()


window = Tk()
window.title("DYGTube Downloader")
window.geometry("500x260")
window['background'] = '#4E4E4E'                    # site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
window.resizable(False, False)                      # False para não responsivo e True para responsivo.
window.attributes('-alpha',9.1)

color_frame = '#585757'
color_botao = '#3D3D3D'

frame = Frame(window, width=600, height=35, bg=color_frame)
frame.grid(row=0, column=0)


label = Label(window,
                text="URL*",
                fg='#09AF30',
                bg="#4E4E4E").place(x=40, y=80)     # y é altura e x é para os lados

def make_menu(w):
    global the_menu_1
    the_menu_1 = Menu(w, tearoff=0)
    the_menu_1.add_command(label="Colar")
    
    
def show_menu(e):
    w = e.widget
    the_menu_1.entryconfigure("Colar",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu_1.tk.call("tk_popup", the_menu_1, e.x_root, e.y_root)


make_menu(window)
entrada_de_dados = Entry(window, width=40)
entrada_de_dados.place(x=95, y=80)
entrada_de_dados.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
lbl = Label(window, text = "")

# botão que inicia o download.
botao = Button(window,
                text="Download Vídeo",
                command=download_video,
                fg='#09AF30',
                bg=color_botao,).place(x=120, y=160)

# botão para iniciar download apenas do auidio do vídeo.
botao_mp3 = Button(window,
                text="Download MP3",
                command=download_mp3,
                fg='#09AF30',
                bg=color_botao,).place(x=270, y=160)


# botão para exibir informações sobre o programa.
botao_sobre = Button(window,
                text="Sobre",
                command=sobre_software,
                fg='#09AF30',
                bg=color_botao,
                width=3,).place(x=103, y=2)          # y é altura e x é para os lados


botao_playlist = Button(window,
                text="playlist",
                command=download_playlist,
                fg='#09AF30',
                bg=color_botao,
                width=4,).place(x=45, y=2)           # y é altura e x é para os lados


botao_combo = Button(window,
                text="mix",
                command=escolha_mix,
                fg='#09AF30',
                bg=color_botao,
                width=2,).place(x=2, y=2)


if __name__ == "__main__":
  window.mainloop()
