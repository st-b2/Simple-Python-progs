from pytube import YouTube

URL = 'https://youtube.com/'
DOWLOAD_DIRECRORY = 'Downloads'

def download_video(url):
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download(DOWLOAD_DIRECRORY) #HD

if __name__=='__main__':
    download_video(URL)

