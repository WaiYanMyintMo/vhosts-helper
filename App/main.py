# //Must Have Outline
# Host and Vhost assigned at top of file.
# Server Name and DocumentRoot assigned at top of file.
# Function for opening file, reading and returning replaced data.
# Function for appending data to a file.

HostsPath = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
VhostsPath = 'C:\\xampp\\apache\\conf\\extra\\httpd-vhosts.conf'
ServerName = 'testing1.com'
DocumentRoot = 'D:\\Testing\\'


def replace(Data, Old, New):
    return Data.replace(Old, New)


def openBook(Name):
    book = open(Name, 'r+')
    return book


def readReplace(Name, Old, New):
    with openBook(Name) as book:
        return book.read().replace(Old, New)


def append(Name, Data):
    with open(Name, 'a') as book:
        book.write(Data)
