sports=("soccer" "basketball" "tennis" "football" "volleyball" "baseball" "hockey" "swimming" "golf" "tennis")

for sport in "${sports[@]}"; do
    echo "Processing sport: $sport"
    python3 ./video_retrieval.py "$sport" | ./frame_extractor/FrameExtractor &
    echo "Finished processing sport: $sport"
done

wait
echo "All sports processed."