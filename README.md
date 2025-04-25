
# AimLab-AutoAim-Py

<div align="center">
  <img src="https://github.com/carboxylBase/Hzy-Photos/blob/main/AutoAim-icons/AutoAim-icons.png" alt="icon" style="width:50%;">
</div>

📘 [中文版](/docs/README.zh-CN.md)

An AimLab auto-aim tool based on OpenCV and Python.

This project is inspired by [Holo-Spice/Aimlab](https://github.com/Holo-Spice/Aimlab). Thanks to the original author for the ideas and contributions.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Install Dependencies](#install-dependencies)
- [Usage Guide](#usage-guide)

## Features

This project uses image recognition and automation to assist users in aiming within AimLab:

- Automatically recognizes targets  
- Automatically moves the mouse to aim and shoot  
- Supports manual start and scheduled stop  

The current version only supports recognizing blue spheres and excels at static target aiming with high efficiency and precision. It achieved a score of 350,000 in the "Six Balls" mode.  

Due to performance limitations in Python, aiming at dynamic targets is not ideal, and further development on this feature has been paused.

⚠️ **Disclaimer**: This project is for educational and research purposes only, and is only allowed for offline use. Please do not use it for any form of cheating. Use at your own risk.

## Requirements

- Operating System: Windows  
- Game Platform: AimLab  
- Python: >= 3.8  

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage Guide

1. Open a terminal in the project root directory and run the following command:
    ```bash
    python main.py
    ```

2. In the terminal, select a mode: input `1` (Static Aim) or `2` (Dynamic Aim).

3. Open AimLab and select any map.

4. Press the `s` key to start auto-aim, and press the `e` key to stop auto-aim.
