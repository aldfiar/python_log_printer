import os

import pytest

from printer.src.monitor import Monitor


class TestMonitor:

    def test_print(self):
        file_name = "./test_file.txt"
        with open(file_name, 'w+') as f:
            f.write("[1] one\n")
            f.write("[1] two\n")

        monitor = Monitor(r'\[(\d+)\]', FakeReporter(), "one")
        monitor.monitor(file_name)

        os.remove(file_name)


class FakeReporter:
    def print(self, lines):
        assert len(lines) == 1
