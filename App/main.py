varSetBook = open('MainVarSet.txt', 'r')
varSetContent = varSetBook.readlines()
varSetBook.close()
SvrName = varSetContent[0].strip('\n')
Dir = varSetContent[1].strip('\n')

with open('config.txt', 'r') as configBook:
    configBook = configBook.readlines()
    OutputFolder = configBook[0].strip('\n')
    vhost_path = configBook[1].strip('\n')
    host_path = configBook[2].strip('\n')
    lookup = configBook[3].strip('\n')
    vhost_lookup = configBook[4].strip('\n')
print(f'Variables in template are {SvrName} and {Dir}.')

InputSvrName = input('Enter server name (example.com): ')
dirvar = input('Enter Dir Address (D:/project/location/document/root): ')
if '"' in dirvar:
    InputDir = dirvar
elif "'" in dirvar:
    InputDir = dirvar.replace("'", '"')
else:
    InputDir = f'"{dirvar}"'

TemplateBook = open('Template.txt', 'r')
TemplateContent = TemplateBook.read()
# print(f'Template is as follow\n..................\n{TemplateContent}\n...........')
print('\n.....................')
print(f'Replacing {SvrName} with {InputSvrName} and {Dir} with {InputDir}')

TemplateContent = TemplateContent.replace(SvrName, InputSvrName)
TemplateContent = TemplateContent.replace(Dir, InputDir)

## Extra Variables Start
with open('VarSet.txt', 'r') as VarSetBook:
    lines = VarSetBook.readlines()
    for i in lines:
        pass







## Extra Variables Stop
print(f'....................\n\n {TemplateContent}')
print('\n.....................')
while True:
    Directness = input('Do you want to insert directly into httpd-vhost.conf file? (y/n) :').lower()
    if Directness == 'y' or Directness == 'n':
        break
if Directness == 'y':
    with open(vhost_path, 'r+') as vhost_book:
        vhost_readlines = vhost_book.readlines()
        if vhost_lookup == '':
            og_data = vhost_book.read()
            final_data = '\n\n' + TemplateContent
            vhost_book.write(final_data)
        else:
            num = 0
            while num < vhost_readlines.__len__ - 1:
                if vhost_lookup in vhost_readlines[num]:
                    vindex = num
                    break
                num += 1
            try:
                print(vindex)
            except Exception:
                print('ERROR : vLOOKUP not found.')
            with open(vhost_path, 'w+') as vhost_book:
                new_data = '\n\n' + TemplateContent
                vhost_readlines.insert(vindex + 1, new_data)
                vhost_book.writelines(vhost_readlines)
    print("VHosts file updated")
    while True:
        backup = input(f'Do you also want a copy in {OutputFolder} folder? (y/n) :').lower()
        if backup == 'y' or backup == 'n':
            break
    if backup == 'y':
        print(f'Saving it to {InputSvrName}.txt in {OutputFolder} folder')
        open(f'../{OutputFolder}/{InputSvrName}.txt', 'w+').write(TemplateContent)

else:
    print(f'Saving it to {InputSvrName}.txt in {OutputFolder} folder')
    open(f'../{OutputFolder}/{InputSvrName}.txt', 'w+').write(TemplateContent)

if input('Do you want to add host entry? (y/ANYTHING) :').lower() == 'y':
    host_book = open(host_path, 'r+')
    host_readlines = host_book.readlines()
    num = 0
    new_data = f'\n127.0.0.1 {InputSvrName}\n'
    if lookup != '':
        while num < host_readlines.__len__() - 1:
            if lookup in host_readlines[num]:
                index = num
                break
            num += 1
        host_book.close()
        try:
            print(index)
        except Exception:
            print('ERROR : LOOKUP not found.')
        with open(host_path, 'w+') as host_book:
            host_readlines.insert(index + 1, new_data)
            host_book.writelines(host_readlines)
    else:
        with open(host_path, 'a') as host_book:
            host_book.write(new_data)


    print("Hosts file updated")

print('ALL DONE, have a great time!')
input('Enter any key to close the program ...\n')