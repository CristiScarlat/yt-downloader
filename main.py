from pytube import YouTube
import sys


def show_progress(stream, data, remaining_bytes):
    percentage = ((stream.filesize - remaining_bytes) / stream.filesize) * 100
    print(f'{round(percentage)}%')
    sys.stdout.write("\033[F")


def download(link):
    youtubeObject = YouTube(link, show_progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except Exception as error:
        print("An error has occurred", error)
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
download(link)
