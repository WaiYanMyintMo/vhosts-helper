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
            data = '\n' + data
            append(path, data)
        elif update_option == '+':
            with open(path, 'r') as fr, open(path, 'w') as fw:
                old_data = fr.read()
                fw.write(data)
                edit(path, old_data)
    else:
        with open(path, 'r') as fr:
            found = False
            fr_lines = fr.readlines()
            if update_option == '-':
                with open(path, "w") as fw:
                    for line in fr_lines:
                        fw.write(line)
                        if update_type in line:
                            found = True
                            fw.write(data + "\n")
            elif update_option == '+':
                with open(path, "w") as fw:
                    for line in fr_lines:
                        if update_type in line:
                            found = True
                            fw.write(data + "\n")
                        fw.write(line)
            if not found:
                edit(path, data)
                # content = f.read()
                # f.seek(0, 0)
                # f.write(data.rstrip('\r\n') + '\n' + content)


def output(path: str, data:str) -> None:
    with open(path, 'w+') as file:
        data = '--Output--' + data
        file.write(data)


def main():
    book_path = '..\\Output\\amhelib.com.txt'
    edit(book_path, 'S', 'Vroom')

if __name__ == '__main__':
    main()