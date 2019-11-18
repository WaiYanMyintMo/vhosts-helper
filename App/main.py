# //Must Have Outline
# Host and Vhost assigned at top of file.
# Server Name and DocumentRoot assigned at top of file.
# Function for opening file, reading and returning replaced data.
# Function for appending data to a file.

HostsPath = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
VhostsPath = 'C:\\xampp\\apache\\conf\\extra\\httpd-vhosts.conf'
ServerName = 'testing1.com'
DocumentRoot = 'D:\\Testing1\\'


def replace(data, old, new):
    return data.replace(old, new)


def read_replace(name, old, new):
    with open(name, 'r') as book:
        return book.read().replace(old, new)


def append(name, data):
    with open(name, 'a') as book:
        book.write(data)


def update(filename):
    if filename == 'hosts':
        path = HostsPath
    elif filename == 'vhosts':
        path = VhostsPath



def main():
    update('hosts')


main()
