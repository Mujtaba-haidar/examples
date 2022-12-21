import pytube
print('download your video ')
url =input('enter video url:')
pytube.YouTube(url).streams.get_lowest_resolution().download('ex15-download.py')
