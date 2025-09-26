# 🎵 Local Music Queue Server over Windows Hotspot

A Flask-based local web server that allows devices connected to a Windows hotspot to browse and add songs to a shared playlist queue. It prevents duplicate entries and displays the number of songs currently waiting in the queue. Ideal for collaborative listening sessions at home or small gatherings.

---

## 🚀 Features

- 📡 Accessible to all devices connected to your Windows hotspot.
- 🎶 Displays a list of available songs from a CSV-based master list.
- ➕ Allows users to add songs to a shared playlist queue.
- 🚫 Prevents duplicate entries in the queue.
- 📊 Displays real-time count of pending songs in the playlist.
- 💾 Saves the queue to a CSV file for persistence.

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **HTML/CSS (Jinja templates)**
- **CSV files for data storage**

---

## 📁 Project Structure

project/
│
├── app.py # Flask server
├── templates/
│ └── form.html # Web UI for selecting songs
├── song_master.csv # Master list of available songs
└── selections.csv # Queue of selected songs

yaml
Copy code

---

## ⚙️ How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/music-queue-server.git
cd music-queue-server
Install dependencies:

bash
Copy code
pip install flask
Update file paths in app.py to match your local directory structure (for song_master.csv and selections.csv).

Run the server:

bash
Copy code
python app.py
Access the server from any device connected to your hotspot at:

cpp
Copy code
http://192.168.137.1:5000/
📋 Notes
Make sure the host PC is sharing internet via a Windows Hotspot.

The host IP (192.168.137.1) is the default for Windows hotspots. You can verify it using ipconfig.

The song_master.csv file must contain at least two columns: an ID and a song name.

🧪 Example song_master.csv
vbnet
Copy code
ID,Song Name
001,Bohemian Rhapsody
002,Hotel California
003,Take On Me
📄 License
This project is open-source and available under the MIT License.

🤝 Contributions
Pull requests and suggestions are welcome! Feel free to fork this repo and propose improvements.
