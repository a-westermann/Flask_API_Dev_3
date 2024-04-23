from configparser import ConfigParser


def read_config(environment, filename='database.ini'):
    ini_parser = ConfigParser()
    ini_parser.read(filename)

    config = {}
    if ini_parser.has_section(environment):
        print(f'Environment: {environment}')
        params = ini_parser.items(environment)
        for param in params:
            config[param[0]] = param[1]
            print(param)
    else:
        raise Exception(f'Section {environment} not present in the {filename} file.')

    return config
