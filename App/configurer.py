import yaml
config_path = '..\\Config\\config.yaml'


def get_config() -> dict:
    with open(config_path, 'r') as file:
        config = yaml.full_load(file)
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
        if x[0] == '$':
            u = x[1:]
            if u in editor_config.keys():
                keyword_config[i] = editor_config[u]
    return keyword_config


def configurer(option: str):
    config = get_config()
    if option == 'editor':
        return get_editor_config(config)
    elif option == 'keyword':
        return get_keyword_config(config)
    elif option == 'config':
        return config
    else:
        raise Exception


def main():
    option = 'keyword'
    x = configurer(option)
    print(x)


if __name__ == '__main__':
    main()
