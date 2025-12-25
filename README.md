#  File Sorter

A simple Python tool that automatically organizes files in a folder by moving them into categorized sub-folders such as Documents, Images, Videos, Audio, Archives, and Others.

This project keeps messy folders (like Downloads or Desktop) clean and organized and helped me practice Python automation.

##  Why I Built This
Folders quickly become messy when we download many files. I built this project to automatically organize files, save time, and practice file handling concepts in Python.

##  Features
 Detects file type using extension  
 Creates folders automatically  
 Works on any folder  
 Safe (moves files — does not delete)  
 Beginner-friendly Python project

##  Requirements
- Python 3.8 or higher

Check version:
python --version

##  Installation
Clone the repository and open the folder:

git clone https://github.com/Sushma-Anumalla/File.Sorter.git
cd File.Sorter

##  How to Run
Run the script:

python FileSort.py

(Optional) Run for a specific folder:

python FileSort.py "C:\Users\YourName\Downloads"

##  Example
Before sorting:
photo.jpg  
song.mp3  
report.pdf  
video.mp4  

After sorting:
Images/photo.jpg  
Audio/song.mp3  
Documents/report.pdf  
Videos/video.mp4  

##  What I Learned
- Working with files and folders in Python
- Using os and shutil modules
- Writing reusable functions
- Structuring a simple project professionally
- Creating documentation for GitHub

##  Contributing
Suggestions and improvements are welcome.

##  License
This project is open source. MIT License is recommended if others want to reuse it.

