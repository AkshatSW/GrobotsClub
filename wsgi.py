import os
import sys
from threading import Thread
import requests
import time
from app import app

def keep_server_active():
    url = 'http://127.0.0.1:5000'  # Change to your server's URL
    timeout = 5  # Time to wait for server response in seconds

    while True:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code != 200:
                print(f"Server responded with status code {response.status_code}. Restarting server...")
                restart_server()
            else:
                print("Server is active.")
        except requests.RequestException as e:
            print(f"Error: {e}. Restarting server...")
            restart_server()

        time.sleep(10)  # Check every 10 seconds

def restart_server():
    print("Restarting server...")
    os.system("./restart_gunicorn.sh")

if __name__ == "__main__":
    # Start the keep_server_active thread
    keep_alive_thread = Thread(target=keep_server_active)
    keep_alive_thread.start()

    # Start the Flask app
    app.run()
