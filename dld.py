from pytube import YouTube
import random
def download(link):
  #prompt
  iv = random.randint(1,9999999999)
  #link = input("Enter link to video you would like to download:  ")
  yt = YouTube(link)
  #get video
  video = yt.streams.get_highest_resolution()
  print("starting download...")
  #download
  video.download("downloads/",filename='download'+ str(iv) + ".mp4")
  print("Download finished!")
  return iv