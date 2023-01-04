def create_cfg(file: str, cfg_dict: dict):
    """
    English:
    ----------
    Creates a configuration file from a dictionary. Note: the names of the options must be lowercase.

    Parameters
    ----------
    file : str
        The path to the configuration file to be created.
    cfg_dict : dict
        The dictionary containing the settings to be written to the file. The key of the dictionary is the name of the section, and the value is a dictionary with the options of the section and their respective values.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Cria um arquivo de configuração a partir de um dicionário. Obs.: os nomes das opções devem ser minúsculos.

    Parâmetros
    ----------
    file : str
        O caminho para o arquivo de configuração a ser criado.
    cfg_dict : dict
        O dicionário que contém as configurações a serem escritas no arquivo. A chave do dicionário é o nome da seção, e o valor é um dicionário com as opções da seção e seus respectivos valores.

    Retorna
    -------
    None
    """
    with open(file, 'w') as file:
        for section, options in cfg_dict.items():
            file.write(f'\n[{section}]\n')
            for option, value in options.items():
                file.write(f'{option}={value}\n')


def read_cfg(file: str):
    """
    English:
    ----------
    Reads a .cfg configuration file and returns the options as a dictionary.

    Parameters
    ----------
    file : str
        The name of the configuration file to be read.

    Returns
    -------
    options : dict
        A dictionary containing the options and their values, organized by section.

    Português (brasileiro):
    ----------
    Lê um arquivo de configuração no formato .cfg e retorna as opções como um dicionário.

    Parâmetros
    ----------
    file : str
        O nome do arquivo de configuração a ser lido.

    Retorna
    -------
    options : dict
        Um dicionário contendo as opções e seus valores, organizados por seção.
    """
    from configparser import ConfigParser

    config = ConfigParser()

    config.read(file)
    sections = config.sections()

    sections_dict = dict()
    for section in sections:
        options = config.options(section)
        options_dict = dict()

        for option in options:
            value = config.get(section, option)
            options_dict[option] = value

        sections_dict[section] = options_dict

    return sections_dict


def backup(file: str, output_path: str = '', backup_name: str = ''):
    """
    English:
    ----------
    Makes a backup of a file.

    Parameters
    ----------
    file : str
        The path to the file that will be copied.
    output_path : str
        The path where the backup will be saved. The default is an empty string.
    backup_name : str
        The name of the backup. If not provided, the name will be the current date and time.

    Returns
    -------
    None

    Português (brasileiro):
    ----------
    Realiza uma cópia de segurança de um arquivo.

    Parâmetros
    ----------
    file : str
        O caminho para o arquivo que será copiado.
    output_path : str
        O caminho onde a cópia de segurança será salva. O padrão é uma string vazia.
    backup_name : str
        O nome da cópia de segurança. Se não for informado, o nome será a data e hora atual.

    Retorna
    -------
    None
    """
    import shutil

    if backup_name == '':
        from datetime import datetime

        try:
            extension = file[file.rindex('.'):]
        except ValueError:
            extension = ''

        backup_name = datetime.now().strftime("%Y-%m-%d %Hh%M") + extension

    if len(output_path) > 0 and (output_path[-1] != '\\'
                                 or output_path[-1] != '/'):
        output_path += '/'

    try:
        shutil.copy(file, output_path + backup_name)
    except FileNotFoundError:
        try:
            import os

            os.makedirs(output_path)
        except PermissionError:
            print(
                'Caminho informado não existe. Criação de diretório não foi autorizado.\nAjuste a permissão do algoritmo ou crie manualmente a pasta de destino.'
            )
    finally:
        shutil.copy(file, output_path + backup_name)


def check_hash(*files):
    """
    English:
    ----------
    Checks the integrity of multiple files by comparing their hashes, or returns the hash if a single file is provided.

    Parameters
    ----------
    *files : list
        The path to the files to be checked.

    Returns
    -------
    bool (if more than one file was provided)
        If the check was successful.
    str (if a single file was provided)
        The hash of the provided file.

    Português (brasileiro):
    ----------
    Verifica a integridade de vários arquivos comparando seus hashes, ou retorna o hash caso um único arquivo seja informado.

    Parâmetros
    ----------
    *files : list
        O caminho para os arquivos a serem verificados.

    Retorna
    -------
    bool (caso mais de um arquivo tiver sido fornecido)
        Se a verificação foi realizada com sucesso.
    str (caso um único arquivo foi fornecido)
        O hash do arquivo informado.
    """
    import hashlib

    if len(files) > 1:
        for file in files:
            with open(file, 'rb') as f:
                hasher = hashlib.sha256()
                hasher.update(f.read())
                try:
                    if hash == hasher.digest():
                        continue
                    else:
                        return False
                except UnboundLocalError:
                    hash = hasher.digest()
                    continue
        return True

    else:
        with open(files[0], 'rb') as f:
            hasher = hashlib.sha256()
            hasher.update(f.read())
            hash = hasher.hexdigest()
            return hash