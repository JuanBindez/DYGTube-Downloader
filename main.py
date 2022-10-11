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
# autor: https://github.com/juanBindez
# e-mail: juanbindez780@gmail.com


try:

    import os
    try:
      from pytube import YouTube
      from pytube.cli import on_progress
      from tkinter import *
      from tkinter import messagebox
      import time
    except ModuleNotFoundError:
      messagebox.showinfo("Atenção!!!", "você não tem o pytube instalado ,vou instalar pra você")
      os.system("pip install pytube")
      
    import urllib3
    import time

    

    def download_youtube():

      link = entrada_de_dados.get()

      yt = YouTube(link, on_progress_callback = on_progress)

      messagebox.showinfo("Youtube Downloader", "Titulo = " + yt.title)

      ys = yt.streams.get_highest_resolution()

      ys.download()
      time.sleep(5)

      messagebox.showinfo("Youtube Downloader", "Seu Dowload Esta Pronto")
      


  
    #bloco de interface
    window = Tk()
    window.title("Youtube Downloader")
    window.geometry("500x200")
    window['background'] = '#4E4E4E'# site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
    window.resizable(False, False)# False para não responsivo e True para responsivo.

    label = Label(window, text="Link *").place(x=20, y=60)# y é altura e x é para os lados
    #label.grid(row=0, column=0)
    entrada_de_dados = Entry(window, width=40)
    entrada_de_dados.place(x=150, y=60)
    #entrada_de_dados.grid(row=0, column=1)

    #label_discricao = Label(window, text="Autor: Juan Bindez <https://github.com/JuanBindez>   2022 v0.1").place(x=20, y=170)


    botao = Button(window, text="Iniciar Download", command=download_youtube, fg='white', bg='green').place(x=180, y=100)
    #botao.grid(row=4, column=1)


    window.mainloop()
    #fim do bloco de interface


except AttributeError:
  messagebox.showinfo("Atenção!!!", "Houve Um Erro De Atributo!")

  
