sports=("soccer" "basketball" "tennis", "football", "volleyball", "baseball", "hockey", "swimming", "golf", "tennis")

for sport in "${sports[@]}"; do
    python3 video_retriever.py "$sport" | ./frame_extractor/FrameExtractor
done
