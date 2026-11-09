# logparse-suspicious

Flags source addresses with repeated failed logins in an auth log. Built for triage of lab and authorized logs.

## Problem it solves
Brute-force attempts show up as bursts of failed logins from one source. Scanning raw logs by eye is slow, so this script counts failures per source and lists the ones above a threshold.

## Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The script uses only the Python standard library, so `requirements.txt` has no packages.

## Usage
```bash
python3 logparse.py samples/sample-auth.log --scope scope.txt --threshold 3 --year 2026
```

Example output:

```
source           failures  first_seen            last_seen
192.0.2.50       5         2026-03-02 10:14:01   2026-03-02 10:14:09
```

## Options
- `--scope FILE`: a list of allowed networks, one per line. Sources outside it are refused.
- `--threshold N`: minimum failures to report (default 5).
- `--year YEAR`: year to use, since syslog timestamps omit it.

## Limits
- Parses one log format (OpenSSH-style `Failed password` lines).
- Counts failures only. It doesn't correlate with successful logins or other sources.
- Thresholds are a starting point. Tune them against your baseline.

## Testing
Run against `samples/sample-auth.log`. The expected output is shown above.

## Authorized use
For use on logs from systems you own or are authorized to analyze.
