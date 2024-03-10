import os
import sys
import datetime
import subprocess

def extract_file_metadata(image_path):
    # Check if the disk image file exists
    if not os.path.exists(image_path):
        print("Error: Disk image file not found")
        return

    # Extract file metadata using the 'fls' command from Sleuth Kit
    try:
        fls_output = subprocess.check_output(["fls", "-p", "-r", image_path])
    except FileNotFoundError:
        print("Error: Sleuth Kit not found. Make sure it's installed and in your system PATH.")
        return

    # Parse the output to extract file metadata
    files = []
    for line in fls_output.splitlines():
        try:
            line = line.decode("utf-8")
        except UnicodeDecodeError:
            continue

        parts = line.split("|")
        if len(parts) >= 6:
            file_name = parts[5].strip()
            file_size = int(parts[3].strip())
            file_inode = parts[0].strip()
            file_timestamp = parts[1].strip()

            # Convert timestamp to a human-readable format
            try:
                timestamp = datetime.datetime.strptime(file_timestamp, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                timestamp = file_timestamp

            files.append({
                "name": file_name,
                "size": file_size,
                "inode": file_inode,
                "timestamp": timestamp
            })

    return files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_metadata_extractor.py [image_path]")
        sys.exit(1)

    image_path = sys.argv[1]
    metadata = extract_file_metadata(image_path)

    if metadata:
        print("File Metadata:")
        for file_data in metadata:
            print(f"Name: {file_data['name']}")
            print(f"Size: {file_data['size']} bytes")
            print(f"Inode: {file_data['inode']}")
            print(f"Timestamp: {file_data['timestamp']}")
            print("-" * 20)
    else:
        print("No file metadata found in the disk image.")
