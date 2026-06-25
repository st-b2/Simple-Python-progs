# 🐍 Python Scripts for automation

This repository contains a collection of simple but useful Python scripts for everyday tasks: downloading videos, converting images, speech recognition, working with files and logging, and etc.

---

## 📚 Table of Contents

- [📋 List of scripts](#-list-of-scripts)
  - [📥 Download-videos-from-YouTube](#-download-videos-from-youtube)
  - [📝 Generate-change-logs](#-generate-change-logs)
  - [📂 Rename-files](#-rename-files)
  - [🎤 WAV to Text Conversion](#-wav-to-text-conversion)
  - [🖼️ Image Conversion](#️-image-conversion)
- [🛠️ Installing dependencies](#️-installing-dependencies)

---

## 📋 Script List

### 📥 Downloading videos from YouTube

**File:** `dowload_videos_from_youtube.py`

A simple script for downloading videos from YouTube in maximum quality.

**How it works:**
- Accepts the URL of the video
- Downloads to the `Downloads` folder
- Uses the pytube library

**Usage:**
```python
# Change the URL in the script
URL = 'https://youtube.com/your_video_link'

# Run
python download_videos_from_youtube.py
```
**Dependencies**
```bash
pip install pytube
```

## 📝 Generation of change logs

**File:**`log_generation.py `

The script tracks file changes in the specified directory and writes them to a log file.

**How it works:**
- Scans all files in the directory (recursively)
- Checks the time of the last change (mtime, atime, ctime)
- If the file has been changed in the last 87,000 seconds (~24 hours), it writes to the log

**Usage:**
```bash
# Running with
the python directory specified log_generation.py D:\MyFolder

# Run with path request (interactive mode)
python log_generation.py
```
**Settings:**
```python
TIME_BORDER = 87000 # Tracking time (seconds)
CHECK_DIRECTORY = r'D:\PythonProjects '  # Default path
FILE_LOG = r'D:\PythonProjects\viruses\log.txt ' # Path to the log
```

### 📂 Renaming files

**File:**`rename_files.py `

Mass renaming of files according to a given rule.

**How it works:**
- Traverses through all files in the directory (recursively)
- Adds the A_ prefix to the file name if there is none.
- Replaces _Diff. on _BC

**Usage:**
```python
# Change the path in the script
DIRECTORY = r'D:\PythonProjects'

# Run
python rename_files.py
```
**Example:**
```text
Before: image_Diff.jpg
After: A_image_BC.jpg
```
### 🎤 WAV to text conversion

**File:** `conv_wav_to_txt.py`

Speech recognition from an audio file (WAV) using Google Speech Recognition.

**How it works:**
- Downloads a WAV file
- Sends it for recognition in Google Speech Recognition
- Returns the recognized text

**Usage:**
```python
# Change the path to the file in the script
FILE_PATH = 'audio.wav'
LANGUAGE = 'ru-RU' # Recognition language (ru-RU, en-EN)

# Run
python conv_wav_to_txt.py
```

**Dependencies:**
```bash
pip install SpeechRecognition pydub
```

**Saving the result to a file:**
```python
# Uncomment at the end of the script
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(result)
```

### 🖼️ Image Conversion

**File:** `convert_images.py`

Mass image conversion: format change, compression to a preset size.

**How it works:**
- Traverses through all files in the directory (recursively)
- Finds files with the extension .jpg
- Converts to .png
- Compresses to 1024x124 size (keeping the proportions)
- Deletes the original JPG file

**Usage:**
```python
# Change the settings in the script
DIRECTORY = r'D:\PythonProjects\test ' # Folder with images
FROM_EXTENTION = '.jpg' # Source format
TO_EXTENTION = '.png' # Target format
MAX_SIZE = (1024, 1024) # Maximum size

# Run
python convert_images.py
```

**Dependencies:**
```bash
pip install Pillow
```

**Saving the result to a file:**
```python
# Uncomment at the end of the script
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(result)
```
---
## 🛠️ Installing dependencies

**All dependencies with one command:**
```bash
pip install pytube SpeechRecognition Pillow pydub
```
