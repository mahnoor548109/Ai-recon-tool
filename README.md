# AI-Powered Recon & Vulnerability Triage Tool

A Python-based tool that combines automated network reconnaissance (Nmap) with AI-driven vulnerability analysis (Groq API - Llama 3.3 70B). This tool converts raw scan data into an instant, actionable, prioritized security report.

## Overview

Manual analysis of Nmap scan output can be time-consuming, especially for beginners. This tool automates the reconnaissance phase of a penetration test by scanning a target, then using an LLM to interpret the results and generate a risk-prioritized triage report — reducing analysis time from minutes to seconds.

## Features

- Automated Nmap service and version detection scan
- AI-powered analysis of open ports and services using Groq's Llama 3.3 70B model
- Identifies potentially outdated or vulnerable services
- Generates a priority order for further manual testing
- Automatically saves a timestamped report file for record-keeping

## Tech Stack

- Python 3
- Nmap (network scanning engine)
- Groq API (Llama 3.3 70B Versatile model)
- Tested in a home lab: Kali Linux (attacker) targeting Metasploitable2 (intentionally vulnerable VM)

## Setup

```bash
pip install groq --break-system-packages
export GROQ_API_KEY="your_api_key_here"
python3 recon.py
```

## How It Works

1. User provides a target IP address
2. The tool runs an Nmap scan (`-sV`) to detect open ports, services, and versions
3. The raw scan output is sent to the Groq AI API
4. The AI analyzes the data and returns:
   - A summary of running services
   - Identification of outdated or vulnerable services
   - A prioritized list of what to investigate first
5. Results are displayed in the terminal and saved to a timestamped `.txt` report

## Sample Output

When run against a target like Metasploitable2, the tool detects 20+ open services (FTP, SSH, MySQL, IRC, etc.) and the AI categorizes them by risk level — for example, prioritizing SSH/Telnet/FTP (credential exposure risk), MySQL/PostgreSQL (database risk), HTTP (web application risk), and VNC/X11 (remote access risk).

## Use Case

This tool is designed to speed up the initial reconnaissance phase of a penetration test. Instead of manually cross-referencing every detected service version against known vulnerabilities, the AI provides an immediate, human-readable triage report, helping a pentester decide where to focus first.

## Disclaimer

This tool is intended strictly for authorized penetration testing and educational purposes. Only use it against systems you own or have explicit written permission to test.

# AI-Powered Recon & Vulnerability Triage Tool

A Python-based tool that combines automated network reconnaissance (Nmap) with AI-driven vulnerability analysis (Groq API - Llama 3.3 70B). This tool converts raw scan data into an instant, actionable, prioritized security report.

## Overview

Manual analysis of Nmap scan output can be time-consuming, especially for beginners. This tool automates the reconnaissance phase of a penetration test by scanning a target, then using an LLM to interpret the results and generate a risk-prioritized triage report — reducing analysis time from minutes to seconds.

## Features

- Automated Nmap service and version detection scan
- AI-powered analysis of open ports and services using Groq's Llama 3.3 70B model
- Identifies potentially outdated or vulnerable services
- Generates a priority order for further manual testing
- Automatically saves a timestamped report file for record-keeping

## Tech Stack

- Python 3
- Nmap (network scanning engine)
- Groq API (Llama 3.3 70B Versatile model)
- Tested in a home lab: Kali Linux (attacker) targeting Metasploitable2 (intentionally vulnerable VM)

## Setup

```bash
pip install groq --break-system-packages
export GROQ_API_KEY="your_api_key_here"
python3 recon.py
```

## How It Works

1. User provides a target IP address
2. The tool runs an Nmap scan (`-sV`) to detect open ports, services, and versions
3. The raw scan output is sent to the Groq AI API
4. The AI analyzes the data and returns:
   - A summary of running services
   - Identification of outdated or vulnerable services
   - A prioritized list of what to investigate first
5. Results are displayed in the terminal and saved to a timestamped `.txt` report

## Sample Output

When run against a target like Metasploitable2, the tool detects 20+ open services (FTP, SSH, MySQL, IRC, etc.) and the AI categorizes them by risk level — for example, prioritizing SSH/Telnet/FTP (credential exposure risk), MySQL/PostgreSQL (database risk), HTTP (web application risk), and VNC/X11 (remote access risk).

## Use Case

This tool is designed to speed up the initial reconnaissance phase of a penetration test. Instead of manually cross-referencing every detected service version against known vulnerabilities, the AI provides an immediate, human-readable triage report, helping a pentester decide where to focus first.

## Disclaimer

This tool is intended strictly for authorized penetration testing and educational purposes. Only use it against systems you own or have explicit written permission to test.

## Author

Mahnoor — BSCS Student | Aspiring Penetration Tester
Mahnoor — BSCS Student | Aspiring Penetration Tester
