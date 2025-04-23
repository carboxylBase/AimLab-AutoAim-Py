# AimLab-OpenCV

📘 [English version](../README.md)

基于 OpenCV 的 AimLab 辅助瞄准工具.

## 目录
[TOC]

## 功能介绍

本项目通过图像识别与自动操作,辅助用户在 AimLab 游戏中进行瞄准:

- 自动识别目标  
- 自动移动鼠标瞄准  
- 支持手动启动与定时停止  

⚠️ **免责声明**:本项目仅用于学习与研究目的,只允许在离线模式使用,请勿用于任何形式的作弊行为,使用风险自负.

## 环境要求

- 操作系统: Windows
- 游戏平台: AimLab
- Python: >= 3.8  

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用教程
1. 在项目根目录打开终端,输入:
    ```bash
    python main.py
    ```
2. 打开 AimLab,选择一张想玩的地图.
3. 选中 Scream 或者 Mask 窗口,点击 s 键,3 秒钟之后开始自动瞄准.