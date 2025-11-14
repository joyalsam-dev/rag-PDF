import subprocess
import time
import webview
import threading
import os
import sys

def start_streamlit():
    app_path = os.path.join(os.path.dirname(__file__), "app.py")
    cmd = [sys.executable, "-m", "streamlit", "run", app_path, "--server.port=8501", "--server.headless=true"]
    subprocess.Popen(cmd)

def open_window():
    time.sleep(2)  # wait for streamlit to start
    webview.create_window("My Streamlit App", "http://127.0.0.1:8501", width=1200, height=800)
    webview.start()

if __name__ == '__main__':
    threading.Thread(target=start_streamlit).start()
    open_window()
