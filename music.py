# Updated music.py with YouTube links
music_dict = {
    "Positive": [
        "https://www.youtube.com/embed/nfWlot6h_JM",  # Shake It Off – Taylor Swift
        "https://www.youtube.com/embed/qpgTC9MDx1o",  # Animals – Maroon 5
        "https://www.youtube.com/embed/wV1FrqwZyKw",  # Pretty Little Baby – Connie Francis
        "https://www.youtube.com/embed/68ugkg9RePc",  # Blue (Da Ba Dee) – Eiffel 65
        "https://www.youtube.com/embed/e-ORhEE9VVg",  # Blank Space – Taylor Swift
    ],
    "Negative": [
        "https://www.youtube.com/embed/V1Pl8CzNzCw",  # Lovely – Billie Eilish
        "https://www.youtube.com/embed/50VNCymT-Cs",  # Let Me Down Slowly – Alec Benjamin
        "https://www.youtube.com/embed/7MAp3D3VPAw",  # I Can Do It With a Broken Heart – Taylor Swift (Fan Vid)
    ],
    "Neutral": [
        "https://www.youtube.com/embed/mRD0-GxqHVo",  # Heat Waves – Glass Animals
        "https://www.youtube.com/embed/RBumgq5yVrA",  # Let Her Go – Passenger
        "https://www.youtube.com/embed/DyDfgMOUjCI",  # Bad Guy – Billie Eilish
    ],
    "Anxious": [
        "https://www.youtube.com/embed/hLQl3WQQoQ0",  # Someone Like You – Adele
        "https://www.youtube.com/embed/kNKu1uNBVkU",  # Rise Up – Andra Day
        "https://www.youtube.com/embed/6sAQ9W3nZCo",  # Weightless – Marconi Union
        "https://www.youtube.com/embed/OsUFgUxm5bY?si=JT5eOl7QriUmu3Kp", #pretty little baby -chris
        "https://www.youtube.com/embed/riCP9x31Kuk?si=clk7yGlPVPn29AOR", #anxiety - doechii

    ],
    "Heartbroken": [
        "https://www.youtube.com/embed/zpzdgmqIHOQ",  # Lose You To Love Me – Selena Gomez
        "https://www.youtube.com/embed/J6zwL7s8w5I",  # Back to December – Taylor Swift
        "https://www.youtube.com/embed/5rOiW_xY-kc",  # Someone Like You – Adele
    ],
    "Motivated": [
        "https://www.youtube.com/embed/7wtfhZwyrcc",  # Believer – Imagine Dragons
        "https://www.youtube.com/embed/3AtDnEC4zak",  # Stronger – Kanye West
        "https://www.youtube.com/embed/btPJPFnesV4",  # Eye of the Tiger – Survivor
    ],
    "Bored": [
        "https://www.youtube.com/embed/q0hyYWKXF0Q",  # Dance Monkey – Tones and I
        "https://www.youtube.com/embed/7wtfhZwyrcc",  # Believer – Imagine Dragons
        "https://www.youtube.com/embed/fLexgOxsZu0",  # Happy – Pharrell Williams
        ""
    ]
}

def get_playlist(mood):
    return music_dict.get(mood, music_dict["Positive"])
