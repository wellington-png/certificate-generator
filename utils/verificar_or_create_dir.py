import os


def create_dir_curso(nome):
    if nome in os.listdir('certificado'):
        return
    else:
        os.system(f'mkdir certificado/{nome}')