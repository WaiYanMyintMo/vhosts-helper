# //Must Have Outline
# Host and Vhost assigned at top of file.
# Server Name and DocumentRoot assigned at top of file.
# Function for opening file, reading and returning replaced data.
# Function for appending data to a file.

config = {'PathName': 'HostsPath',
          'HostsPath': 'C:\\Windows\\System32\\drivers\\etc\\hosts',
          'VhostsPath': 'C:\\xampp\\apache\\conf\\extra\\httpd-vhosts.conf',
          'ServerName': 'testing1.com',
          'DocumentRoot': 'D:\\Testing1\\',
          'UpdateLocationType': '"",str',
          'UpdateLocation': '',
          'UnspecifiedLocationTypes': '"End", "Start"',
          'UnspecifiedLocation': 'End'}


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
    update('hosts')


main()
