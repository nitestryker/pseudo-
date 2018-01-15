#setup.py
from cx_Freeze import setup, Executable
setup( name = "pseudo",
       version = "0.1",
       description = "an anonymous bbs / messaging system",
       executables = [Executable("pseudo.py")] )