from pytube import Playlist
py=Playlist("https://www.youtube.com/watch?v=XKw2cyfvXRs&list=PLjVLYmrlmjGfhrXt_Kb6liQh2yzkcaPMi")
print(f'Downloading: {py.title}')
for video in py.videos:
    video.streams.first().download()
print("Downloaded")