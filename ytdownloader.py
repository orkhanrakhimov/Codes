from pytube import YouTube

# video URL
video_url = input("Enter the YouTube video URL: ")

yt = YouTube(video_url)

print("Title: ", yt.title)
print("Views: ", yt.views)

# highest resolution
yd = yt.streams.get_highest_resolution()

# download path 
download_path = "C:/Users/PC/Desktop/ytdownloads"

# Download video
yd.download(download_path)

print("Download completed!")
