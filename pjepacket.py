#!/usr/bin/env python
# -*- coding: utf-8 -*-
import checkinstalled
import downloadhandler
import api_file
import platform


if __name__ == "__main__":
    # System information
    os = platform.system()  # Operational System
    arch = platform.machine()   # CPU architecture
    version = platform.platform()   # Operational System version and details
    # remove file list
    remove_list = []
    # File names
    # Java
    java_name = 'Java.exe'
    # Mozilla FireFox
    firefox_name = 'Firefox Installer.exe'
    # PJE office
    pje_name = 'PjeOffice.exe'
    if arch == 'AMD64':
        # Drive name
        drive_name = 'GDsetupStarsignCUTx64.exe'
        # CSP name
        csp_name = 'SafeSignIC30124-x64-win-tu-admin.exe'
    # Arch i386 or 32 - bits
    else:
        # Drive name
        drive_name = 'GDsetupStarsignCUTx32.exe'
        # CSP name
        csp_name = 'SafeSignIC30124-x86-win-tu-admin.exe'

    # object to verify installed packets
    install_check = checkinstalled.CheckInstalled()
    # object for packets downloads
    download_packets = downloadhandler.DownloadHandler(arch)
    # check if driver is not installed
    if not install_check.check_driver():
        # check if driver alredy not downloaded
        if not api_file.check_file(drive_name):
            print("Baixando o Driver {}:".format(drive_name))
            # download driver and save result
            driver = download_packets.download_driver(drive_name)
            # driver download succesfully
            if driver[0]:
                print(driver[1])
                # driver will be delete
                remove_list.append(drive_name)
            # driver download error
            else:
                print(driver[1])
                # error
                print(driver[2])
        # Install driver
        try:
            driver_install = api_file.install_packet(drive_name)
            if driver_install[0] and install_check.check_driver():
                print(driver_install[1] + '\n')
            elif not driver_install[0]:
                print(driver_install[1])
                raise driver_install[2]
            else:
                print("Houve algum erro durante a instalação do Driver!")
                raise Exception
        except Exception as err:
            print(str(err) + '\n')
    # check if CSP is not installed
    if not install_check.check_csp():
        # check if CSP alredy not downloaded
        if not api_file.check_file(csp_name):
            print("Baixando o CSP {}:".format(csp_name))
            # download CSP and save result
            csp = download_packets.download_csp(csp_name)
            if csp[0]:
                print(csp[1])
                # CSP will be delete
                remove_list.append(csp_name)
            else:
                print(csp[1])
                print(csp[2])
        # Install CSP
        try:
            csp_install = api_file.install_packet(csp_name)
            if csp_install[0] and install_check.check_csp():
                print(csp_install[1] + '\n')
            elif not csp_install[0]:
                print(csp_install[1])
                raise csp_install[2]
            else:
                print("Houve algum erro durante a instalação do CSP!")
                raise Exception
        except Exception as err:
            print(str(err) + '\n')
    # check if Java is not installed
    if not install_check.check_java():
        if not api_file.check_file(java_name):
            print("Baixando o Java:")
            java = download_packets.download_java(java_name)
            if java[0]:
                print(java[1])
                # java will be delete
                remove_list.append(java_name)
            else:
                print(java[1])
                print(java[2])
        # Install Java
        try:
            java_install = api_file.install_packet(java_name)
            if java_install[0] and install_check.check_java():
                print(java_install[1] + '\n')
            elif not java_install[0]:
                print(java_install[1])
                raise java_install[2]
            else:
                print("Houve algum erro durante a instalalção do Java!")
                raise Exception
        except Exception as err:
            print(str(err) + '\n')
    # check if mozilla is not installed
    if not install_check.check_firefox():
        if not api_file.check_file(firefox_name):
            print("Baixando o Mozilla Firefox:")
            firefox = download_packets.download_mozilla(firefox_name)
            if firefox[0]:
                print(firefox[1])
                # firefox will be delete
                remove_list.append(firefox_name)
            else:
                print(firefox[1])
                print(firefox[2])
        # Install Mozilla Firefox
        try:
            firefox_install = api_file.install_packet(firefox_name)
            if firefox_install[0] and install_check.check_firefox():
                print(firefox_install[1] + '\n')
            elif not firefox_install[0]:
                print(firefox_install[1])
                raise firefox_install[2]
            else:
                print("Houve algum erro durante a instalação do Mozilla Firefox!")
                raise Exception
        except Exception as err:
            print(str(err) + '\n')
    # check if PjeOffice is not installed
    if not install_check.check_pje():
        if not api_file.check_file(pje_name):
            print("Baixando o PJeOffice")
            pje = download_packets.download_pje_office(pje_name)
            if pje[0]:
                print(pje[1])
                # PjeOffice will be delete
                remove_list.append(pje_name)
            else:
                print(pje[1])
                print(pje[2])
        try:
            pje_install = api_file.install_packet(pje_name)
            if pje_install[0] and install_check.check_pje():
                print(pje_install[1] + '\n')
            elif not pje_install[0]:
                print(pje_install[1])
                raise pje_install[2]
            else:
                print("Houve algum erro durante a instalação do PJeOffice!")
                raise Exception
        except Exception as err:
            print(str(err) + '\n')

    # delete downloaded files
    for i in remove_list:
        api_file.remove_file(i)
