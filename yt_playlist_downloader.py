from pytube import Playlist

print("***Youtube Playlist Downloader***\n")

playlist=Playlist(input("Enter Playlist URL: "))
for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.filter(type='video', subtype='mp4', res='720p', progressive=True).\
        order_by('resolution').\
        desc().\
            first().\
                download()
