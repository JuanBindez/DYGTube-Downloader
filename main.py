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
from tkinter import ttk

def progress_bar():
  #bloco de interface progress
  global window_progress

  window_progress = Tk()
  window_progress.title("DYG Downloader")
  window_progress.geometry("400x100")
  window_progress['background'] = '#4E4E4E'# site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
  window_progress.resizable(False, False)# False para não responsivo e True para responsivo.
  window_progress.attributes('-alpha',9.1)

  global progress

  progress = ttk.Progressbar(window_progress, orient=HORIZONTAL,
      length=300, mode='determinate')

  progress.pack(pady=30)


def download_video():
  """Aqui é feito o download do video.
     a variavel link recebe a url.
  """

  progress_bar()
  progress['value'] = 0
  label = Label(window_progress,
                text="0 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
  time.sleep(3)

  link = entrada_de_dados.get()

  yt = YouTube(link, on_progress_callback = on_progress)
  messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
  ys = yt.streams.get_highest_resolution()
  ys.download()

  time.sleep(2)
  label = Label(window_progress,
                text="10 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
  progress.update_idletasks()
  progress['value'] = 10

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 50
 
  label = Label(window_progress,
                text="50 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 60
  
  label = Label(window_progress,
                text="60 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 70
  
  label = Label(window_progress,
                text="70 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 80
  
  label = Label(window_progress,
                text="80 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 90
  
  label = Label(window_progress,
                text="90 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
                
  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 100
 
  time.sleep(1)
  label = Label(window_progress,
                text="100 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
 
  time.sleep(2)
  label = Label(window_progress,
                  text="Dowload Concluído!",
                  fg='white',
                  bg="#4E4E4E").place(x=140, y=60)

  
def download_mp3():
  """Esta função faz download apenas do áudio."""
  
  progress_bar()
  progress['value'] = 0
  label = Label(window_progress,
                text="0 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
  time.sleep(3)

  link = entrada_de_dados.get()
  
  yt = YouTube(link, on_progress_callback = on_progress)
  messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
  ys = yt.streams.get_audio_only()
  ys.download()

  time.sleep(2)
  label = Label(window_progress,
                text="10 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
  progress.update_idletasks()
  progress['value'] = 10

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 50
 
  label = Label(window_progress,
                text="50 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 60
  
  label = Label(window_progress,
                text="60 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 70
  
  label = Label(window_progress,
                text="70 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 80
  
  label = Label(window_progress,
                text="80 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)

  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 90
  
  label = Label(window_progress,
                text="90 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
                
  time.sleep(1)
  progress.update_idletasks()
  progress['value'] = 100
 
  time.sleep(1)
  label = Label(window_progress,
                text="100 %",
                fg='white',
                bg="#4E4E4E").place(x=190, y=60)
 
  time.sleep(2)
  label = Label(window_progress,
                  text="Dowload Concluído!",
                  fg='white',
                  bg="#4E4E4E").place(x=140, y=60)

def combo_mix():
  """faz download de varios ao mesmo tempo"""

  def download_video():
    """Aqui é feito o download do video.
      a variavel link recebe a url.
    """

    link_1 = entrada_url_1.get()
    
    yt = YouTube(link_1, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)

    link_2 = entrada_url_2.get()

    yt = YouTube(link_2, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)

    link_3 = entrada_url_3.get()
    
    yt = YouTube(link_3, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)

    link_4 = entrada_url_4.get()

    yt = YouTube(link_4, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)


    link_5 = entrada_url_5.get()
    
    yt = YouTube(link_5, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)

    link_6 = entrada_url_6.get()

    yt = YouTube(link_6, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)


    link_7 = entrada_url_7.get()
    
    yt = YouTube(link_7, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)


    link_8 = entrada_url_8.get()

    yt = YouTube(link_8, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)

  
    link_9 = entrada_url_9.get()
    
    yt = YouTube(link_9, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)

  
    link_10 = entrada_url_10.get()

    yt = YouTube(link_10, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    time.sleep(3)

    messagebox.showinfo("DYG Downloader", "Seus Dowloads Estão Prontos")
    
    # fim do bloco download video da opção mix

  def download_mp3():
    """Esta função faz download apenas do áudio."""

    link_1 = entrada_url_1.get()
    
    yt = YouTube(link_1, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(1)

    link_2 = entrada_url_2.get()

    yt = YouTube(link_2, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(1)

    link_3 = entrada_url_3.get()
    
    yt = YouTube(link_3, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(3)
  
    link_4 = entrada_url_4.get()

    yt = YouTube(link_4, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(3)

    link_5 = entrada_url_5.get()
    
    yt = YouTube(link_5, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(3)

    link_6 = entrada_url_6.get()

    yt = YouTube(link_6, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(3)

    link_7 = entrada_url_7.get()
    
    yt = YouTube(link_7, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(3)

    link_8 = entrada_url_8.get()

    yt = YouTube(link_8, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(3)

    link_9 = entrada_url_9.get()
    
    yt = YouTube(link_9, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(3)

    link_10 = entrada_url_10.get()

    yt = YouTube(link_10, on_progress_callback = on_progress)
    #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
    ys = yt.streams.get_audio_only()
    ys.download()
    time.sleep(3)

    messagebox.showinfo("DYG Downloader", "Seus Dowloads Estão Prontos")

    # fim do bloco download MP3 da opção mix


  def info_function():
    """exibe informações sobre a função mix.
      ao clicar no botão sobre abrirá uma janela com informações.
    """

    messagebox.showinfo("DYG Downloader", "Com esta função você pode baixar até 10 vídeos e MP3 com apenas 1 click")
    


  #bloco de interface da opção mix.
  window = Tk()
  window.title("DYG Downloader")
  window.geometry("435x600")
  window['background'] = '#4E4E4E'# site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
  window.resizable(False, False)# False para não responsivo e True para responsivo.
  window.attributes('-alpha',9.1)

  
  label = Label(window,
                text="URL 1*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=60)# y é altura e x é para os lados

  entrada_url_1 = Entry(window, width=40)
  entrada_url_1.place(x=95, y=60)


  label = Label(window,
                text="URL 2*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=85)

  entrada_url_2 = Entry(window, width=40)
  entrada_url_2.place(x=95, y=85)


  label = Label(window,
                text="URL 3*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=110)# y é altura e x é para os lados

  entrada_url_3 = Entry(window, width=40)
  entrada_url_3.place(x=95, y=110)


  label = Label(window,
                text="URL 4*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=135)

  entrada_url_4 = Entry(window, width=40)
  entrada_url_4.place(x=95, y=135)

  label = Label(window,
                text="URL 5*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=160)# y é altura e x é para os lados

  entrada_url_5 = Entry(window, width=40)
  entrada_url_5.place(x=95, y=160)


  label = Label(window,
                text="URL 6*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=185)

  entrada_url_6 = Entry(window, width=40)
  entrada_url_6.place(x=95, y=185)


  label = Label(window,
                text="URL 7*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=210)# y é altura e x é para os lados

  entrada_url_7 = Entry(window, width=40)
  entrada_url_7.place(x=95, y=210)


  label = Label(window,
                text="URL 8*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=235)

  entrada_url_8 = Entry(window, width=40)
  entrada_url_8.place(x=95, y=235)


  label = Label(window,
                text="URL 9*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=260)# y é altura e x é para os lados

  entrada_url_9 = Entry(window, width=40)
  entrada_url_9.place(x=95, y=260)


  label = Label(window,
                text="URL 10*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=285)

  entrada_url_10 = Entry(window, width=40)
  entrada_url_10.place(x=95, y=285)


  # botão que inicia o download do video da opção mix.
  botao_video = Button(window,
                  text="Download Vídeo",
                  command=download_video,
                  fg='white',
                  bg='green',).place(x=90, y=500)

  # botão para iniciar download apenas do auidio do vídeo da opção mix.
  botao_mp3 = Button(window,
                text="Download MP3",
                command=download_mp3,
                fg='white',
                bg='green',).place(x=240, y=500)


  botao_info = Button(window,
                text="Info",
                command=info_function,
                fg='black',
                bg='grey',
                width=2,).place(x=390, y=2)# y é altura e x é para os lados

  # fim do bloco da opção mix


def sobre_software():
  """exibe informações sobre o programa.
     ao clicar no botão sobre abrirá uma janela com informações.
  """
  
  #bloco de interface sobre o software.
  window = Tk()
  window.title("DYG Downloader")
  window.geometry("435x200")
  window['background'] = '#4E4E4E'# site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
  window.resizable(False, False)# False para não responsivo e True para responsivo.
  window.attributes('-alpha',9.1)

  label = Label(window,
                text="DYG",
                fg='white', 
                bg="#4E4E4E").place(x=200, y=10)# y é altura e x é para os lados

  label = Label(window,
                text="v2.1.0",
                fg='white',
                bg="#4E4E4E").place(x=195, y=29)

  label = Label(window, 
                text="O DYG faz download de video e audio MP3 do Youtube.", 
                fg='white', 
                bg="#4E4E4E").place(x=50, y=80)

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


#bloco de interface principal
window = Tk()
window.title("DYG Downloader")
window.geometry("500x200")
window['background'] = '#4E4E4E'# site para gerar cores Hex:  https://www.rapidtables.com/web/color/RGB_Color.html
window.resizable(False, False)# False para não responsivo e True para responsivo.
window.attributes('-alpha',9.1)


label = Label(window,
                text="URL*",
                fg='white',
                bg="#4E4E4E").place(x=40, y=60)# y é altura e x é para os lados


entrada_de_dados = Entry(window, width=40)
entrada_de_dados.place(x=95, y=60)

# botão que inicia o download.
botao = Button(window,
                text="Download Vídeo",
                command=download_video,
                fg='white',
                bg='green',).place(x=120, y=130)

# botão para iniciar download apenas do auidio do vídeo.
botao_mp3 = Button(window,
                text="Download MP3",
                command=download_mp3,
                fg='white',
                bg='green',).place(x=270, y=130)


# botão para exibir informações sobre o programa.
botao_sobre = Button(window,
                text="Sobre",
                command=sobre_software,
                fg='black',
                bg='grey',
                width=2,).place(x=455, y=2)# y é altura e x é para os lados


botao_combo = Button(window,
                text="mix",
                command=combo_mix,
                fg='black',
                bg='grey',
                width=2,).place(x=455, y=30)


if __name__ == "__main__":
  window.mainloop()
#fim do bloco de interface
