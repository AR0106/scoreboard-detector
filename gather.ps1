# Extremely minimal PowerShell gather script
# Usage: Run this from the project root in PowerShell.
# For each sport, run: python ./video_retriever.py {sport} | ./frame_extractor/build/Debug/FrameExtractor.exe

$sports = @(
    'soccer', 'basketball', 'tennis', 'football', 'volleyball',
    'baseball', 'hockey', 'swimming', 'golf'
)

foreach ($sport in $sports) {
    Write-Host "Processing: $sport"
    # Note: use the project's python on PATH and the FrameExtractor executable at the expected path
    python './video_retriever.py' $sport | & 'frame_extractor\build\Debug\FrameExtractor.exe'
    Write-Host "Finished: $sport"
}
