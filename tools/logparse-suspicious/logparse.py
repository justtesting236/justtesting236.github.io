#!/usr/bin/env python3
"""Flag source addresses with repeated failed logins in an auth log."""

import argparse
import ipaddress
import re
import sys
from collections import defaultdict
from datetime import datetime

FAILED = re.compile(
    r"^(?P<ts>\w{3}\s+\d+\s[\d:]+)\s+\S+\s+sshd\[\d+\]:\s+Failed password .* from "
    r"(?P<src>[\d.]+) port"
)


def load_scope(path):
    networks = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                networks.append(ipaddress.ip_network(line, strict=False))
    return networks


def parse(path, year):
    hits = defaultdict(list)
    with open(path) as fh:
        for line in fh:
            m = FAILED.match(line)
            if not m:
                continue
            ts = datetime.strptime(f"{year} {m['ts']}", "%Y %b %d %H:%M:%S")
            hits[m["src"]].append(ts)
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("logfile")
    ap.add_argument("--scope", help="file listing allowed networks")
    ap.add_argument("--threshold", type=int, default=5)
    ap.add_argument("--year", type=int, default=datetime.now().year,
                    help="year to use, since syslog timestamps omit it")
    args = ap.parse_args()

    scope = load_scope(args.scope) if args.scope else None

    hits = parse(args.logfile, args.year)
    print(f"{'source':<16} {'failures':<9} {'first_seen':<21} last_seen")
    for src, times in sorted(hits.items(), key=lambda kv: -len(kv[1])):
        if len(times) < args.threshold:
            continue
        if scope is not None and not any(ipaddress.ip_address(src) in n for n in scope):
            print(f"refusing {src}: not in scope file", file=sys.stderr)
            continue
        times.sort()
        print(f"{src:<16} {len(times):<9} {times[0]!s:<21} {times[-1]!s}")


if __name__ == "__main__":
    main()
