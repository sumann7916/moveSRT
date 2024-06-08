# Move Subtitle Files to Matching Folders

This script monitors a specified directory for new `.srt` files and automatically moves them to the most appropriate folder in another specified directory. It uses `inotifywait` to efficiently watch for file creation events.

Created because made it easier if the files were in respective folder as most of the times i needed to downlad the SRT file separately.

## Prerequisites

- Python 3.x
- `inotify-tools`

## Installation

### Install `inotify-tools`

```bash
sudo apt-get update
sudo apt-get install inotify-tools

crontab -l
and insert the script so that it starts on reboot
@reboot /path/to/python/script  /path/to/folder/where/srt/file/downloaded /path/to/movies/folder

```
