import glob


def get_infrastructures(path_to_yaml_files='yaml-files/*'):
    yaml_files = glob.glob(path_to_yaml_files)
    infrastructures = list()
    for file in yaml_files:
        infrastructures.append(file.split('\\')[1].strip('.yaml'))
    return infrastructures




