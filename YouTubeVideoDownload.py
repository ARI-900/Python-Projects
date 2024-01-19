from pytube import YouTube

link = "https://www.youtube.com/watch?v=J7ck984Qhso&list=RDUDVtMYqUAyw&index=2"
Youtube_1 = YouTube(link)

print(Youtube_1.title)
print(Youtube_1.thumbnail_url)

videos = Youtube_1.streams.filter(only_video=True)

# videos = Youtube_1.streams.filter(only_audio=True)
# videos = Youtube_1.streams      # this show .all()

tubelist = list(enumerate(videos))  # tubelist is variable

for i in tubelist:
    print(i)

print() #privide space

streamIndex = int(input("Enter Index Number: "))

videos[streamIndex].download()

print("Video Download Successfully ...")
