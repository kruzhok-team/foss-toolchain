import csv

class AmbiguousInputError(Exception):
    
    def __init__(self, data):
        self.message = f"Could not define proper order for {data}"


def parse_csv(content: str) -> list[dict[str, str]]:
    """
    Parse csv and returns corresponding column-value for every row

    :param content: csv-formatted content like "Name,Age,City\nJohn,30,New York"
    :type content: str

    Example:

    Input: "Name,Age,City\nJohn,30,New York"

    Ouput:
    [
        {"Name": "John", "Age": "30", "City": "New York"},
        {"Name": "Alice", "Age": "25", "City": "Chicago"},
    ]
    """
    data = []
    lines = content.strip().split("\n")
    if not lines:
        return data

    reader = csv.reader(lines)
    header = next(reader)

    for row in reader:
        row_dict = {column.strip(): "" for column in header}
        if len(row) < len(header) or len(row) > len(header) + 1:
            raise AmbiguousInputError(row)
        if len(row) == len(header) + 1 and row[-1] != "":
            raise AmbiguousInputError(row)
        for col_name, value in zip(header, row):
            row_dict[col_name.strip()] = value.strip()
        data.append(row_dict)

    return data
