def replace(data: str, old: str, new:str) -> str:
    return data.replace(old, new)


def read(name: str) -> str:
    with open(name, 'r') as book:
        return book.read()


def append(name: str, data: str):
    with open(name, 'a') as book:
        book.write(data)


def edit(path: str, data: str, update_type: str = 'append', update_option: str = '-') -> None:
    if update_type == 'append':
        if update_option == '-':
            append(path, data)


def main():
    book_path = '..\\Output\\amhelib.com.txt'
    a = read_replace(book_path, 'S', 'Vroom')
    append(book_path, a)

if __name__ == '__main__':
    main()