# this is part of the DYGtube Downloader project.
#
# Release: v3.0-rc3
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


from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

from src.debug import DebugInfo
from src.source import MixDownload
from src.source import PlaylistDownload

try:
  def choice_mix():
    """download multiple files at the same time"""

    def download_mix_video():
      """Here the video is downloaded.
      the link variable receives the url.
      """ 
      save_path = filedialog.askdirectory()

      link_1 = entrada_url_1.get()
      di = MixDownload(link_1, save_path)
      di.download_video_mp4()

      link_2 = entrada_url_2.get()
      di = MixDownload(link_2, save_path)
      di.download_video_mp4()

      link_3 = entrada_url_3.get()
      di = MixDownload(link_3, save_path)
      di.download_video_mp4()

      link_4 = entrada_url_4.get()
      di = MixDownload(link_4, save_path)
      di.download_video_mp4()

      link_5 = entrada_url_5.get()
      di = MixDownload(link_5, save_path)
      di.download_video_mp4()

      link_6 = entrada_url_6.get()
      di = MixDownload(link_6, save_path)
      di.download_video_mp4()

      link_7 = entrada_url_7.get()
      di = MixDownload(link_7, save_path)
      di.download_video_mp4()

      link_8 = entrada_url_8.get()
      di = MixDownload(link_8, save_path)
      di.download_video_mp4()
    
      link_9 = entrada_url_9.get()
      di = MixDownload(link_9, save_path)
      di.download_video_mp4()
    
      link_10 = entrada_url_10.get()
      di = MixDownload(link_10, save_path)
      di.download_video_mp4()

      messagebox.showinfo("DYG Downloader", "Your Dowloads Are Ready")
    

    def download_mix_mp3():
      """This function only downloads the audio."""

      save_path = filedialog.askdirectory()

      link_1 = entrada_url_1.get()
      di = MixDownload(link_1, save_path)
      di.download_audio_mp3()

      link_2 = entrada_url_2.get()
      di = MixDownload(link_2, save_path)
      di.download_audio_mp3()

      link_3 = entrada_url_3.get()
      di = MixDownload(link_3, save_path)
      di.download_audio_mp3()

      link_4 = entrada_url_4.get()
      di = MixDownload(link_4, save_path)
      di.download_audio_mp3()

      link_5 = entrada_url_5.get()
      di = MixDownload(link_5, save_path)
      di.download_audio_mp3()

      link_6 = entrada_url_6.get()
      di = MixDownload(link_6, save_path)
      di.download_audio_mp3()

      link_7 = entrada_url_7.get()
      di = MixDownload(link_7, save_path)
      di.download_audio_mp3()

      link_8 = entrada_url_8.get()
      di = MixDownload(link_8, save_path)
      di.download_audio_mp3()

      link_9 = entrada_url_9.get()
      di = MixDownload(link_9, save_path)
      di.download_audio_mp3()

      link_10 = entrada_url_10.get()
      di = MixDownload(link_10, save_path)
      di.download_audio_mp3()
      
      messagebox.showinfo("DYG Downloader", "Your Dowloads Are Ready")


    window = Tk()
    window.title("DYGTube Downloader")
    window.geometry("480x450")
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
      the_menu.add_command(label="Paste")
      
    def show_menu(e):
        w = e.widget
        the_menu.entryconfigure("Paste",
        command=lambda: w.event_generate("<<Paste>>"))
        the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

    COLOR_FRAME = '#585757'
    GENERAL_BACKGROUND_COLOR = '#373636'
    BUTTON_COLOR = '#191A1A'
    LETTER_FG_COLOR = '#00E9CA'

    label = Label(window,
                  text="URL 1*",).place(x=40, y=60)

    make_menu(window)
    entrada_url_1 = Entry(window, width=40)
    entrada_url_1.place(x=95, y=60)
    entrada_url_1.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
    lbl = Label(window, text = "")

    label = Label(window,
                  text="URL 2*",).place(x=40, y=85)

    entrada_url_2 = Entry(window, width=40)
    entrada_url_2.place(x=95, y=85)

    label = Label(window,
                  text="URL 3*",).place(x=40, y=110)
    
    entrada_url_3 = Entry(window, width=40)
    entrada_url_3.place(x=95, y=110)

    label = Label(window,
                  text="URL 4*",).place(x=40, y=135)

    entrada_url_4 = Entry(window, width=40)
    entrada_url_4.place(x=95, y=135)

    label = Label(window,
                  text="URL 5*",).place(x=40, y=160)

    entrada_url_5 = Entry(window, width=40)
    entrada_url_5.place(x=95, y=160)

    label = Label(window,
                  text="URL 6*",).place(x=40, y=185)

    entrada_url_6 = Entry(window, width=40)
    entrada_url_6.place(x=95, y=185)

    label = Label(window,
                  text="URL 7*",).place(x=40, y=210)

    entrada_url_7 = Entry(window, width=40)
    entrada_url_7.place(x=95, y=210)

    label = Label(window,
                  text="URL 8*",).place(x=40, y=235)

    entrada_url_8 = Entry(window, width=40)
    entrada_url_8.place(x=95, y=235)

    label = Label(window,
                  text="URL 9*",).place(x=40, y=260)

    entrada_url_9 = Entry(window, width=40)
    entrada_url_9.place(x=95, y=260)

    label = Label(window,
                  text="URL 10*",).place(x=40, y=285)

    entrada_url_10 = Entry(window, width=40)
    entrada_url_10.place(x=95, y=285)


    botao_video = Button(window,
                    text="Download Video",
                    command=download_mix_video,
                    width=60,).place(x=0, y=348)
    

    botao_mp3 = Button(window,
                  text="Download MP3",
                  command=download_mix_mp3,
                  width=60,).place(x=0, y=385)

                  
except Exception as e:
  DebugInfo.logger_info.info("------------------------------start debugging--------------------------------")
  DebugInfo.logger_info.info("(From mix mudule) Error found ")
  DebugInfo.logger_error.error(e, exc_info=True)
