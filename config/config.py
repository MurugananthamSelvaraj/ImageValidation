import toml
config_filepath = 'config\config.toml'


class Configfiles:
    with open(config_filepath, 'r') as f:
        config = toml.load(f)

    DATABASE_CONFIG = config['database']
