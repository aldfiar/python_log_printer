import re


class Monitor:
    def __init__(self, expression, reporter) -> None:
        self.storage = dict()
        self.expression = expression
        self.reporter = reporter

    def _add_line(self, key, line):
        if key not in self.storage.keys():
            self.storage[key] = list()
        self.storage[key].append(line)

    def monitor(self, file_name):
        with open(file_name, 'r') as f:
            for line in f:
                key = re.search(self.expression, line).group(1)
                if key:
                    self._add_line(key=key, line=line.rstrip())
                    if "ERROR" in line:
                        self.reporter.print(self.storage[key])
