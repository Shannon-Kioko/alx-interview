#!/usr/bin/python3
import sys
import datetime

def print_statistics(file_size_total, status_code_counts):
    print(f"Total file size: {file_size_total}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

def parse_line(line):
    parts = line.strip().split()
    if len(parts) != 7:
        return None, None
    status_code = parts[-2]
    try:
        file_size = int(parts[-1])
        status_code = int(status_code)
        return status_code, file_size
    except ValueError:
        return None, None

def main():
    file_size_total = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is None or file_size is None:
                continue

            file_size_total += file_size
            status_code_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_statistics(file_size_total, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(file_size_total, status_code_counts)

if __name__ == "__main__":
    main()
