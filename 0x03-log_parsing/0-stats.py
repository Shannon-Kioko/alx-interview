#!/usr/bin/python3
import sys
import datetime

# Initialize variables to store metrics
file_size_total = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        # Split the line into its components
        parts = line.strip().split()
        if len(parts) != 7:
            # Skip lines that don't match the expected format
            continue

        # Extract file size and status code from the line
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        file_size_total += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {file_size_total}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    # Handle keyboard interruption
    print(f"Total file size: {file_size_total}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
