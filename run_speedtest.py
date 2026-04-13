#!/usr/bin/env python3

import argparse
import json
import sys
import speedtest


def parse_args():
    parser = argparse.ArgumentParser(description="Run a network speed test")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--simple", action="store_true")
    group.add_argument("--json", action="store_true")
    return parser.parse_args()


def run_test(verbose=False):
    st = speedtest.Speedtest()

    if verbose:
        print("Finding best server...", flush=True)
    st.get_best_server()

    speeds = {}
    for label, method in [("download", st.download), ("upload", st.upload)]:
        if verbose:
            print(f"Testing {label}...", end=" ", flush=True)
        speeds[label] = method() / 1_000_000
        if verbose:
            print(f"{speeds[label]:.2f} Mbps")

    server = st.results.server
    return {
        "download_mbps": round(speeds["download"], 2),
        "upload_mbps": round(speeds["upload"], 2),
        "ping_ms": round(st.results.ping, 2),
        "server_name": server["name"],
        "server_country": server["country"],
        "server_sponsor": server["sponsor"],
    }


def main():
    args = parse_args()

    try:
        data = run_test(verbose=not (args.simple or args.json))
    except speedtest.SpeedtestException as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    server_str = f"{data['server_name']}, {data['server_country']} ({data['server_sponsor']})"

    if args.json:
        print(json.dumps(data, indent=2))
    elif args.simple:
        print(f"Ping: {data['ping_ms']} ms  Down: {data['download_mbps']} Mbps  Up: {data['upload_mbps']} Mbps")
    else:
        print(f"Download: {data['download_mbps']} Mbps")
        print(f"Upload:   {data['upload_mbps']} Mbps")
        print(f"Ping:     {data['ping_ms']} ms")
        print(f"Server:   {server_str}")


if __name__ == "__main__":
    main()
