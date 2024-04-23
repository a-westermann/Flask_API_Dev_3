from configparser import ConfigParser


def read_config(filename='database.ini', section='postgresql'):
    ini_parser = ConfigParser()
    ini_parser.read(filename)

    config = {}
    if parser.has_section(section):
        print(f'{section}\n')
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
            print(param)
    else:
        raise Exception(f'Section {section} not present in the {filename} file.')

    return config


if __name__ == '__main__':
    config = read_config()
    print(config)
