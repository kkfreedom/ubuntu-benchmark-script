import os
import time
import psutil
import platform
import socket
import requests
import speedtest
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.align import Align
from rich.columns import Columns
from rich import box

console = Console()

# --- 1. 硬件信息获取 ---
def get_system_info():
    mem = psutil.virtual_memory()
    return {
        "操作系统": f"{platform.system()} {platform.release()}",
        "架构": platform.machine(),
        "CPU 型号": platform.processor() or "x86_64",
        "核心/线程": f"{psutil.cpu_count(logical=False)}C / {psutil.cpu_count(logical=True)}T",
        "内存总量": f"{round(mem.total / (1024**3), 2)} GB",
        "主机名": socket.gethostname()
    }

# --- 2. CPU & 磁盘性能测试 ---
def benchmark_cpu():
    n = 10000
    start_time = time.time()
    pi = 0
    for i in range(n):
        pi += 4 * ((-1)**i) / (2*i + 1)
    return round(time.time() - start_time, 4)

def benchmark_disk():
    test_file = "temp_bench_file.dat"
    size_mb = 100
    data = os.urandom(1024 * 1024)
    # Write
    start_time = time.time()
    with open(test_file, "wb") as f:
        for _ in range(size_mb):
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
    write_speed = size_mb / (time.time() - start_time)
    # Read
    start_time = time.time()
    with open(test_file, "rb") as f:
        while f.read(1024 * 1024): pass
    read_speed = size_mb / (time.time() - start_time)
    os.remove(test_file)
    return round(write_speed, 2), round(read_speed, 2)

# --- 3. 代理与网络分流检测 ---
def get_ip_by_source(url):
    headers = {'User-Agent': 'curl/7.81.0'}
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        ip_match = re.search(r'(\d{1,3}\.){3}\d{1,3}', resp.text)
        return ip_match.group(0) if ip_match else "未知"
    except: return "超时/失败"

# --- 4. 自动匹配测速 ---
def benchmark_network():
    try:
        st = speedtest.Speedtest(secure=True)
        st.get_best_server()
        dl = st.download() / 1_000_000
        ul = st.upload() / 1_000_000
        best = st.results.dict()['server']
        return round(dl, 2), round(ul, 2), f"{best['sponsor']} ({best['name']})"
    except: return "N/A", "N/A", "测速失败"

# --- 5. 主运行程序 ---
def run_full_benchmark():
    console.clear()
    console.print(Panel.fit("[bold green]🚀 Ubuntu 全能性能评估系统 v5.0[/bold green]\n[dim]CPU | 磁盘 | 代理分流 | 全链路带宽[/dim]", border_style="bright_blue"))

    # 1. 硬件概览
    sys_info = get_system_info()
    sys_table = Table(box=box.SIMPLE, show_header=False, padding=(0,2))
    for k, v in sys_info.items():
        sys_table.add_row(f"[bold cyan]{k}[/bold cyan]", v)
    console.print(Panel(sys_table, title="[white]💻 硬件概览[/white]", border_style="blue"))

    # 2. 性能与网络检测 (带进度条)
    results = {}
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=30),
        console=console
    ) as progress:
        
        # CPU & Disk
        t1 = progress.add_task("[yellow]测试 CPU 计算性能...", total=100)
        results['cpu_time'] = benchmark_cpu()
        progress.update(t1, completed=100)
        
        t2 = progress.add_task("[magenta]测试 磁盘读写 吞吐量...", total=100)
        results['write_s'], results['read_s'] = benchmark_disk()
        progress.update(t2, completed=100)

        # IP Detection (触发分流)
        t3 = progress.add_task("[cyan]探测分流 IP 出口状态...", total=100)
        results['ip_cn'] = get_ip_by_source("http://members.3322.org/dyndns/getip")
        results['ip_gl'] = get_ip_by_source("https://ifconfig.me/ip")
        progress.update(t3, completed=100)

        # Network Speed
        t4 = progress.add_task("[green]执行全链路带宽测速...", total=100)
        results['dl'], results['ul'], results['node'] = benchmark_network()
        progress.update(t4, completed=100)

    # 3. 结果面板展示
    # 网络状态分栏
    ip_status = "[bold green]分流规则已生效[/bold green]" if results['ip_cn'] != results['ip_gl'] else "[bold red]全局模式/未分流[/bold red]"
    net_panel = Panel(
        f"国内直连出口: [bold blue]{results['ip_cn']}[/bold blue]\n"
        f"海外代理出口: [bold magenta]{results['ip_gl']}[/bold magenta]\n"
        f"当前分流判定: {ip_status}",
        title="🌐 网络分流探测", border_style="cyan"
    )

    # 汇总表格
    res_table = Table(title="\n[bold bright_green]📊 性能评估综合汇总[/bold bright_green]", box=box.DOUBLE_EDGE, expand=True)
    res_table.add_column("分类", style="bold white", width=12)
    res_table.add_column("测试项目", style="white")
    res_table.add_column("数值 / 结果", justify="center", style="bright_yellow")
    res_table.add_column("等级", justify="center")

    # CPU
    cpu_lv = "[green]极佳[/green]" if results['cpu_time'] < 0.005 else "[yellow]良好[/yellow]"
    res_table.add_row("运算性能", "CPU 圆周率运算", f"{results['cpu_time']} s", cpu_lv)
    
    # Disk
    disk_lv = "[green]极速[/green]" if results['write_s'] > 400 else "[yellow]普通[/yellow]"
    res_table.add_row("IO 性能", "磁盘同步写入", f"{results['write_s']} MB/s", disk_lv)
    res_table.add_row("IO 性能", "磁盘顺序读取", f"{results['read_s']} MB/s", "---")

    # Network
    res_table.add_row("带宽性能", "下载带宽 (DL)", f"{results['dl']} Mbps", "[cyan]检测完成[/cyan]")
    res_table.add_row("带宽性能", "上传带宽 (UL)", f"{results['ul']} Mbps", "---")
    res_table.add_row("测速节点", "匹配服务器", results['node'], "---", end_section=True)

    console.print(net_panel)
    console.print(res_table)

    # Footer
    mem = psutil.virtual_memory()
    console.print(Align.center(f"[dim]实时状态: CPU {psutil.cpu_percent()}% | 内存 {mem.percent}% | 测试时间: {time.strftime('%Y-%m-%d %H:%M:%S')}[/dim]"))
    console.print("\n[bold green]✅ 测试圆满完成！[/bold green] 如果您对结果满意，请考虑为服务器升级配置或优化分流规则。")

if __name__ == "__main__":
    run_full_benchmark()
