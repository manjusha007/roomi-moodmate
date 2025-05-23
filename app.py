# Updated app.py with Roomi Asks answer and feedback storage
import streamlit as st
import datetime
import pandas as pd
import random
from music import get_playlist
import os

st.set_page_config(page_title="Roomi – Your MoodMate", layout="centered")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    .stApp {
        background: linear-gradient(to right top, #1a1a2e, #16213e);
        font-family: 'Poppins', sans-serif;
        color: #f1f1f1;
        padding: 1rem;
    }

    h1, h2, h3 {
        color: #ff4ecb;
        font-weight: 700;
    }

    .stTextInput > div > div > input,
    .stTextArea > div > textarea {
        background-color: #2c2c54;
        border: 1px solid #ff4ecb;
        border-radius: 10px;
        padding: 12px;
        color: #ffffff;
    }

    label {
        color: #ffffff !important;
        font-weight: 500;
        text-shadow: 0 0 5px #ffffffaa, 0 0 10px #ff4ecb55;
    }

    .stButton > button {
        background-color: #ff4ecb;
        color: #0f0f1f;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px 18px;
        border: none;
        box-shadow: 0 0 8px #ff4ecb88;
        transition: all 0.3s ease-in-out;
    }

    .stButton > button:hover {
        background-color: #e03baf;
        transform: scale(1.05);
        box-shadow: 0 0 12px #ff4ecb;
    }

    iframe {
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(255, 78, 203, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🧠 Mood Detector
def analyze_mood(text):
    mood_keywords = {
        "Positive": ["happy", "excited", "great", "love", "fun", "joy", "grateful"],
        "Negative": ["sad", "tired", "angry", "upset", "cry", "depressed"],
        "Anxious": ["anxious", "worried", "nervous", "panic", "stressed"],
        "Heartbroken": ["heartbroken", "breakup", "alone", "rejected"],
        "Motivated": ["motivated", "confident", "driven", "focused"],
        "Bored": ["bored", "nothing", "dull", "lazy"],
        "Neutral": ["okay", "fine", "normal", "meh"]
    }
    text = text.lower()
    mood_scores = {m: sum(word in text for word in words) for m, words in mood_keywords.items()}
    mood = max(mood_scores, key=mood_scores.get)
    return mood if mood_scores[mood] > 0 else "Neutral"

# 🎶 Music Player
def music_ui(mood):
    playlist = get_playlist(mood)
    if "song_index" not in st.session_state:
        st.session_state.song_index = 0

    st.markdown(f"🎵 **Roomi suggests this video for your mood:** *{mood}*")
    current_song = playlist[st.session_state.song_index]
    st.markdown(f'<iframe width="300" height="170" src="{current_song}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⏮️ Prev"):
            st.session_state.song_index = (st.session_state.song_index - 1) % len(playlist)
    with col2:
        if st.button("⏭️ Next"):
            st.session_state.song_index = (st.session_state.song_index + 1) % len(playlist)

# 📔 Diary Feature
def diary_ui():
    st.subheader("📔 Roomi's Mood Diary")
    thought = st.text_area("What are you feeling right now?")
    if st.button("💾 Save to Diary"):
        diary_log = {
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "entry": thought
        }
        pd.DataFrame([diary_log]).to_csv("diary_log.csv", mode='a', header=not os.path.exists("diary_log.csv"), index=False)
        st.success("Saved to your diary 📘")

    if os.path.exists("diary_log.csv"):
        st.markdown("---")
        st.markdown("### 📚 Your Previous Entries")
        entries = pd.read_csv("diary_log.csv", names=["time", "entry"])
        for _, row in entries.iterrows():
            st.markdown(f"**{row['time']}** 🕒")
            st.markdown(f"- {row['entry']}")

# ✨ Daily Quote Generator
def feel_good_quote():
    quotes = [
        "You are stronger than you think 💪",
        "Even the darkest night will end and the sun will rise 🌞",
        "Your feelings are valid and you're doing great 💖",
        "Keep going, beautiful soul 💫",
        "One breath at a time. You've got this. 🫶"
    ]
    st.markdown("---")
    st.markdown(f"💌 **Daily Uplift:** *{random.choice(quotes)}*")

# 🧩 Roomi Asks with Answer
ROOMI_QUESTIONS = [
    "What’s one small thing that made you smile today?",
    "If your mood had a color, what would it be? 🎨",
    "Who would you send a virtual hug to right now?",
    "Describe your current mood in a 3-word movie title.",
    "If you had a superpower today, what would it be? 💫"
]

def interactive_prompt():
    st.markdown("---")
    if "roomi_question" not in st.session_state:
        st.session_state.roomi_question = random.choice(ROOMI_QUESTIONS)

    question = st.session_state.roomi_question
    st.markdown(f"💬 **Roomi Asks:** {question}")
    user_answer = st.text_area("Your answer:")

    if st.button("✨ Submit Answer"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        feedback = {
            "time": timestamp,
            "question": question,
            "answer": user_answer
        }
        pd.DataFrame([feedback]).to_csv("roomi_answers.csv", mode='a', header=not os.path.exists("roomi_answers.csv"), index=False)
        st.success("✨ Roomi says: That’s such a thoughtful answer! 💕")

    if os.path.exists("roomi_answers.csv"):
        st.markdown("---")
        st.markdown("### 💌 Roomi's Fanbook")
        answers = pd.read_csv("roomi_answers.csv", names=["time", "question", "answer"])
        for _, row in answers.tail(3).iterrows():
            st.markdown(f"🕒 {row['time']} – *{row['question']}*")
            st.markdown(f"💖 _{row['answer']}_")

# ✨ Main Layout
st.title("🏠 Roomi – Your MoodMate")
tab1, tab2 = st.tabs(["🧠 Mood Vibes", "📔 Mood Diary"])

with tab1:
    user_input = st.text_input("Tell me how you're feeling:")
    if user_input:
        mood = analyze_mood(user_input)
        st.success(f"✨ You're feeling **{mood}**!")
        music_ui(mood)
        feel_good_quote()
        interactive_prompt()

with tab2:
    diary_ui()

# Footer
st.markdown("---")
st.caption("Made with 💖 by Roomi. Stay strong, stay soft.")