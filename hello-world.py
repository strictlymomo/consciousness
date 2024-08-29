
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter
from utils import save_transcript

formatter_JSON = JSONFormatter()
formatter_Text = TextFormatter()

video_id = "bhSlYfVtgww"

# Must be a single transcript.
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en-US'])
transcript_json = formatter_JSON.format_transcript(transcript, indent=2)
transcript_text = formatter_Text.format_transcript(transcript)

save_transcript(video_id, transcript_json, 'json')
save_transcript(video_id, transcript_text, 'txt')