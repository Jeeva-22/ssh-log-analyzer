# Automated SSH Log Analyzer

## Overview
A Python-based security operations tool designed to automate Level 1 SOC triage. This script parses Linux `auth.log` files to detect SSH brute-force attacks and credential stuffing while actively reducing false positives (alert fatigue) through a configurable failure threshold.

## The Security Problem
Authentication logs are noisy. A single server can generate thousands of events a day. Security analysts need to differentiate between an employee making a simple password typo and an automated botnet actively attacking the infrastructure. 

This script solves that by isolating repeated authentication failures from unique IP addresses, only alerting when a specific threshold is crossed.

## Skills Demonstrated
- **Security Telemetry Parsing:** Extracting actionable intelligence from raw server logs.
- **Regular Expressions (Regex):** Building custom patterns to identify standardized log structures.
- **Alert Fatigue Reduction:** Implementing threshold logic to filter out human error and surface genuine threats.
- **Python Scripting:** Using core libraries (`re`, `collections`) to manipulate and evaluate data arrays.

## Prerequisites
- Python 3.x
- No external dependencies required (runs on built-in libraries).

## Usage
1. Clone this repository to your local machine.
2. Ensure `auth.log` is in the same directory as the script.
3. Run the script via the command line:
   ```bash
   python log_analyzer.py
