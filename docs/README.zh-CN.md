
# AimLab-AutoAim-Py

<div align="center">
  <img src="https://github.com/carboxylBase/AimLab-opencv/blob/main/docs/assets/AimLab-AutoAim-icon.png" alt="icon" style="width:50%;">
</div>

📘 [English version](../README.md)

基于 OpenCV 和 Python 的 AimLab 自动瞄准工具.

本项目受 [Holo-Spice/Aimlab](https://github.com/Holo-Spice/Aimlab) 启发开发, 感谢原作者的思路与贡献.

## 目录
- [功能介绍](#功能介绍)
- [环境要求](#环境要求)
- [安装依赖](#安装依赖)
- [使用教程](#使用教程)

## 功能介绍

本项目通过图像识别与自动操作, 辅助用户在 AimLab 游戏中进行瞄准:

- 自动识别目标  
- 自动移动鼠标进行瞄准与射击  
- 支持手动启动与定时停止  

当前版本仅支持识别蓝色球体, 擅长静态目标的高效率、高精度瞄准. 在 "六小球" 模式中取得了 35w 分的成绩.  

由于 Python 性能的限制,动态目标的瞄准效果并不理想,目前已暂停对此功能的进一步开发.

⚠️ 免责声明: 本项目仅供学习与研究使用, 仅可用于离线模式, 请勿用于任何形式的作弊行为, 使用风险自负.

## 环境要求

- 操作系统: Windows  
- 游戏平台: AimLab  
- Python: >= 3.8  

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用教程

1. 在项目根目录打开终端, 输入以下命令:
    ```bash
    python main.py
    ```

2. 在终端中选择模式: 输入 `1` (静态瞄准) 或 `2` (动态瞄准).

3. 打开 AimLab, 选择任意地图.

4. 按下 `s` 键开始自动瞄准, 按下 `e` 键结束自动瞄准.
