from pytube import YouTube
link="https://www.youtube.com/watch?v=OKuiyX5k6zg&t=10188s"
yt=YouTube(link)
print(yt.title)
print(yt.thumbnail_url)
video=yt.streams
vid=list(enumerate(video))
for i in vid:
    print(i)
print()
stream= int(input("Enter the straming Choice:"))
video[stream].download()
print("Downloaded Successfully")