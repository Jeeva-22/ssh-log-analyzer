import re
from collections import defaultdict

def analyze_ssh_logs(file_path, threshold=3):
    failed_attempts = defaultdict(int)
    pattern = re.compile(r"(?P<date>\w{3}\s+\d+\s\d{2}:\d{2}:\d{2}).*Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)")

    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = pattern.search(line)
                if match:
                    ip = match.group('ip')
                    failed_attempts[ip] += 1
    except FileNotFoundError:
        print(f"Error: Could not find {file_path}")
        return

    print("Brute Force Attempts Detected")
    print("-" * 35)
    
    for ip, count in failed_attempts.items():
        if count >= threshold:
            print(f"[WARNING] IP: {ip} | Failed Attempts: {count}")

if __name__ == "__main__":
    analyze_ssh_logs("auth.log", threshold=3)