import config as cfg
from itertools import count
import subprocess
import os

def process_drop_input(path):
    new_file = File(path)
    cfg.file_list.append(new_file)

def decompress(file):
    print('FileDB/FileDBReader.exe decompress -f "'+str(file)+'" -y')
    subprocess.run('FileDB/FileDBReader.exe decompress -f "'+str(file)+'" -y')

def compress(file):
    print('FileDB/FileDBReader.exe compress -f "'+str(file)+'" -y')
    subprocess.run('FileDB/FileDBReader.exe compress -f "'+str(file)+'" -y')

def fctohex(file):
    print('FileDB/FileDBReader.exe fctohex -f "'+str(file)+'" -y')
    subprocess.run('FileDB/FileDBReader.exe fctohex -f "'+str(file)+'" -y')
    os.replace(file.title_raw + '_fcimport.xml', file.parentdir+file.title_raw+'.xml')

def hextofc(file):
    print('FileDB/FileDBReader.exe hextofc -f "'+str(file)+'" -y')
    subprocess.run('FileDB/FileDBReader.exe hextofc -f "'+str(file)+'" -y')
    os.replace(file.title_raw + '_fcexport.xml', file.parentdir + file.title_raw + '.fc')

def interpret(file):
    print('FileDB/FileDBReader.exe interpret -f "'+str(file)+'" -i "'+file.interpreter_i+'" -y')
    subprocess.run('FileDB/FileDBReader.exe interpret -f "'+str(file)+'" -i "'+file.interpreter_i+'" -y')

def tohex(file):
    print('FileDB/FileDBReader.exe toHex -f "'+str(file)+'" -i "'+file.interpreter_h+'" -y')
    subprocess.run('FileDB/FileDBReader.exe toHex -f "'+str(file)+'" -i "'+file.interpreter_h+'" -y')

def check_fileversion(file):
    version_string = subprocess.run('FileDB/FileDBReader.exe check_fileversion -f "'+str(file)+'" ', capture_output=True).stdout.decode('ascii')
    print(version_string)
    version = version_string[version_string.rfind('Version ')+8:]
    return version

class File:
    uidgen = count(0)

    def __init__(self, path):
        self.id = next(File.uidgen)
        self.path = path
        self.parentdir = path[:path.rfind('\\')+1]
        self.title = '.../' + path[1+path.rfind('\\'):]
        self.title_raw = path[1+path.rfind('\\'):path.rfind('.')]
        self.type = path[path.rfind('.'):]
        self.version = '?'
        try:
            self.version = check_fileversion(self)
        except:
            pass

        self.actions = [0, 0, 0, 0]

        self.interpreter_i = 0
        self.interpreter_h = 0

    def __eq__(self, other):
        if type(self) is type(other):
            return self.id == other.id
        return False

    def __str__(self):
        return self.path

def process_files():
    def process_file(file):
        actions = [decompress, compress, fctohex, hextofc, interpret, tohex]
        file_action_settings = file.actions + [file.interpreter_i != 0, file.interpreter_h != 0]
        for (action, active) in zip(actions, file_action_settings):
            if active:
                action(file)
    for file in cfg.file_list:
        process_file(file)