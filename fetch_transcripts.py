from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = {
    "jay-schwedelson-b2b-email-tips": "OehFi1JcIIo",
    "jay-schwedelson-email-subject-lines": "Jg41i6qzFRM",
    "exit-five-email-teardown-2024": "1z0NHIa0sO4",
    "jay-schwedelson-email-personalization": "moejF39TrKM"
}

output_dir = "research/youtube-transcripts"
os.makedirs(output_dir, exist_ok=True)

for name, video_id in videos.items():
    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
        text = "\n".join([entry.text for entry in transcript])
        with open(f"{output_dir}/{name}.md", "w", encoding="utf-8") as f:
            f.write(f"# Transcript: {name}\n\n")
            f.write(f"Source: https://www.youtube.com/watch?v={video_id}\n\n")
            f.write("## Full Transcript\n\n")
            f.write(text)
        print(f"✓ Saved: {name}")
    except Exception as e:
        print(f"✗ Failed: {name} → {e}")

print("Done!")
