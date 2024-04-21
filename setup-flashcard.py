import subprocess
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

def open_vscode_and_run_ng(directory):
    # Uruchamianie Visual Studio Code i zapisywanie PID
    vscode_process = subprocess.Popen(["C:\\Users\\vagrant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", directory])

    # Uruchamianie terminala z poleceniem npm i i czekanie na jego zakończenie
    npm_process = subprocess.Popen(["cmd", "/C", "cd /d " + directory + " && npm i"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    npm_process.wait()  # Czekaj na zakończenie instalacji pakietów npm

    # Po zakończeniu npm i, uruchamianie Angulara
    ng_process = subprocess.Popen(["cmd", "/C", "cd /d " + directory + " && ng s -o"], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # Zapisywanie PID do pliku
    with open("process_pids.txt", "w") as file:
        file.write(f"VSCode PID: {vscode_process.pid}\n")
        file.write(f"npm install PID: {npm_process.pid}\n")
        file.write(f"Angular serve PID: {ng_process.pid}\n")

open_vscode_and_run_ng(script_dir)
