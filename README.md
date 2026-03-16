# 🚀 Ubuntu Full-Spectrum Benchmark Tool (v5.0)

[![AI-Collaborated](https://img.shields.io/badge/AI-Collaborated-blueviolet?style=for-the-badge&logo=openai)](https://github.com/kkfreedom/ubuntu-benchmark-script)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[简体中文](./README.zh-CN.md)

---

A professional, aesthetically pleasing, and comprehensive Ubuntu server performance assessment tool written in Python. Specially optimized for network detection and speed testing under **Split-Proxy / Transparent Proxy** environments.

## 🤖 AI Collaboration Statement
> **Note**
> This project was developed in deep collaboration between **kkfreedom** and **Gemini CLI (AI Assistant)**. The AI contributed to the core software architecture, network split-tunneling logic optimization, and Terminal UI enhancements.

## ✨ Key Features
- 💻 **Hardware Overview**: Instant retrieval of CPU model, core/thread count, and total RAM.
- ⚡ **Computation Benchmark**: Evaluates single-core performance via high-precision Pi calculation.
- 💾 **IO Throughput Test**: Real-world synchronous write and sequential read speed measurements (100MB test file).
- 🌐 **Deep Split-Tunneling Detection**:
    - Designed specifically for **Transparent Proxy/Router-level Split-Tunneling** environments.
    - Compares Domestic (3322.org) vs. Global (ifconfig.me) exit IPs to verify rule effectiveness.
- 🚀 **Smart Network Speedtest**: Automatically matches the fastest server node based on the current exit IP.
- 🎨 **Rich Terminal UI**: Powered by the `rich` library, featuring dynamic progress bars, nested panels, and colorful summary tables.

## 🛠️ Installation & Usage
```bash
# 1. Install Python3
sudo apt update && sudo apt install -y python3-pip

# 2. Install Dependencies
pip3 install rich psutil requests speedtest-cli --break-system-packages

# 3. Quick Start
python3 benchmark.py
```

## 📄 License
This project is licensed under the [MIT License](LICENSE).
