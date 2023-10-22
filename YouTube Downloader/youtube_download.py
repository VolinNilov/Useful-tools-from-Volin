import yt_dlp

'''
Ru: Вводим через терминал ссылку на видео
Eng: Enter the video link through the terminal
'''
url = input('Enter the link for the video: ') 

def download(url):
    '''
    Ru: Опции для скачивания. По умолчанию стоит формат скачки 'mp4', его можно поменять, но советую оставить этот формат
    Eng: Options for downloading. The default download format is 'mp4', you can change it, but I advise you to keep this format
    '''
    ydl_opts = {
        'format': 'mp4'
    }

    '''
    Ru: Открываем контектстный менеджер и начинаем скачивание нашего видео
    Eng: Open the content manager and start downloading our video.
    '''
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

'''
Ru: Вызов функции скачивания видео
Eng: Calling the video download function
'''
download(url)