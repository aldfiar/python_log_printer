import re


class Monitor:
    def __init__(self, expression, reporter, condition) -> None:
        self.storage = dict()
        self.expression = expression
        self.reporter = reporter
        self.condition = condition

    def _add_line(self, key, line):
        if key not in self.storage.keys():
            self.storage[key] = list()
        self.storage[key].append(line)

    def monitor(self, file_name):
        with open(file_name, 'r') as f:
            for line in f:
                find = re.search(self.expression, line)
                if find is not None:
                    key = find.group(1)
                    self._add_line(key=key, line=line.rstrip())
                    if self.condition in line:
                        self.reporter.print(self.storage[key])
