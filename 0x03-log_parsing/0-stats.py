#!/usr/bin/python3
"""
This script does Log parsing: Parses log data from stdin and computes statistics.
"""

import sys

<<<<<<< HEAD
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
=======
if __name__ == "__main__":
    # Initialize variables
    total_filesize, line_count = 0, 0
    # Define status codes to track
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Initialize dictionary to store status code frequencies
    status_code_counts = {code: 0 for code in status_codes}

    def print_stats(status_code_counts: dict, file_size: int) -> None:
        print("File size: {:d}".format(total_filesize))
        for k, v in sorted(status_code_counts.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except BaseException:
                pass
            try:
                total_filesize += int(data[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_stats(status_code_counts, total_filesize)
        print_stats(status_code_counts, total_filesize)
    except KeyboardInterrupt:
        print_stats(status_code_counts, total_filesize)
        raise
>>>>>>> 8b0f79022ed7143335e2ff8e74499c9cbebd8833
