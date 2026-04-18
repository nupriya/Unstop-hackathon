from moviepy.video.io.VideoFileClip import VideoFileClip

def generate_clips(video_path, segments):
    video = VideoFileClip(video_path)
    paths = []

    for i, seg in enumerate(segments):
        start = seg["start"]
        end = seg["end"]

        clip = video.subclip(start, end)

        output_path = f"temp/clip_{i}.mp4"
        clip.write_videofile(output_path)

        paths.append(output_path)

    return paths