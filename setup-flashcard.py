import subprocess
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

def open_vscode_and_run_ng(directory):
    # Uruchamianie Visual Studio Code i zapisywanie PID
    vscode_process = subprocess.Popen(["C:\\Users\\vagrant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", directory])
    # Uruchamianie terminala i zapisywanie PID
    terminal_process = subprocess.Popen(["cmd", "/K", "cd /d " + directory + " && npm i && ng s -o"], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # Zapisywanie PID do pliku
    with open("process_pids.txt", "w") as file:
        file.write(f"{vscode_process.pid}\n")
        file.write(f"{terminal_process.pid}\n")

open_vscode_and_run_ng(script_dir)
