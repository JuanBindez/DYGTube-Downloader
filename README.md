

<h1 align="">
  <img alt="NextLevelWeek" title="#NextLevelWeek" src="DYGTube_logo.png" width="150px"/>
</h1>


<h1 align="">DYGTube 2.10.4</h1>

----------

### Access the website click __[here](https://dygtube.freesoftwarebrasil.com.br)__.

### about:

### This software effectively allows you to download videos and audios, with a friendly and intuitive interface, the user can choose the desired quality and output format, in addition to being able to download entire playlists at once. With its simplified functionality, the software provides an agile and practical experience for those who want to download multimedia content.

-----------
## Below is the step-by-step process for compiling (turning it into an executable), but if you prefer, the executable is already available on the website Visit the website click __[here](https://dygtube.freesoftwarebrasil.com.br)__.

![Captura de tela de 2023-03-11 14-00-45](https://user-images.githubusercontent.com/79322362/224499591-fbb09be4-1a75-49cd-8816-854b1c8d0ec0.png)

### Install Git:

    sudo apt install git

### Make a git clone:

    git clone https://github.com/JuanBindez/DYGTube-Downloader-v2.9.2-rc
    
### Access the folder:

    cd DYGTube-Downloader-v2.9.2-rc

### Activate the virtualenv and enter the command:


    pip install -r requirements.txt

### command to compile:


    pyinstaller --onefile --noconsole --windowed main.py
    
#### Or:

    python3 setup.py build
    
    
### Before compiling the files will look like this:

![Captura de tela de 2022-07-18 13-58-12](https://user-images.githubusercontent.com/79322362/179566764-2d5149fe-4425-45d6-a025-032d66251c7f.png)

### After compiling, 3 new files will appear:

![Captura de tela de 2022-07-18 14-16-32](https://user-images.githubusercontent.com/79322362/179566787-86690eba-0902-4be7-9d7f-620996c776b5.png)

### In the Dist folder will be the compiled file:

![Captura de tela de 2022-07-18 13-59-03](https://user-images.githubusercontent.com/79322362/179566803-b58c664b-bb25-4d49-8bb0-8fd5466123de.png)

### Clicking on it will open the program:


![Captura de tela de 2023-03-05 18-21-32](https://user-images.githubusercontent.com/79322362/222986752-2164afbc-f91f-4f25-b838-a3837bcfa50f.png)
