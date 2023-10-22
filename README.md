# Useful-tools-from-Volin
Here we will collect useful self-written utilities for automating work with code, the main language in which all this is written is Python

In the future I will add useful utilities in list format, the list will be updated in the process of adding new software products

# Auto lib's loader

[Tab here, to see auto lib's loader programm](https://github.com/VolinNilov/Useful-tools-from-Volin/tree/main/Auto%20Lib%20Loader)

This code allows you to automatically download the necessary libraries through the Python programming language's PIP package manager. The list of required libraries is given in the file "requirements.txt". This code is intended for fast and automatic deployment of already existing program code on a new device, utomating the process of downloading the necessary libraries through the PIP package manager.

Instructions for use:

After downloading the file ```auto_loader.py```, you need to create a new file with a .txt extension and the name "requirements" in the directory where you installed this file (it should be "requirements.txt"), or change the name for this file to your own in the program code, in term 17, ```with open('file_name.txt', 'r') as f:```. After that it is enough to enter into the file ```file_name.txt``` the names of libraries you need and everything is ready! _(Each library must be specified on a new line)_

Now you only need to add the following lines in your main file, which should be created in the same directory as ```auto_loader.py``` and ```file_name.txt```: 

```
# auto lib's loader
from auto_loader import loader_start
loader_start()
```

The magic has happened, you will now have all the libraries you need automatically loaded!


# Youtube Video Downloader

[Tab here, to see youtube video downloader programm](https://github.com/VolinNilov/Useful-tools-from-Volin/tree/main/YouTube%20Downloader)

In this script you will get the ability to download videos from youtube by entering only the link to the video in the command line. 
