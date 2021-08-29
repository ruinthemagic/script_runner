import subprocess
import os
import csv
from pprint import pprint

SCRIPTS_LIST = '/Users/liam/Desktop/script_runner/scripts_list.csv'

class Script_:
    def __init__(self, executable, execute_path, venv_path, script_path):
        self.executable = executable
        self.execute_path = execute_path
        self.venv_path = venv_path
        self.script_path = script_path
        
    def set_loc(self, execute_path = None):
        if execute_path:
            os.chdir(execute_path)
            print(os.getcwd())
        else:
            pass

    def set_venv(self, venv_path = None):
        if venv_path:
            os.system(f'source {venv_path}/bin/activate')
        else:
            pass


    def run_script(self, executable: str, script_path: str):
        os.system(f'{executable} {script_path}')

    def run_my_script(self):
        self.set_loc(self.execute_path)
        self.set_venv(self.venv_path)
        self.run_script(executable=self.executable, script_path=self.script_path)
        
def read_user_scripts():
    with open(SCRIPTS_LIST, 'r') as scripts:
        scripts = list(csv.DictReader(scripts, skipinitialspace=True))
    return scripts

def main():
    user_scripts = read_user_scripts()
    for script_ in user_scripts:
        s = Script_(
            executable=script_['executable'],
            execute_path=script_['execute_path'],
            venv_path=script_['venv_path'],
            script_path=script_['venv_path']
        )
        s.run_my_script()
    read_user_scripts()

main()