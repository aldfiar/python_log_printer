import sys

from printer.src.monitor import Monitor
from printer.src.reporter import Reporter

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Pass path to log file")
        exit()
    path = sys.argv[1]
    monitor = Monitor(r'\[(\d+)\]', Reporter(4, "----"), "ERROR")
    monitor.monitor(path)
