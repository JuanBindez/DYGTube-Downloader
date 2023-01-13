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


from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def sobre_software():
  """exibe informações sobre o programa.
     ao clicar no botão sobre abrirá uma janela com informações.
  """
  
  #bloco de interface sobre o software.
  window = Tk()
  window.title("DYGTube Downloader")
  window.geometry("440x200")
  window['background'] = '#4E4E4E'# site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
  window.resizable(False, False)# False para não responsivo e True para responsivo.
  window.attributes('-alpha',9.1)

  label = Label(window,
                text="DYGTube",
                fg='white', 
                bg="#4E4E4E").place(x=188, y=10)# y é altura e x é para os lados

  label = Label(window,
                text="v2.5.3-rc3",
                fg='white',
                bg="#4E4E4E").place(x=195, y=29)

  label = Label(window, 
                text="O DYGTube faz download de video e audio MP3 do Youtube.", 
                fg='white', 
                bg="#4E4E4E").place(x=27, y=80)

  label = Label(window,
                text="Este programa vem com absolutamente nenhuma garantia.", 
                fg='#09AF30', 
                bg="#4E4E4E").place(x=21, y=110)# y é altura e x é para os lados

  label = Label(window, 
                text="Para mais detalhes, visite Licença Pública Geral GNU, versão 2", 
                fg='white',
                bg="#4E4E4E").place(x=15, y=150)# y é altura e x é para os lados

  label = Label(window,
                text="Copyright (c) 2022-2023  Juan Bindez", 
                fg='#09AF30', 
                bg="#4E4E4E").place(x=80, y=170)
