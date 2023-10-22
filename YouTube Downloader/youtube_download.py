import yt_dlp

url = input() # ссылка на вход

def download(url):
    ydl_opts = {
        'format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download(url)