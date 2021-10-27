from os import path, system
from subprocess import run


def check_file(name):
    if path.exists(name):
        return True
    return False


def install_packet(name):
    try:
        run(name)
        return [True, "{} foi instalado com sucesso!".format(name)]
    except Exception as err:
        return [False, "Não foi possível instalar o {}".format(name), err]


def remove_file(name):
    system('del "{}"'.format(name))
