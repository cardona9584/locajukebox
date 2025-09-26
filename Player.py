import pygame
import time
from pathlib import Path
import threading
import csv
import random 

# Initialize the pygame mixer (audio only)
pygame.mixer.init()

csv_file = r"C:\Users\scout\OneDrive\Desktop\Web Page\song_master.csv"  # Path to the CSV file

def load_playlist_from_csv(csv_file):
    """
    Load Playlist from a CSV
    """
    playlist = []
    try:
        with open(csv_file, newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # If the row is not empty
                    song_path = Path(row[1])  # First column as song path
                    if song_path.exists() and song_path.suffix in [".mp3", ".wav"]:
                        playlist.append(song_path)
                    else:
                        print(f"Invalid file: {song_path}")
    except FileNotFoundError:
        print(f"The CSV File Was Not Found '{csv_file}'Not Found")
    except Exception as e:
        print(f"Error Reading The File: {e}")
    return playlist

# Load playlist from the CSV file
playlist = load_playlist_from_csv(csv_file)

print(playlist)

if not playlist:
    print("not valid songs found")
    exit()

# Index for the current song

# Random Songs
random.shuffle(playlist)

current_song_index = 0
csv_file = r"C:\Users\scout\OneDrive\Desktop\Web Page\selections.csv"  # Route to CSV File

def validate_csv_for_song():
    """
    Validate and fetch a song from the selections CSV.
    """
    global current_song_index
    try:
        with open(csv_file, newline='', encoding="utf-8") as file:
            reader = list(csv.reader(file))  

        if len(reader) >= 2:  # At least 2 rows
            second_row = reader[1]  # Second Row
            if second_row:  # If there is a second row
                song_path = Path(second_row[0])  
                if song_path.exists() and song_path.suffix in [".mp3", ".wav"]:
                    print(f"Song founded: {song_path}")

                    # Delete Second Song and rewrite the file
                    with open(csv_file, mode="w", newline='', encoding="utf-8") as file:
                        writer = csv.writer(file)
                        writer.writerows(reader[:1] + reader[2:])  # Save except the second song

                    return song_path
    except FileNotFoundError:
        print("The CSV file was not found.")
    except Exception as e:
        print(f"Error reading or writing the CSV file: {e}")
    return None  # No valid song found in the CSV


def play_next_song():
    """
    Play the next song in the playlist.
    """
    global current_song_index
    try:
        csv_song = validate_csv_for_song()
        if csv_song:
            print(f"Playing song from CSV: {csv_song.name}")
            pygame.mixer.music.load(str(csv_song))
            pygame.mixer.music.play()
        elif current_song_index < len(playlist):
            print(f"Playing: {playlist[current_song_index].name}")
            song = str(playlist[current_song_index])
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            current_song_index += 1
        else:
            print("End of the playlist.")
            pygame.mixer.music.stop()
    except pygame.error as e:
        # Handle pygame related errors
        print(f"Error playing the song: {e}")
        print("Skipping to the next song...")
        current_song_index += 1
        play_next_song()  # Call the function again to continue
    except Exception as e:
        # Handle general errors
        print(f"Unexpected error: {e}")
        print("Skipping to the next song...")
        current_song_index += 1
        play_next_song() 

def user_input():
    """
    Wait for user input to control playback.
    """
    global current_song_index
    while True:
        command = input("Type 'n' to skip to the next song, or 'q' to quit: ").strip().lower()
        if command == 'n':
            pygame.mixer.music.stop()  # Stop the current song to skip to the next
            play_next_song()
        elif command == 'q':
            print("Exiting the player...")
            pygame.mixer.music.stop()
            exit()

# Start a thread to handle user input
input_thread = threading.Thread(target=user_input, daemon=True)
input_thread.start()

# Play the first song
play_next_song()

try:
    # Keep the script running by checking if the music is still playing
    while True:
        if not pygame.mixer.music.get_busy():
            play_next_song()
        time.sleep(1)

except KeyboardInterrupt:
    print("Playback manually stopped.")
    pygame.mixer.music.stop()
    pygame.mixer.music.stop()