class Reporter:

    def __init__(self, limit, delimiter) -> None:
        self.limit = limit
        self.delimiter = delimiter

    def print(self, lines: list):
        print_lines = list()
        if len(lines) < self.limit:
            print_lines.extend(lines)
        else:
            print_lines.extend(lines[-self.limit:])
        print_lines.append(self.delimiter)
        for element in print_lines:
            print(element)
