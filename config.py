import toml
import tomllib
config_filepath = 'config.toml'


class MyConfigClass:
    with open('config.toml', 'r') as f:
        config = toml.load(f)

    DATABASE_CONFIG = config['database']
    IMAGE_VALIDATION_CONFIG = config['image_validation']

    def validation_setting(self):
        with open('config.toml', 'rb') as toml_file:
            config = tomllib.load(toml_file)
            self.image_size = config.get('image_validation')['image_size']
            self.image_format = config.get('image_validation')['image_format']
            self.image_size_error = config.get('image_validation')[
                'image_size_error']
            self.image_format_error = config.get('image_validation')[
                'image_format_error']
            self.image_empty_error = config.get('image_validation')[
                'image_empty_error']
            return self
