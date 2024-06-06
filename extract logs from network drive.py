import os
import re
from datetime import datetime

# Path to the network drive
network_drive_path = '/path/to/network/drive'

# Pattern to match files starting with "ABCDBB8"
file_pattern = re.compile(r'^ABCDBB8.*')

# Function to find the most recent file
def find_most_recent_file(path, pattern):
    recent_file = None
    recent_time = None
    
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                if pattern.match(file):
                    file_path = os.path.join(root, file)
                    file_time = os.path.getmtime(file_path)
                    
                    if recent_time is None or file_time > recent_time:
                        recent_file = file_path
                        recent_time = file_time
    except PermissionError:
        print(f'Permission denied: Unable to access {path}')
    except FileNotFoundError:
        print(f'File not found: {path}')
    except Exception as e:
        print(f'An error occurred while accessing the network path: {e}')
    
    return recent_file

# Function to extract error logs from a file
def extract_error_logs(file_path):
    error_logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if 'ERROR' in line:
                    error_logs.append(line.strip())
    except PermissionError:
        print(f'Permission denied: Unable to read the file {file_path}')
    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred while reading the file: {e}')
    
    return error_logs

# Main script
def main():
    # Find the most recent file
    recent_file = find_most_recent_file(network_drive_path, file_pattern)

    if recent_file:
        print(f'Most recent file: {recent_file}')
        # Extract error logs
        error_logs = extract_error_logs(recent_file)
        # Print error logs
        if error_logs:
            for log in error_logs:
                print(log)
        else:
            print('No error logs found in the file.')
    else:
        print('No matching file found.')

# Execute the main script
if __name__ == "__main__":
    main()
