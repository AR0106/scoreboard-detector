import hashlib
import cv2
import os
import numpy as np
from yt_dlp import YoutubeDL

OUTPUT_FOLDER = "./frames"

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


def extract_frames(video_url):
    print(f"Extracting frames from video {video_url}")
    video = cv2.VideoCapture(video_url)

    video_prefix = hashlib.md5(video_url.encode()).hexdigest()

    frame_num = 0
    while True:
        rand = np.random.default_rng().integers(1, 10000)

        ret, frame = video.read()
        if not ret:
            break

        frame_num += 1

        if rand == 1:
            print(f"Extracting frame {frame_num}")
            frame_path = os.path.join(OUTPUT_FOLDER, f"{video_prefix}_{frame_num}.jpg")
            cv2.imwrite(frame_path, frame)

    print(f"Finished extracting frames from video {video_url}")
    video.release()


ydl_search_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "quiet": False,  # Suppress console output for cleaner execution
    "geturl": True,  # Get the direct URL instead of downloading
}

ydl_video_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "quiet": False,  # Suppress console output for cleaner execution
    "noplaylist": True,  # Do not download playlists
}

ydl = YoutubeDL(ydl_search_opts)

videos = ydl.extract_info(
    f"ytsearch{10}:{'high school football game stream'}", download=False
)

video_urls = []

for video in videos["entries"]:
    videoDL = YoutubeDL(ydl_video_opts)
    video_info = videoDL.extract_info(video["webpage_url"], download=False)

    # Extract stream URLs from formats - only 720p mp4
    formats = video_info["formats"]
    video_720p_mp4 = next(
        (
            fmt
            for fmt in formats
            if fmt["height"] == 720 and fmt["ext"] == "mp4" and fmt["vcodec"] != "none"
        ),
        None,
    )

    if video_720p_mp4:
        video_urls.append(video_720p_mp4["url"])
    else:
        print("No 720p MP4 formats available")

for url in video_urls:
    extract_frames(url)
