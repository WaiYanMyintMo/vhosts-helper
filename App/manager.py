# //Must Have Outline
# Host and Vhost assigned at top of file.
# Server Name and DocumentRoot assigned at top of file.
# Function for opening file, reading and returning replaced data.
# Function for appending data to a file.
from configurer import configurer
from themer import theme
from editor import edit as edit_low, read


def get_template_config() -> str:
    template_config = configurer('template')
    hosts_template_path = template_config['HostsTemplatePath']
    vhosts_template_path = template_config['VhostsTemplatePath']
    update_type = template_config['UpdateType']
    update_option = template_config['UpdateOption']
    return hosts_template_path, vhosts_template_path, update_type, update_option


def get_editor_config() -> str:
    editor_config = configurer('editor')
    hosts_path = editor_config['HostsPath']
    vhosts_path = editor_config['VhostsPath']
    edit_includes = editor_config['EditIncludes']
    return hosts_path, vhosts_path, edit_includes


def get_keyword_config():
    keyword_config = configurer('keyword')
    return keyword_config


def edit_hosts(hosts_path: str, hosts_template_path: str, keyword_config: dict,
               update_type: str = 'append', update_option: str = '-'):

    hosts_template = read(hosts_template_path)
    hosts_data = theme(hosts_template, keyword_config)
    edit_low(hosts_path, hosts_data, update_type, update_option)


def edit_vhosts(vhosts_path :str, vhosts_template_path: str, keyword_config: dict,
                update_type: str = 'append', update_option: str = '-'):

    vhosts_template = read(vhosts_template_path)
    vhosts_data = theme(vhosts_template, keyword_config)
    edit_low(vhosts_path, vhosts_data, update_type, update_option)


def edit_main():
    # Get data from config
    hosts_template_path, vhosts_template_path, update_type, update_option = get_template_config()

    hosts_path, vhosts_path, edit_includes = get_editor_config()

    keyword_config = get_keyword_config()

    # Logic for selection
    if edit_includes.title() == 'Both':
        include_vhosts = True
        include_hosts = True
    elif edit_includes.title() == 'Vhosts':
        include_vhosts = True
    elif edit_includes.title() == 'Hosts':
        include_hosts = True
    if include_hosts:
        edit_hosts(hosts_path, hosts_template_path, keyword_config, update_type='append', update_option='-')
    if include_vhosts:
        edit_vhosts(vhosts_path, vhosts_template_path, keyword_config, update_type='append', update_option='-')


def start():
    print('Vhosts Helper - Stiles-X\n')
    print('ServerName, DocumentRoot and Port No. MUST be edited in Config/config.yaml')
    print('You are RECOMMENDED to read the templates and MUST edit them to suit your needs')
    print('Reading through the config file RECOMMENDED before using the program')
    print('Note: You MUST run program with Administrator rights. Reason: Hosts File')
    print('\nDo you accept that all responsibilties is solely yours?')
    input('And that you have read through the config file?')
    print('Program is starting ...')
    edit_main()
    print('\nProgram is successfully executed')
    print('No guarantee that program executed successfully')
    input('Press anything to exit the program ...')

# leftover_config = {'PathName': 'HostsPath',
#                    'UpdateLocationType': '"",str',
#                    'UpdateLocation': '',
#                    'UnspecifiedLocationTypes': '"End", "Start"',
#                    'UnspecifiedLocation': 'End'}
