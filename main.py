'''
Author: www.github.com/JuanBindez
Description: download youtube videos
Python Version: 3.10
year: 2022
Local: Brazil
'''

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
    

    label = Label(window, text="Cole Seu Link Aqui:").place(x=20, y=60)# y é altura e x é para os lados
    #label.grid(row=0, column=0)
    entrada_de_dados = Entry(window, width=40)
    entrada_de_dados.place(x=150, y=60)
    #entrada_de_dados.grid(row=0, column=1)

    label_discricao = Label(window, text="Autor: Juan Bindez <https://github.com/JuanBindez>   2022 v0.1").place(x=20, y=170)


    botao = Button(window, text="Iniciar Download", command=download_youtube).place(x=180, y=100)
    #botao.grid(row=4, column=1)


    window.mainloop()
    #fim do bloco de interface


except AttributeError:
  messagebox.showinfo("Atenção!!!", "Houve Um Erro De Atributo!")

  
