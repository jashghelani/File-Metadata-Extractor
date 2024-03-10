# File-Metadata-Extractor
The File Metadata Extractor is a Python tool designed to facilitate digital forensic investigations by analyzing disk image files and extracting essential file metadata. This metadata includes file names, sizes, inodes, and timestamps, providing valuable insights into the contents and structure of the disk image.

Features
Extracts file metadata from disk image files
Analyzes file names, sizes, inodes, and timestamps
Utilizes the Sleuth Kit's fls command for forensic analysis
Supports various disk image formats, including raw image files and forensic disk images

Installation
Before using the File Metadata Extractor, ensure that Sleuth Kit is installed on your system. You can download and install Sleuth Kit from the official website or using package managers like apt, yum, or brew, depending on your operating system.

Once Sleuth Kit is installed, download or clone the file_metadata_extractor.py script to your local machine.

Usage
To use the File Metadata Extractor, follow these steps:

Open a terminal or command prompt.

Navigate to the directory containing the file_metadata_extractor.py script.

Run the script with the following command:

python file_metadata_extractor.py [image_path]
Replace [image_path] with the path to the disk image file you want to analyze.

The script will analyze the disk image file and extract file metadata. It will then display the extracted metadata, including file names, sizes, inodes, and timestamps, in the terminal.

Example
Suppose you have a disk image file named example_disk_image.dd containing various files. Running the File Metadata Extractor with this disk image file as input will display metadata for each file found within the image.

Sample command:

python file_metadata_extractor.py example_disk_image.dd

Disclaimer
The File Metadata Extractor is provided for educational and research purposes only. It is intended to assist digital forensic analysts in conducting investigations and analyzing disk images. Users are responsible for ensuring compliance with applicable laws and regulations regarding digital forensics and data privacy.

The authors of the File Metadata Extractor are not liable for any misuse or illegal activities resulting from its use.

Contributing
Contributions to the File Metadata Extractor are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to submit a pull request or open an issue on the GitHub repository.

License
The File Metadata Extractor is licensed under the MIT License.
