# Scanner

A simple multi-threaded TCP port scanner written in Python. This project scans all TCP ports (1–65535) on a target host using concurrent threads and reports which ports are open. This scanner is designed for learning.

## How It Works

- Accepts a target hostname or IP as a command-line argument
- Resolves hostnames to IP addresses
- Creates a pool of worker threads
- Each thread attempts a TCP connection to a specific port
- Open ports are printed safely without overlapping output
- Displays total scan duration and ports scanned

## Install

Clone the repository or copy the script locally:

`git clone <repo-url>`

`cd scanner`

## Run

Run the scanner from the command line:

`python scanner.py <target_ip_or_hostname>`

## Sample Output

## Legal & Ethical Warning

This tool should only be used on:

- Systems you own
- Systems you have explicit permission to test
- Lab environments (TryHackMe, Hack The Box, local VMs)

Unauthorized port scanning may be illegal and violate acceptable use policies.
