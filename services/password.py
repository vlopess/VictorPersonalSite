import os
import sys


curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.split(rootPath)[0])
from repository.passwordRepository import passwordRepository

class PasswordController:
    def __init__(self):    
        pr = passwordRepository()
        self.map = pr.select()        