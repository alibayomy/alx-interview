#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics"""
import sys
import re


def main():
    """Entery point"""

    ip_regex = r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$'
    counter = 0
    total_size = 0
    status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                    404: 0, 405: 0, 500: 0}
    try:
        for line in sys.stdin:
            if counter == 10:
                counter = 0
                print(f"File size: {total_size}")
                for key, value in status_code.items():
                    if value > 0:
                        print(f"{key}: {value}")
                data = line.split()
                try:
                    ip = data[0]
                    status = data[-2]
                    file_size = data[-1]
                    counter += 1
                except ValueError as e:
                    raise e

                try:
                    file_size = int(file_size)
                    total_size = total_size + file_size
                except ValueError as e:
                    raise e

                try:
                    file_status_code = int(status)
                    if (file_status_code in status_code.keys()):
                        status_code[file_status_code] = status_code[file_status_code] + 1
                except ValueError as e:
                    raise e
            
    except KeyboardInterrupt:
        print(f"File size: {total_size}")
        for key,value in status_code.items():
            if value > 0:
                print(f"{key}: {value}")
main()
