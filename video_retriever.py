import hashlib
import sys
import cv2
import os
import numpy as np
import signal
from yt_dlp import YoutubeDL

OUTPUT_FOLDER = "./frames"

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


ydl_search_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "quiet": True,  # Suppress console output for cleaner execution
    "geturl": True,  # Get the direct URL instead of downloading
}

ydl_video_opts = {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "quiet": True,  # Suppress console output for cleaner execution
    "noplaylist": True,  # Do not download playlists
}


# Handle broken pipe gracefully
def signal_handler(signum, frame):
    sys.exit(0)


signal.signal(signal.SIGPIPE, signal_handler)

ydl = YoutubeDL(ydl_search_opts)

videos = ydl.extract_info(
    f"ytsearch{10}:high school {sys.argv[1]} game stream", download=False
)

video_urls = []

for video in videos["entries"]:
    try:
        videoDL = YoutubeDL(ydl_video_opts)
        video_info = videoDL.extract_info(video["webpage_url"], download=False)

        # Extract stream URLs from formats - only 720p mp4
        formats = video_info["formats"]
        video_720p_mp4 = next(
            (
                fmt
                for fmt in formats
                if fmt["height"] == 720
                and fmt["ext"] == "mp4"
                and fmt["vcodec"] != "none"
            ),
            None,
        )

        if video_720p_mp4:
            video_urls.append(video_720p_mp4["url"])
        else:
            print(
                f"No 720p MP4 format found for {video['webpage_url']}", file=sys.stderr
            )
    except Exception as e:
        print(
            f"Error processing video {video.get('webpage_url', 'unknown')}: {e}",
            file=sys.stderr,
        )
        continue

url_encoding = ""
for url in video_urls:
    url_encoding += url + "|"

try:
    if url_encoding:
        print(url_encoding, end="", flush=True)
    else:
        print("No video URLs found", file=sys.stderr)
        sys.exit(1)
except (BrokenPipeError, KeyboardInterrupt):
    # Handle broken pipe gracefully when C++ program terminates early
    sys.exit(0)
