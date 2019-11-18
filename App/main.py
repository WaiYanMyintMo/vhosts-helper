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



def main():
    hosts_template, vhosts_template, update_type, update_option = get_template_config()
    keyword_config = configurer('keyword')
    data = theme(vhosts_template, keyword_config)
    print(data)
    edit(edit_path, data, update_type, update_option)



if __name__ == '__main__':
    main()

# leftover_config = {'PathName': 'HostsPath',
#                    'UpdateLocationType': '"",str',
#                    'UpdateLocation': '',
#                    'UnspecifiedLocationTypes': '"End", "Start"',
#                    'UnspecifiedLocation': 'End'}
