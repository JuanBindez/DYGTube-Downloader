# this is part of the DYGtube Downloader project.
#
# Release: v2.9.2-alpha
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

from src.debug import DebugInfo
from src.source import DownloadInit
from src.source import PlaylistDownload
from src.progress_bar_module import progress_bar

try:
  def choice_mix():
    """download multiple files at the same time"""

    def download_mix_video():
      """Here the video is downloaded.
      
      the link variable receives the url.
      """ 

      link_1 = entrada_url_1.get()
      di = DownloadInit(link_1)
      di.download_video_mp4()

      link_2 = entrada_url_2.get()
      di = DownloadInit(link_2)
      di.download_video_mp4()

      link_3 = entrada_url_3.get()
      di = DownloadInit(link_3)
      di.download_video_mp4()

      link_4 = entrada_url_4.get()
      di = DownloadInit(link_4)
      di.download_video_mp4()

      link_5 = entrada_url_5.get()
      di = DownloadInit(link_5)
      di.download_video_mp4()

      link_6 = entrada_url_6.get()
      di = DownloadInit(link_6)
      di.download_video_mp4()

      link_7 = entrada_url_7.get()
      di = DownloadInit(link_7)
      di.download_video_mp4()

      link_8 = entrada_url_8.get()
      di = DownloadInit(link_8)
      di.download_video_mp4()
    
      link_9 = entrada_url_9.get()
      di = DownloadInit(link_9)
      di.download_video_mp4()
    
      link_10 = entrada_url_10.get()
      di = DownloadInit(link_10)
      di.download_video_mp4()

      messagebox.showinfo("DYG Downloader", "Seus Dowloads Estão Prontos")
    

    def download_mix_mp3():
      """This function only downloads the audio."""

      link_1 = entrada_url_1.get()
      di = DownloadInit(link_1)
      di.download_audio_mp3()

      link_2 = entrada_url_2.get()
      di = DownloadInit(link_2)
      di.download_audio_mp3()

      link_3 = entrada_url_3.get()
      di = DownloadInit(link_3)
      di.download_audio_mp3()

      link_4 = entrada_url_4.get()
      di = DownloadInit(link_4)
      di.download_audio_mp3()

      link_5 = entrada_url_5.get()
      di = DownloadInit(link_5)
      di.download_audio_mp3()

      link_6 = entrada_url_6.get()
      di = DownloadInit(link_6)
      di.download_audio_mp3()

      link_7 = entrada_url_7.get()
      di = DownloadInit(link_7)
      di.download_audio_mp3()

      link_8 = entrada_url_8.get()
      di = DownloadInit(link_8)
      di.download_audio_mp3()

      link_9 = entrada_url_9.get()
      di = DownloadInit(link_9)
      di.download_audio_mp3()

      link_10 = entrada_url_10.get()
      di = DownloadInit(link_10)
      di.download_audio_mp3()
      
      messagebox.showinfo("DYG Downloader", "Seus Dowloads Estão Prontos")


    window = Tk()
    window.title("DYGTube Downloader")
    window.geometry("450x500")
    window['background'] = '#373636'
    window.resizable(False, False)
    window.attributes('-alpha',9.1)

    """information:

    website to generate colors in hex:  https://www.rapidtables.com/web/color/RGB_Color.html

    y is height and x is for sides
    """
    
    def info_function():
      """displays information about the mix function.
      clicking on the button will open a window with information.
      """
      messagebox.showinfo("DYG Downloader", "here you make 10 downloads at once")

    def make_menu(w):
      global the_menu
      the_menu = Menu(w, tearoff=0)
      the_menu.add_command(label="Colar")
      
    def show_menu(e):
        w = e.widget
        the_menu.entryconfigure("Colar",
        command=lambda: w.event_generate("<<Paste>>"))
        the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

    COLOR_FRAME = '#585757'
    GENERAL_BACKGROUND_COLOR = '#373636'
    BUTTON_COLOR = '#191A1A'
    LETTER_FG_COLOR = '#00E9CA'

    frame = Frame(window, width=600, height=35, bg=COLOR_FRAME)
    frame.grid(row=0, column=0)

    label = Label(window,
                  text="URL 1*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=60)

    make_menu(window)
    entrada_url_1 = Entry(window, width=40)
    entrada_url_1.place(x=95, y=60)
    entrada_url_1.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    lbl = Label(window, text = "")

    label = Label(window,
                  text="URL 2*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=85)

    entrada_url_2 = Entry(window, width=40)
    entrada_url_2.place(x=95, y=85)

    label = Label(window,
                  text="URL 3*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=110)
    entrada_url_3 = Entry(window, width=40)
    entrada_url_3.place(x=95, y=110)

    label = Label(window,
                  text="URL 4*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=135)

    entrada_url_4 = Entry(window, width=40)
    entrada_url_4.place(x=95, y=135)

    label = Label(window,
                  text="URL 5*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=160)

    entrada_url_5 = Entry(window, width=40)
    entrada_url_5.place(x=95, y=160)

    label = Label(window,
                  text="URL 6*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=185)

    entrada_url_6 = Entry(window, width=40)
    entrada_url_6.place(x=95, y=185)

    label = Label(window,
                  text="URL 7*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=210)

    entrada_url_7 = Entry(window, width=40)
    entrada_url_7.place(x=95, y=210)

    label = Label(window,
                  text="URL 8*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=235)

    entrada_url_8 = Entry(window, width=40)
    entrada_url_8.place(x=95, y=235)

    label = Label(window,
                  text="URL 9*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=260)

    entrada_url_9 = Entry(window, width=40)
    entrada_url_9.place(x=95, y=260)

    label = Label(window,
                  text="URL 10*",
                  fg=LETTER_FG_COLOR,
                  bg=GENERAL_BACKGROUND_COLOR).place(x=40, y=285)

    entrada_url_10 = Entry(window, width=40)
    entrada_url_10.place(x=95, y=285)

    # mix download option dutton video.
    botao_video = Button(window,
                    text="Download Video",
                    command=download_mix_video,
                    fg=LETTER_FG_COLOR,
                    bg=BUTTON_COLOR,).place(x=90, y=400)
    # button to start downloading only the audio of the video from the mix option.
    botao_mp3 = Button(window,
                  text="Download MP3",
                  command=download_mix_mp3,
                  fg=LETTER_FG_COLOR,
                  bg=BUTTON_COLOR,).place(x=240, y=400)

    botao_info = Button(window,
                  text="Info",
                  command=info_function,
                  fg=LETTER_FG_COLOR,
                  bg=BUTTON_COLOR,
                  width=2,).place(x=405, y=2)
                  
except Exception as e:
  DebugInfo.logger_error.error(e, exc_info=True)
