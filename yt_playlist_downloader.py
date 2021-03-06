from pytube import Playlist
from pytube import YouTube

print("***Youtube Playlist Downloader***\n")

playlist=Playlist(input("Enter Playlist URL: "))

for video in playlist.videos:
    url= YouTube(video.watch_url)
    format = url.streams.filter(progressive=True)
    index = list(enumerate(format))
    print('{} '.format(video.title))
    for i in index:
        print(i)
    opt = int(input("\nEnter video format (index), -1 to skip: "))
    vid = format[opt]
    if opt!=-1:
        print('Downloading : {} '.format(video.title))
        vid.download()
        print("***Download Successfull***\n")
    else:
        print("Download cancelled\n")

