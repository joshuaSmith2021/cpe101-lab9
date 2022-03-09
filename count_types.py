# Purpose: Find type of correctly casted string
def smart_type(value: str) -> str:
    try:
        int(value)
        return 'int'
    except ValueError:
        try:
            float(value)
            return 'float'
        except ValueError:
            return 'other'


# Purpose: Print error message and exit program
def unable_to_open(file_name: str) -> None:
    print('Unable to open %s' % file_name)
    exit(1)


# Purpose: Open file and return list of values
def open_file(file_name: str) -> None:
    try:
        with open(file_name) as f:
            return f.read().split()
    except FileNotFoundError:
        unable_to_open(file_name)
    except PermissionError:
        unable_to_open(file_name)


# Purpose: Print out type details
def print_types(values: list) -> None:
    types = [smart_type(x) for x in values]

    print('Ints: %d' % types.count('int'))
    print('Floats: %d' % types.count('float'))
    print('Other: %d' % types.count('other'))


if __name__ == '__main__':
    values = open_file('infile')
    print_types(values)
