# Email Indicators of Compromise

IOC extraction tool designed to analyze suspicious .eml files.

The script parses raw email files, extracts IPs, URLs, headers, and attachments, performs hashing, safely defangs indicators,

## How It Works

- Reads a raw email file (.eml)
- Parses headers and body using Python's email module
- Extracts IP addresses and URLs using regex
- Filters invalid and reserved IP addresses
- Enriches public IPs via external API
- Defangs all indicators for safe output
- Extracts attachment metadata and hashes

## Install

Clone the repository or copy the script locally:

`git clone <email-ioc>`

`cd email-ioc`

## Run

Run the scanner from the command line:

`python eioc.py <sample_email.eml>`

## Sample Output

Extracted IP Addresses:

Extracted URLs:

Extracted Headers:

Authentication-Results:
Subject:
From:
To:
Date:
Return-Path:
Message-ID:
X-Sender-IP:=

Extracted Attachments:

Filename:
MD5:
SHA1:
SHA256:

## Legal & Ethical Warning

This tool should only be used on:

- Systems you own
- Systems you have explicit permission to test
- Lab environments (TryHackMe, Hack The Box, local VMs)

Unauthorized port scanning may be illegal and violate acceptable use policies.

### Resources

TCM Courses
