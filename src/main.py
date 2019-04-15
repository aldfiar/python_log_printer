import sys

from src.monitor import Monitor
from src.reporter import Reporter

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Pass path to llog first")
        exit()
    path = sys.argv[1]
    monitor = Monitor((r'\[(\d+)\]'), Reporter(4, "----"))
    monitor.monitor(path)
