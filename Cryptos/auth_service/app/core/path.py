import os


def get_path_env():
    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    env_file_path: str = os.path.abspath(os.path.join(
        base_dir,
        '..', '..', '..', '..',
        'settings', '.env')
    )

    return env_file_path


def get_path_toml():
    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    env_file_path: str = os.path.abspath(os.path.join(
        base_dir,
        '..', '..', '..', '..',
        'settings', 'config.toml')
    )
    return env_file_path


path_env_file = get_path_env()
path_toml_file = get_path_toml()
