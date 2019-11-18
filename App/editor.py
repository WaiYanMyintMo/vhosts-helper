def replace(data: str, old: str, new:str) -> str:
    return data.replace(old, new)


def read_replace(name: str, old: str, new: str) -> str:
    with open(name, 'r') as book:
        return book.read().replace(old, new)


def append(name: str, data: str):
    with open(name, 'a') as book:
        book.write(data)


def update(config_local: dict) -> None:
    if pathname == 'hosts':
        path = HostsPath
    elif pathname == 'vhosts':
        path = VhostsPath


def main():
    book_path = '..\\Output\\amhelib.com.txt'
    a = read_replace(book_path, 'S', 'Vroom')
    append(book_path, a)

if __name__ == '__main__':
    main()