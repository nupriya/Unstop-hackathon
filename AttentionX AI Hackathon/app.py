import streamlit as st
import os

from utils.audio import extract_audio, transcribe_with_timestamps
from utils.viral_ai import compute_viral_score
from utils.clips import generate_clips
from utils.captions import generate_caption
from utils.analytics import plot_emotional_timeline
from utils.smart_crop import smart_vertical_crop

# Page setup
st.set_page_config(page_title="AttentionX AI", layout="wide")

st.title("🔥 AttentionX – Viral Content Engine")

# Ensure temp folder exists
os.makedirs("temp", exist_ok=True)

# Upload video
uploaded_file = st.file_uploader("Upload long-form video", type=["mp4"])

if uploaded_file:

    video_path = f"temp/{uploaded_file.name}"

    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.video(video_path)

    if st.button("🚀 Generate Viral Clips"):

        with st.spinner("Analyzing video..."):

            # 🎧 Extract audio + transcript
            audio_path = extract_audio(video_path)
            segments = transcribe_with_timestamps(audio_path)

            # 🧠 Full transcript
            full_text = " ".join([seg["text"] for seg in segments])

            st.subheader("🧠 Full Transcript")
            st.write(full_text)

            # ⏱️ Timestamped transcript
            st.subheader("⏱️ Timestamped Transcript")
            for seg in segments:
                st.write(
                    f"[{round(seg['start'],1)}s - {round(seg['end'],1)}s] {seg['text']}"
                )

            # 🔥 Viral ranking (FIXED)
            ranked = sorted(
                [(compute_viral_score(s), s) for s in segments],
                key=lambda x: x[0],
                reverse=True
            )[:3]

            top_segments = [r[1] for r in ranked]
            scores = [r[0] for r in ranked]

            # 📊 Emotional timeline
            all_scores = [compute_viral_score(s) for s in segments]
            chart = plot_emotional_timeline(segments, all_scores)
            st.subheader("📊 Emotional / Viral Peaks")
            st.image(chart)

            # ✂️ Generate clips
            clips = generate_clips(video_path, top_segments)

            # 🎯 Smart vertical crop
            final_clips = []
            for c in clips:
                new_path = c.replace(".mp4", "_vertical.mp4")
                final_clips.append(smart_vertical_crop(c, new_path))

        st.success("✅ Done! Viral clips generated")

        # 🎬 Display results
        for i, clip in enumerate(final_clips):
            st.subheader(f"🔥 Viral Clip {i+1}")
            st.video(clip)

            # 💬 Hook
            caption = generate_caption(top_segments[i]["text"])
            st.write("💬 Hook:", caption)

            # 🔥 Score
            st.metric("🔥 Viral Score", round(scores[i], 2))