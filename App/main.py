varSetBook = open('VarSet.txt', 'r')
varSetContent = varSetBook.readlines()
varSetBook.close()
SvrName = varSetContent[0].strip('\n')
Dir = varSetContent[1].strip('\n')
OutputFolder = varSetContent[2].strip('\n')
vhost_path = varSetContent[3].strip('\n')
host_path = varSetContent[4].strip('\n')
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

print(f'....................\n\n {TemplateContent}')
print('\n.....................')
while True:
    Directness = input('Do you want to insert vhost directly? (y/n) :').lower()
    if Directness == 'y' or Directness == 'n':
        break
if Directness == 'y':
    with open(vhost_path, 'r+') as vhost_book:
        og_data = vhost_book.read()
        final_data = '\n\n' + TemplateContent
        vhost_book.write(final_data)
    print('Inserting done')
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
    lookup = r'########## custom url for xampp localhost ##############'
    num = 0
    while num < 50:
        if lookup in host_readlines[num]:
            index = num
            break
        num += 1
    host_book.close()

    with open(f'{host_path}\\hosts', 'w+') as host_book:
        new_data = f'127.0.0.1 {InputSvrName}\n'
        host_readlines.insert(index + 1, new_data)
        host_book.writelines(host_readlines)
    print("Hosts file updated")

print('ALL DONE, have a great time!')
input('Enter any key to close the program ...\n')