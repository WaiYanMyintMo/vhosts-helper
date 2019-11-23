def tryyaml():
    try:
        import yaml
    except ImportError:
        import os
        os.system("pip install pyyaml")


tryyaml()
import yaml


def get_config_path(arg) -> str:
    if arg == '':
        config_path = '..\\Config\\config.yaml' #default path
    else:
        config_path = arg
    return config_path


def get_config(arg) -> dict:
    config_path = get_config_path(arg)
    try:
        with open(config_path, 'r') as file:
            config = yaml.full_load(file)
    except FileNotFoundError:
        print("\nCan't find config.yaml, are you sure you are running this from within App folder")
        print("You didn't run it from the app folder. Didn't I warn you?")
        input("Do you understand what happened? Press any key to exit program...\n")
        import sys
        sys.exit()
    return config


def get_editor_config(config: dict) -> dict:
    editor_config = config['editor_config']
    return editor_config


def get_raw_keyword_config(config: dict) -> dict:
    keyword_config = config['keyword_config']
    return keyword_config


def get_keyword_config(config: dict) -> dict:
    editor_config = get_editor_config(config)
    keyword_config = get_raw_keyword_config(config)
    for i in keyword_config.keys():
        x = keyword_config.get(i)
        if len(x) > 0:
            if x[0] == '$':
                u = x[1:]
                if u in editor_config.keys():
                    keyword_config[i] = editor_config[u]
                else:  # Dunno what I did, but this handles the $
                    keyword_config[i] = u  #without any error
    return keyword_config


def get_template_config(config: dict) -> dict:
    template_path = config['template_config']
    return template_path


def configurer(option: str, arg) -> dict:
    config = get_config(arg)
    if option == 'editor':
        return get_editor_config(config)
    elif option == 'keyword':
        return get_keyword_config(config)
    elif option == 'template':
        return get_template_config(config)
    elif option == 'config':
        return config
    else:
        raise Exception


def get_template_config_matched(arg) -> str:
    template_config = configurer('template', arg)
    hosts_template_path = template_config['HostsTemplatePath']
    vhosts_template_path = template_config['VhostsTemplatePath']
    update_type = template_config['EditType']
    update_option = template_config['EditOption']
    return hosts_template_path, vhosts_template_path, update_type, update_option


def get_editor_config_matched(arg) -> str:
    editor_config = configurer('editor', arg)
    hosts_path = editor_config['HostsPath']
    vhosts_path = editor_config['VhostsPath']
    edit_includes = editor_config['EditIncludes']
    saves_to_output = editor_config['SavesToOutput']
    output_path = editor_config['OutputPath']
    server_name = editor_config['ServerName']
    return hosts_path, vhosts_path, edit_includes, saves_to_output, output_path, server_name


def get_keyword_config_matched(arg) -> dict:
    keyword_config = configurer('keyword', arg)
    return keyword_config



def main():
    option = 'keyword'
    x = configurer(option)
    print(x)


if __name__ == '__main__':
    main()
