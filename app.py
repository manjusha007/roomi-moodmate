# # app.py
# import streamlit as st
# import datetime
# import pandas as pd
# from music import get_playlist

# st.set_page_config(page_title="Roomi – Your MoodMate", layout="centered")
# st.markdown(
#     """
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

#     .stApp {
#         background: linear-gradient(to right top, #1a1a2e, #16213e);
#         font-family: 'Poppins', sans-serif;
#         color: #f1f1f1;
#         padding: 1rem;
#     }

#     h1, h2, h3 {
#         color: #ff4ecb;
#         font-weight: 700;
#     }

#     .stTextInput > div > div > input,
#     .stTextArea > div > textarea {
#         background-color: #2c2c54;
#         border: 1px solid #ff4ecb;
#         border-radius: 10px;
#         padding: 12px;
#         color: #f1f1f1;
#     }

#     .stButton > button {
#         background-color: #ff4ecb;
#         color: #0f0f1f;
#         font-weight: 600;
#         border-radius: 10px;
#         padding: 10px 18px;
#         border: none;
#         box-shadow: 0 0 8px #ff4ecb88;
#         transition: all 0.3s ease-in-out;
#     }

#     .stButton > button:hover {
#         background-color: #e03baf;
#         transform: scale(1.05);
#         box-shadow: 0 0 12px #ff4ecb;
#     }

#     .stTabs [data-baseweb="tab"] {
#         background-color: #222244;
#         color: #f1f1f1;
#         font-size: 16px;
#         padding: 10px 18px;
#         border-radius: 10px 10px 0 0;
#         margin-right: 4px;
#     }

#     .stTabs [aria-selected="true"] {
#         background-color: #331a4a;
#         border-bottom: 3px solid #ff4ecb;
#         color: #ff4ecb;
#         font-weight: 600;
#     }

#     iframe {
#         border-radius: 10px;
#         box-shadow: 0 0 20px rgba(255, 78, 203, 0.3);
#     }

#     .stCaption {
#         font-size: 13px;
#         color: #bbbbbb;
#     }

#     .css-1aumxhk {
#         background-color: #2c2c54 !important;
#         border-radius: 10px !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )



# # 🧠 Mood Detector
# def analyze_mood(text):
#     mood_keywords = {
#         "Positive": ["happy", "excited", "great", "love", "fun", "joy", "grateful"],
#         "Negative": ["sad", "tired", "angry", "upset", "cry", "depressed"],
#         "Anxious": ["anxious", "worried", "nervous", "panic", "stressed"],
#         "Heartbroken": ["heartbroken", "breakup", "alone", "rejected"],
#         "Motivated": ["motivated", "confident", "driven", "focused"],
#         "Bored": ["bored", "nothing", "dull", "lazy"],
#         "Neutral": ["okay", "fine", "normal", "meh"]
#     }
#     text = text.lower()
#     mood_scores = {m: sum(word in text for word in words) for m, words in mood_keywords.items()}
#     mood = max(mood_scores, key=mood_scores.get)
#     return mood if mood_scores[mood] > 0 else "Neutral"

# # 🎶 Music Player with Back/Forth
# def music_ui(mood):
#     playlist = get_playlist(mood)
#     if "song_index" not in st.session_state:
#         st.session_state.song_index = 0

#     st.markdown(f"🎵 **Roomi suggests this track for your mood:** *{mood}*")
#     current_song = playlist[st.session_state.song_index]
#     st.markdown(f'<iframe src="{current_song.replace("track", "embed/track")}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

#     col1, col2 = st.columns([1, 1])
#     with col1:
#         if st.button("⏮️ Prev"):
#             st.session_state.song_index = (st.session_state.song_index - 1) % len(playlist)
#     with col2:
#         if st.button("⏭️ Next"):
#             st.session_state.song_index = (st.session_state.song_index + 1) % len(playlist)

# # 📔 Diary Feature
# def diary_ui():
#     st.subheader("📔 Roomi's Mood Diary")
#     thought = st.text_area("What are you feeling right now?")
#     if st.button("💾 Save to Diary"):
#         diary_log = {
#             "time": datetime.datetime.now(),
#             "entry": thought
#         }
#         pd.DataFrame([diary_log]).to_csv("diary_log.csv", mode='a', header=False, index=False)
#         st.success("Saved to your diary 📘")

# # ✨ Main Layout
# st.title("🏠 Roomi – Your MoodMate")
# tab1, tab2 = st.tabs(["🧠 Mood Vibes", "📔 Mood Diary"])

# with tab1:
#     user_input = st.text_input("Tell me how you're feeling:")
#     if user_input:
#         mood = analyze_mood(user_input)
#         st.success(f"✨ You're feeling **{mood}**!")
#         music_ui(mood)

# with tab2:
#     diary_ui()

# # Footer
# st.markdown("---")
# st.caption("Made with 💖 by Roomi.")




# app.py
import streamlit as st
import datetime
import pandas as pd
from music import get_playlist

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

    .stTabs [data-baseweb="tab"] {
        background-color: #222244;
        color: #f1f1f1;
        font-size: 16px;
        padding: 10px 18px;
        border-radius: 10px 10px 0 0;
        margin-right: 4px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #331a4a;
        border-bottom: 3px solid #ff4ecb;
        color: #ff4ecb;
        font-weight: 600;
    }

    iframe {
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(255, 78, 203, 0.3);
    }

    .stCaption {
        font-size: 13px;
        color: #bbbbbb;
    }

    .css-1aumxhk {
        background-color: #2c2c54 !important;
        border-radius: 10px !important;
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

    st.markdown(f"🎵 **Roomi suggests this track for your mood:** *{mood}*")
    current_song = playlist[st.session_state.song_index]
    st.markdown(f'<iframe src="{current_song.replace("track", "embed/track")}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

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
            "time": datetime.datetime.now(),
            "entry": thought
        }
        pd.DataFrame([diary_log]).to_csv("diary_log.csv", mode='a', header=False, index=False)
        st.success("Saved to your diary 📘")

# ✨ Main Layout
st.title("🏠 Roomi – Your MoodMate")
tab1, tab2 = st.tabs(["🧠 Mood Vibes", "📔 Mood Diary"])

with tab1:
    user_input = st.text_input("Tell me how you're feeling:")
    if user_input:
        mood = analyze_mood(user_input)
        st.success(f"✨ You're feeling **{mood}**!")
        music_ui(mood)

with tab2:
    diary_ui()

# Footer
st.markdown("---")
st.caption("Made with 💖 by Roomi.")
