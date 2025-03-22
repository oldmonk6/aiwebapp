from youtube_transcript_api import YouTubeTranscriptApi
import os
from groq import Groq
import re

def extract_video_id(url):
    match = re.search(r"(?<=v=|/videos/|embed/|youtu.be/|/v/|/e/|watch\?v=|&v=|/shorts/)([^#&?]*)", url)
    return match.group(1) if match else None
def get_transcript(url):
    video_id=extract_video_id(url)
    if not video_id:
        return None
    try:
            transcript=YouTubeTranscriptApi(video_id)
            return " ".join([t["text"] for t in transcript])
    except Exception as e:
          return f"Error fetching transcript: {e}"

def generateblog(video_url):
    transcript=get_transcript(video_url)
    if not transcript:
        return {"message":"Invalid video URL"}
    client=Groq(os.getenv("openai_key"),)
    chat=client.chat.completions.create(
         messages=[
              {
            "role": "user",
            "content": f"Summarize this YouTube video into a blog:\n{transcript}"
        }
         ],
         model="llama-3.3-70b-versatile",
    )
    return chat.choices[0].message.content

  

