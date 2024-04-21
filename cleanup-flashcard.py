import psutil

def kill_process_by_pid(pid):
    try:
        proc = psutil.Process(pid)
        proc.kill()
        print(f"Zamknięto proces o PID {pid}.")
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        print(f"Nie udało się zamknąć procesu o PID {pid}: {e}")

def cleanup():
    try:
        with open("process_pids.txt", "r") as file:
            pids = [int(line.strip()) for line in file.readlines()]
        for pid in pids:
            kill_process_by_pid(pid)
    except FileNotFoundError:
        print("Nie znaleziono pliku z PID.")

cleanup()

