# speedtest-cli

A nicer terminal front-end for [Ookla's official `speedtest` CLI](https://www.speedtest.net/apps/cli).
It runs the real Ookla test (for accurate results) and renders live progress bars
plus a formatted summary instead of Ookla's default output.

<p align="center">
  <img src="docs/demo.gif" alt="speedtest-cli running: ISP and server header, live ping, download and upload progress bars, then a summary with download, upload, latency, jitter, packet loss and a result link" width="800">
</p>
<p align="center"><sub>Recorded with <a href="https://github.com/charmbracelet/vhs">vhs</a> from <a href="docs/demo.tape"><code>docs/demo.tape</code></a>. The rendering is the real wrapper; the test itself is a replay with made-up numbers from <a href="docs/demo-bin/speedtest"><code>docs/demo-bin/speedtest</code></a>, a stand-in for Ookla's CLI.</sub></p>

## Requirements

Install Ookla's `speedtest` binary (the official one, **not** the Python
`speedtest-cli` package — they aren't the same and produce different numbers):

```bash
# macOS
brew install speedtest --force

# Debian / Ubuntu
curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash
sudo apt-get install speedtest

# Other platforms: https://www.speedtest.net/apps/cli
```

Verify it's on your PATH:

```bash
speedtest --version
```

This wrapper is pure Python 3 with no extra dependencies.

## Install

```bash
ln -s /path/to/run_speedtest.py ~/.local/bin/speedtest-cli
```

## Usage

```bash
speedtest-cli                    # live progress + formatted summary
speedtest-cli --simple           # one-line summary
speedtest-cli --json             # compact JSON (download_mbps, upload_mbps, ping_ms, server fields)
speedtest-cli --raw-json         # Ookla's full raw JSON (jitter, packet loss, result URL, etc.)
speedtest-cli --server-id 1234   # pin a specific Ookla server
speedtest-cli --no-color         # disable ANSI colors
```

### Example output

```
Speedtest by Ookla
  ISP   : Comcast
  Server: Chicago, IL, United States

  ● Ping       ████████████████████████████   14.32 ms
  ↓ Download   ████████████████████████████  245.31 Mbps
  ↑ Upload     ████████████████████████████   12.04 Mbps

────────────────────────────────────────────────────
  ↓ Download     245.31 Mbps
  ↑ Upload        12.04 Mbps
  ⚡ Latency      14.32 ms (jitter 0.84 ms)
  ⊘ Loss           0.00 %
────────────────────────────────────────────────────
  Server: Chicago, IL, United States
  ISP   : Comcast
  Result: https://www.speedtest.net/result/c/...
```
