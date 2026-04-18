import moviepy.editor as mp
import whisper

model = whisper.load_model("base")

def extract_audio(video_path, audio_path="temp/audio.wav"):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path

def transcribe_with_timestamps(audio_path):
    result = model.transcribe(audio_path)
    return result["segments"]