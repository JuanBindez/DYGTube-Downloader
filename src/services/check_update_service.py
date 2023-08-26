# this is part of the DYGtube Downloader project.
#
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
import json

import tkinter as tk
from tkinter import messagebox
import urllib.request
import webbrowser


def check_new_version(current_version):
    version_url = "https://raw.githubusercontent.com/JuanBindez/DYGTube-Downloader/main/version.json"

    try:
        with urllib.request.urlopen(version_url) as response:
            version_info = response.read().decode().strip()

        version_data = json.loads(version_info)
        latest_version = version_data.get("version", "")

        if latest_version != current_version:
            message = f"DYGTube {latest_version} Available!\n\n"
            message += f"Release Date: {version_data.get('release_date', '')}\n"
            message += f"\nNew:\n{version_data.get('new', '- ')}"

            link_update = version_data.get('link', '')
            link = link_update[0]

            ask = messagebox.askokcancel("DYGTube Downloader", message + "\n\n\n\nwant to update?")
            if ask == True:
                webbrowser.open(link)
                exit()
            elif ask == False:
                pass

    except urllib.error.URLError:
        messagebox.showerror("Caution", "no internet connection")
