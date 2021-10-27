import contextlib
import progressbar
import urllib.request
from os import path, system


class DownloadHandler:
    def __init__(self, arch):
        # CPU Arch
        self.__arch = arch
        # Absolute local path
        self.__local_path = '{0}\\'.format(path.dirname(path.abspath(__file__)))
        # Java URL
        self.__java_url = 'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=243702_61ae65e088624f5aaa0b1d2d801acb16'
        # Mozilla Firefox URL
        self.__firefox_url = 'https://download.mozilla.org/?product=firefox-stub&os=win&lang=pt-BR&attribution_code=c291cmNlPXd3dy5nb29nbGUuY29tJm1lZGl1bT1yZWZlcnJhbCZjYW1wYWlnbj0obm90IHNldCkmY29udGVudD0obm90IHNldCkmZXhwZXJpbWVudD0obm90IHNldCkmdmFyaWF0aW9uPShub3Qgc2V0KSZ1YT1jaHJvbWU.&attribution_sig=774d9972789664be6672b065e7f33820ea1cb1e7bafb5ea8c6b2a4f4bc207c70'
        # Pje URL
        self.__pje_url = 'https://cnj-pje-programs.s3-sa-east-1.amazonaws.com/pje-office/PJeOffice.exe'
        # Drivers for StarSign Crypto Starsign CUT S (GD)
        # Arch AMD64 or 64 - bits
        if self.__arch == 'AMD64':
            # URL Drive
            self.__drive_url = 'https://drivers.certisign.com.br/midias/tokens/gdburti/64bits/2k-xp-vi-7/GDsetupStarsignCUTx64.exe?_ga=2.194196777.565501561.1609850436-273546220.1609850436'
            # CSP URL
            self.__csp_url = 'https://drivers.certisign.com.br/midias/gerenciadores/safesign/64bits/SafeSignIC30124-x64-win-tu-admin.exe?_ga=2.162094392.565501561.1609850436-273546220.1609850436'
        # Arch i386 or 32 - bits
        else:
            # URL Drive
            self.__drive_url = 'https://drivers.certisign.com.br/midias/tokens/gdburti/32bits/2k-xp-vi-7/GDsetupStarsignCUTx32.exe?_ga=2.194794665.565501561.1609850436-273546220.1609850436'
            # CSP URL
            self.__csp_url = 'https://drivers.certisign.com.br/midias/gerenciadores/safesign/32bits/SafeSignIC30124-x86-win-tu-admin.exe?_ga=2.2774964.565501561.1609850436-273546220.1609850436'

    # Method to download Driver of Token
    def download_driver(self, drive_name):
        # try download drive
        download = self.__download_file(self.__drive_url, drive_name)
        return download

    # Method to download CSP of Token
    def download_csp(self, csp_name):
        # try download CSP
        download = self.__download_file(self.__csp_url, csp_name)
        return download

    # Method to download Mozilla Firefox
    def download_mozilla(self, firefox_name):
        # try download Mozilla
        download = self.__download_file(self.__firefox_url, firefox_name)
        return download

    # Method to download Java
    def download_java(self, java_name):
        # try download Java
        download = self.__download_file(self.__java_url, java_name)
        return download

    # Method to download PjeOffice
    def download_pje_office(self, pje_name):
        # try download PjeOffice
        download = self.__download_file(self.__pje_url, pje_name)
        return download

    # Method for downloads
    def __download_file(self, url, file_name):
        # Path and name to the file
        file_path = self.__local_path + file_name
        # Try download the file
        try:
            # aliases file url
            with urllib.request.urlopen(url) as file_download:
                # size of the file
                file_size = int(file_download.getheader('Content-Length'))
                # Enable color to windows cmd
                system("color")
                # Progressbar
                bar = progressbar.ProgressBar(0, file_size)
                # Blocksize of download
                blocksize = max(4096, int(file_size) // 100)
                # aliases absolute path + name of file
                with open(file_path, 'wb') as file:
                    # aliases contextlib to help write blocks of download
                    with contextlib.closing(file_download) as fp:
                        # while exists blocks to download
                        while True:
                            # read block downloaded
                            file_data = fp.read(blocksize)
                            # there's no more data
                            if not file_data:
                                # out of loop
                                break
                            # write block
                            file.write(file_data)
                            # update progressbar
                            bar.update_progress(len(file_data))
            return [True, '{} foi baixado com sucesso!'.format(file_name)]
        except Exception as err:
            return [False, 'Erro! não foi possível baixar {}.'.format(file_name), err]
