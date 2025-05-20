import random

def recommend_tasks(mood):
    if mood == "Positive":
        return random.choice(["Go for a walk 🌿", "Study 1hr 📚", "Clean your room 🧹"])
    elif mood == "Negative":
        return random.choice(["Take a nap 😴", "Watch a comedy 😹", "Call a friend 💬"])
    else:
        return random.choice(["Meditate 5 mins 🧘", "Read something chill 📖", "Just breathe ❤️"])

def get_quote():
    return random.choice([
        "You got this 💪",
        "Small steps every day 🐾",
        "Your future self is proud of you 💖",
        "Don’t stop. The version of you you dream of needs this."
    ])
