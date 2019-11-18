# //Must Have Outline
# Host and Vhost assigned at top of file.
# Server Name and DocumentRoot assigned at top of file.
# Function for opening file, reading and returning replaced data.
# Function for appending data to a file.
from configurer import configurer
from themer import theme
from editor import edit,read


def get_template_config():
    template_config = configurer('template')
    hosts = read(template_config['HostsTemplatePath'])
    vhosts = read(template_config['VhostsTemplatePath'])
    update_type = template_config['UpdateType']
    update_option = template_config['UpdateOption']
    return hosts, vhosts, update_type, update_option


def get_editor_config():
    editor_config = configurer('editor')
    hosts_path = editor_config['HostsPath']
    vhosts_path = editor_config['VhostsPath']
    return hosts_path, vhosts_path


def main():
    hosts_template, vhosts_template, update_type, update_option = get_template_config()
    hosts_path, vhosts_path = get_editor_config()

    keyword_config = configurer('keyword')
    hosts_data = theme(hosts_template, keyword_config)
    vhosts_data = theme(vhosts_template, keyword_config)

    edit(hosts_path, hosts_data, update_type='append', update_option='-')
    edit(vhosts_path, vhosts_data, update_type='append', update_option='-')


if __name__ == '__main__':
    print('Vhosts Helper - Stiles-X\n')
    print('ServerName, DocumentRoot and Port No. MUST be edited in Config/config.yaml')
    print('You are RECOMMENDED to read the templates and MUST edit them to suit your needs')
    print('Reading through the config file RECOMMENDED before using the program')
    print('Note: You MUST run program with Administrator rights. Reason: Hosts File')
    print('\nDo you accept that all responsibilties is solely yours?')
    input('And that you have read through the config file?')
    print('Program is starting ...')
    main()
    print('\nProgram is successfully executed')
    print('No guarantee that program executed successfully')
    input('Press anything to exit the program ...')

# leftover_config = {'PathName': 'HostsPath',
#                    'UpdateLocationType': '"",str',
#                    'UpdateLocation': '',
#                    'UnspecifiedLocationTypes': '"End", "Start"',
#                    'UnspecifiedLocation': 'End'}
