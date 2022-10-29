# downloader of the Youtube.
#
# Copyright (c) 2022  Juan Carlos Bindez
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
# autor: https://github.com/juanBindez <juanbindez780@gmail.com>


import os
import urllib3
import time
    
from pytube import YouTube
from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox


def download_youtube():
  """Aqui é feito o download do video.
     a variavel link recebe a url."""

  link = entrada_de_dados.get()
  yt = YouTube(link, on_progress_callback = on_progress)
  messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
  ys = yt.streams.get_highest_resolution()
  ys.download()
  time.sleep(5)

  # exibe a menssagem de conclusão do download.
  messagebox.showinfo("DYG Downloader", "Seu Dowload Esta Pronto")
      

def sobre_software():
  """exibe informações sobre o programa.
     ao clicar no botão sobre abrirá uma janela com informações."""
     
  window = Tk()
  window.title("DYG Downloader")
  window.geometry("435x200")
  window['background'] = '#4E4E4E'# site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
  window.resizable(False, False)# False para não responsivo e True para responsivo.

  label = Label(window,
                text="DYG",
                fg='white', 
                bg="#4E4E4E").place(x=200, y=10)# y é altura e x é para os lados

  label = Label(window,
                text="v1.0.0",
                fg='white',
                bg="#4E4E4E").place(x=195, y=29)

  label = Label(window, 
                text="O DYG faz download de video do Youtube.", 
                fg='white', 
                bg="#4E4E4E").place(x=70, y=80)

  label = Label(window,
                text="Este programa vem com absolutamente nenhuma garantia.", 
                fg='red', 
                bg="#4E4E4E").place(x=20, y=110)# y é altura e x é para os lados

  label = Label(window, 
                text="Para mais detalhes, visite Licença Pública Geral GNU, versão 2", 
                fg='white',
                bg="#4E4E4E").place(x=15, y=150)# y é altura e x é para os lados

  label = Label(window,
                text="Copyright (c) 2022 Juan Carlos Bindez", 
                fg='black', 
                bg="#4E4E4E").place(x=80, y=170)


#bloco de interface
window = Tk()
window.title("DYG Downloader")
window.geometry("500x200")
window['background'] = '#4E4E4E'# site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
window.resizable(False, False)# False para não responsivo e True para responsivo.

label = Label(window,
                text="URL*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=60)# y é altura e x é para os lados


entrada_de_dados = Entry(window, width=40)
entrada_de_dados.place(x=95, y=60)

# botão que inicia o download.
botao = Button(window,
                text="Iniciar Download",
                command=download_youtube,
                fg='white',
                bg='green',).place(x=180, y=130)


# botão para exibir informações sobre o programa.
botao_sobre = Button(window,
                text="Sobre",
                command=sobre_software,
                fg='white',
                bg='grey',
                width=2,).place(x=455, y=2)

if __name__ == "__main__":
  window.mainloop()
#fim do bloco de interface
