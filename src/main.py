"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

# from recommender import load_songs, recommend_songs
from src.recommender import load_songs, recommend_songs
from src.recommender import consistency_test

def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # recommendations = recommend_songs(user_prefs, songs, k=5)

    # print("\nTop recommendations:\n")
    # for song, score, explanation in recommendations:
    #     print(f"🎵 {song['title']} by {song['artist']}")
    #     print(f"   Score: {score:.2f}")
    #     print(f"   Why: {explanation}")
    #     print("-" * 40)
    user_profiles = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
    "Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
    "Conflicting Vibe": {"genre": "pop", "mood": "sad", "energy": 0.9},
    }

    for name, prefs in user_profiles.items():
        print(f"\n=== {name} ===\n")

        # 🧪 CONSISTENCY TEST (NEW AI FEATURE)
        consistency_test(prefs, songs)

        recommendations = recommend_songs(prefs, songs, k=5)

        for song, score, explanation in recommendations:
            print(f"🎵 {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Why: {explanation}")
            print("-" * 40)


if __name__ == "__main__":
    main()
