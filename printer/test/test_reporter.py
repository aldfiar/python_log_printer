import pytest

from printer.src.reporter import Reporter


class TestReporter:

    def test_reporter_lines_larger_than_limit(self, capsys):
        reporter = Reporter(3, "--")
        str_values = [str(x) for x in range(1, 10)]
        reporter.print(str_values)
        out, err = capsys.readouterr()
        values = out.split()
        assert len(values) == 4

    def test_reporter_lines_less_than_limit(self, capsys):
        reporter = Reporter(10, "--")
        str_values = [str(x) for x in range(1, 3)]
        reporter.print(str_values)
        out, err = capsys.readouterr()
        values = out.split()
        assert len(values) == 3
