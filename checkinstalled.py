from os import path
from shutil import which


class CheckInstalled:
    # Method to check if driver is installed
    def check_driver(self):
        driver_path = str(r'C:\Program Files (x86)\G&D')
        if path.exists(driver_path):
            return True
        return False

    # Method to check if CSP is installed
    def check_csp(self):
        csp_path = str(r'C:\ProgramData\A.E.T. Europe B.V\SafeSign')
        if path.exists(csp_path):
            return True
        return False

    # Method to check if PjeOffice is installed
    def check_pje(self):
        pje_path = str(r'C:\Program Files (x86)\pje-office')
        if path.exists(pje_path):
            return True
        return False

    # Method to check Mozilla is installed
    def check_firefox(self):
        mozilla_path = str(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        if path.exists(mozilla_path):
            return True
        return False

    # Method to check if Java is installed
    def check_java(self):
        java_path = which('Java')
        if java_path is not None:
            return True
        return False

