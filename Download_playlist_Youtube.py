from pytube import Playlist

plink = Playlist("https://www.youtube.com/watch?v=4Z4hEq7hyC8&list=PLjVLYmrlmjGdqdwNZvre2yPI6n5LyQ5M9")

print(f"DOWNLOADING: {plink.title}\n")

for video in plink.videos:
    ch = int(input("Want to download[1/0]: "))
    if(ch == 0):
        print("Download unsuccessfull")
        exit(0)

    video.streams.get_highest_resolution().download()

print("Download complet successfully ...")

'''
# process 2

from pytube import Playlist

plink = Playlist("https://www.youtube.com/watch?v=4Z4hEq7hyC8&list=PLjVLYmrlmjGdqdwNZvre2yPI6n5LyQ5M9")

print(f"PlayList name: {plink.title}")

for i,video in enumerate(plink.videos):
     print(i,video.title)


choose = int(input("Enter option: "))

for i,video in enumerate(plink.videos):
    if(i==choose):
         video.streams.get_highest_resolution().download()
         break
print("Download successfully: ",{video.title})

'''