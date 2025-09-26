from flask import Flask, request, render_template, jsonify
import csv
import os

app = Flask(__name__)

# Path to the master values file
master_csv = r'C:\Users\scout\OneDrive\Desktop\Web Page\song_master.csv'  # Change the path as needed

# Path to save the selections
selections_csv = r'C:\Users\scout\OneDrive\Desktop\Web Page\selections.csv'

# Function to load the master values into a dictionary
def load_master_values(csv_file):
    """
    Loads the master values from a CSV file.
    """
    master_values = {}
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header
            for row in reader:
                if len(row) >= 2:  # Ensure there are at least two columns
                    master_values[row[0]] = row[1]
    except FileNotFoundError:
        print(f"The master file '{csv_file}' was not found.")
    except Exception as e:
        print(f"Error reading the master file: {e}")
    return master_values

# Load master values when the server starts
master_values = load_master_values(master_csv)

# Route to display the form
@app.route('/')
def index():
    return render_template('form.html')  # Make sure to create this file in a "templates" folder

# Route to save the data in a CSV file
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    selected_item = data.get('selectedItem')

    # Check if the file already exists
    file_exists = os.path.isfile(selections_csv)

    # Read existing data to avoid duplicates
    existing_pairs = set()
    if file_exists:
        with open(selections_csv, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header
            for row in reader:
                if row:
                    existing_pairs.add((row[0], row[1]))  # Add existing pairs to the set

    # Get the corresponding value from the master
    corresponding_value = master_values.get(selected_item)

    if corresponding_value:
        # Check if the pair already exists in the file
        if (corresponding_value, selected_item) in existing_pairs:
            return jsonify({'message': f'The song "{selected_item}" already exists in the list. No duplicate added.'})

        # Write the data to the CSV file
        with open(selections_csv, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # If the file did not exist, write the header
            if not file_exists:
                writer.writerow(['Master Value','Selected Item'])
            # Write the corresponding pair
            writer.writerow([corresponding_value,selected_item])

        
        total_items = 0
        with open(selections_csv, mode='r', encoding='utf-8') as file:
            total_items = sum(1 for _ in file) - 1  # -1 to avoid header

        return jsonify({
            'message': f'The song "{selected_item}" was correctly added. Songs in Playlist: {total_items}.'
        })
    else:
        return jsonify({'message': f'The element "{selected_item}" does not have an associated value in the master songs file.'})
    

if __name__ == '__main__':
    app.run(host='192.168.137.1', port=5000, debug=True)