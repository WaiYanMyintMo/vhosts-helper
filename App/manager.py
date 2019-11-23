# //Must Have Outline
# Host and Vhost assigned at top of file.
# Server Name and DocumentRoot assigned at top of file.
# Function for opening file, reading and returning replaced data.
# Function for appending data to a file.
from configurer import get_keyword_config_matched as get_keyword_config
from configurer import get_editor_config_matched as get_editor_config
from configurer import get_template_config_matched as get_template_config
from themer import theme
from editor import edit as edit_low, read, output


def edit_hosts(hosts_path: str, hosts_template_path: str, keyword_config: dict, update_type: str, update_option: str):

    hosts_template = read(hosts_template_path)
    hosts_data = theme(hosts_template, keyword_config)
    edit_low(hosts_path, hosts_data, update_type, update_option)

    return hosts_data


def edit_vhosts(vhosts_path :str, vhosts_template_path: str, keyword_config: dict,
                update_type: str, update_option: str):

    vhosts_template = read(vhosts_template_path)
    vhosts_data = theme(vhosts_template, keyword_config)
    edit_low(vhosts_path, vhosts_data, update_type, update_option)

    return vhosts_data


def edit_main():
    # Get data from config
    hosts_template_path, vhosts_template_path, edit_type, edit_option = get_template_config()

    hosts_path, vhosts_path, edit_includes, saves_to_output, output_path, server_name = get_editor_config()

    keyword_config = get_keyword_config()
    include_hosts, include_vhosts = False, False
    # Logic for selection
    if edit_includes.title() == 'Both':
        include_hosts = True
        include_vhosts = True
    elif edit_includes.title() == 'Hosts':
        include_hosts = True
    elif edit_includes.title() == 'Vhosts':
        include_vhosts = True
    if include_hosts:
        try:
            hosts_data = edit_hosts(hosts_path, hosts_template_path, keyword_config, edit_type, edit_option)
        except PermissionError:
            print("\nHosts file can't be edited because of insufficient permission")
            print("Please re-run this program as administrator, didn't I warn you?")
            input('Do you understand what happened? Press any key to exit program ...\n')
            import sys
            sys.exit()
    if include_vhosts:
        vhosts_data = edit_vhosts(vhosts_path, vhosts_template_path, keyword_config, edit_type, edit_option)
    if saves_to_output:
        output_path = output_path + server_name + '.txt'
        if include_hosts == True and include_vhosts:
            hosts_data = '\n' + hosts_data
            vhosts_data = '\n' + vhosts_data
            output(output_path, hosts_data)
            edit_low(output_path, vhosts_data)
            return hosts_data, vhosts_data
        elif include_hosts:
            hosts_data = '\n' + hosts_data
            output(output_path, hosts_data)
            return hosts_data
        elif include_vhosts:
            vhosts_data = '\n' + vhosts_data
            output(output_path, vhosts_data)
            return vhosts_data
    else:
        return None



# leftover_config = {'PathName': 'HostsPath',
#                    'UpdateLocationType': '"",str',
#                    'UpdateLocation': '',
#                    'UnspecifiedLocationTypes': '"End", "Start"',
#                    'UnspecifiedLocation': 'End'}
