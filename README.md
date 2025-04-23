# AimLab-OpenCV

📘 [中文版](/docs/README.zh.md)

An AimLab aiming assistant tool based on OpenCV.

## Table of Contents  
[TOC]

## Features

This project uses image recognition and automated control to assist aiming in AimLab:

- Automatically detects targets  
- Automatically moves the mouse to aim  
- Supports manual start and timed stop  

⚠️ **Disclaimer**: This project is for educational and research purposes only. Use is only permitted in offline mode. Do not use for any form of cheating. Use at your own risk.

## Requirements

- OS: Windows  
- Game Platform: AimLab  
- Python: >= 3.8  

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Open a terminal in the project root directory and run:

   ```bash
   python main.py
   ```

2. Launch AimLab and select a map you want to play.

3. Focus the Scream or Mask window, then press the `s` key. Auto-aiming will start after 3 seconds.
