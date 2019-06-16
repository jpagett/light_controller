import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.1.0"

include_files = ['light_white.png']
packages = ["os", "sys", "random","time"]
excludes = ["tkinter"]

setup(
    name = "Light Controller",
    description='Controls the Luminoodle Professional Bias Lighting strip.',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("lights_gui.py",base="Win32GUI")]
)
