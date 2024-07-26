#!/usr/bin/env python3
"""Script measures the internet speed"""
import time
import requests
import random
import string
import datetime

def generate_random_data(size_in_mb):
    """Generiere zufällige Daten für den Upload-Test"""
    size_in_bytes = size_in_mb * 1024 * 1024
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size_in_bytes))

def measure_download_speed(url, file_size_mb):
    """Misst die Download-Geschwindigkeit"""
    start_time = time.time()
    response = requests.get(url, stream=True)
    total_downloaded = 0
    for chunk in response.iter_content(1024 * 1024):
        total_downloaded += len(chunk)
        if total_downloaded >= file_size_mb * 1024 * 1024:
            break
    end_time = time.time()
    download_time = end_time - start_time
    download_speed_mbps = (file_size_mb * 8) / download_time
    return download_speed_mbps

def measure_upload_speed(url, data):
    """Misst die Upload-Geschwindigkeit"""
    start_time = time.time()
    response = requests.post(url, data=data)
    end_time = time.time()
    upload_time = end_time - start_time
    data_size_mb = len(data) / (1024 * 1024)
    upload_speed_mbps = (data_size_mb * 8) / upload_time
    return upload_speed_mbps

def log_speed(download_speed, upload_speed):
    """Protokolliere die gemessenen Geschwindigkeiten"""
    with open("speed_log.txt", "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp}, Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps\n")

def main():
    download_url = "http://ipv4.download.thinkbroadband.com/10MB.zip"  # URL für den Download-Test
    upload_url = "http://httpbin.org/post"  # URL für den Upload-Test
    file_size_mb = 10  # Größe der herunterzuladenden Datei in MB
    data_size_mb = 5  # Größe der hochzuladenden Daten in MB

    try:
        while True:
            download_speed = measure_download_speed(download_url, file_size_mb)
            upload_data = generate_random_data(data_size_mb)
            upload_speed = measure_upload_speed(upload_url, upload_data)
        
            print(f"Download-Geschwindigkeit: {download_speed:.2f} Mbps")
            print(f"Upload-Geschwindigkeit: {upload_speed:.2f} Mbps")
        
            log_speed(download_speed, upload_speed)
        
            time.sleep(60)  # 1 Minute warten
    except KeyboardInterrupt:
        print("Programm gestoppt!")

if __name__ == "__main__":
    main()
