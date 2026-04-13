# speedtest-cli

A simple CLI script to test network speed from the terminal.

## Requirements

```bash
pip install speedtest-cli
```

## Install

```bash
ln -s /path/to/run_speedtest.py ~/.local/bin/speedtest-cli
```

## Usage

```bash
speedtest-cli              # full output with progress
speedtest-cli --simple     # one-line summary
speedtest-cli --json       # JSON output
```

### Example output

```
Finding best server...
Testing download... 45.23 Mbps
Testing upload...   12.87 Mbps
Download: 45.23 Mbps
Upload:   12.87 Mbps
Ping:     14.3 ms
Server:   Chicago, IL (Comcast)
```
