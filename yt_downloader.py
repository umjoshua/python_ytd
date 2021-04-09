	# From terminal, pip install pytube
from pytube import YouTube

print("***Youtube Downloader***\n")

url=YouTube(input("Enter URL: "))
format = url.streams.filter(progressive=True).all()

index = list(enumerate(format))

for i in index:
    print(i)

opt = int(input("\nEnter video format (index): "))
vid = format[opt]

print("\nDownloading....\n")
vid.download()
print("***Download Successfull***\n")
