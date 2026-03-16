# 🚀 Ubuntu 全能性能评估系统 (v5.0)

[![AI-Collaborated](https://img.shields.io/badge/AI-Collaborated-blueviolet?style=for-the-badge&logo=openai)](https://github.com/kkfreedom/ubuntu-benchmark-script)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[English](./README.md)

---

一款基于 Python 开发的专业、美观、全方位的 Ubuntu 服务器性能评估工具。特别优化了在**分流代理/透明代理**环境下的网络探测与测速功能。

## 🤖 AI 协作声明
> **Note**
> 本项目由 **kkfreedom** 与 **Gemini CLI (AI 智能助手)** 深度协作完成。AI 负责了核心代码架构设计、网络分流逻辑优化以及终端 UI 美化。

## ✨ 核心特性

- 💻 **硬件全扫描**：一键获取 CPU 型号、核心数、线程数及内存总量。
- ⚡ **算力压测**：通过高精度圆周率 (Pi) 运算评估 CPU 单核性能。
- 💾 **IO 吞吐测试**：真实的磁盘同步写入与顺序读取速度实测。
- 🌐 **分流深度探测**：
    - 针对**透明代理/路由器分流**环境设计。
    - 对比国内 (3322.org) 与国外 (ifconfig.me) 出口 IP，实时验证分流规则。
- 🚀 **智能全链路测速**：基于 `speedtest-cli` 自动匹配当前环境下响应最快的服务器节点。
- 🎨 **极致终端美化**：采用 `rich` 库构建，支持动态进度条、嵌套面板和彩色汇总表格。

## 🛠️ 安装与运行

### 环境准备
确保您的系统中已安装 Python3：
```bash
sudo apt update && sudo apt install -y python3-pip
```

### 安装依赖
```bash
pip3 install rich psutil requests speedtest-cli --break-system-packages
```

### 快速启动
```bash
python3 benchmark.py
```

## 📄 开源协议
本项目采用 [MIT License](LICENSE) 协议开源。
