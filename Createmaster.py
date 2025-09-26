import os
import csv
import eyed3

# Path to the folder containing the music files
music_folder = r'E:\Music'  # <-- CHANGE THIS
output_file = r'C:\Users\scout\OneDrive\Desktop\Web Page\song_master.csv'

# Valid audio extensions (only mp3 in this case)
valid_extensions = ['.mp3']

# Open the output CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as output:
    writer = csv.writer(output)
    writer.writerow(['name', 'file path'])

    # Traverse through all files in the folder and subfolders
    for root, _, files in os.walk(music_folder):
        for file in files:
            full_path = os.path.join(root, file)
            name, extension = os.path.splitext(file)

            # Only process mp3 files
            if extension.lower() not in valid_extensions:
                continue

            # Load the audio file using eyed3
            try:
                audio_file = eyed3.load(full_path)

                # Get the ID3 tag information
                artist = audio_file.tag.artist if audio_file.tag.artist else "Unknown"
                title = audio_file.tag.title if audio_file.tag.title else "Unknown"
                genre = str(audio_file.tag.genre) if audio_file.tag.genre else "Unknown"

                # Create the name-artist-genre format
                combined = f"{title.strip()}-{artist.strip()}-{genre.strip()}"

                # Write to the CSV
                writer.writerow([combined, full_path])
            except Exception as e:
                print(f"Error processing file {file}: {e}")

print(f"✅ CSV file generated: {output_file}")