import os
os.system('title INSTALLING MODULES. . .')

try:
    import pystyle
    import base64
    import fade
    import console
    import requests
    import pathlib
    import sys
except ModuleNotFoundError:
    os.system('pip install pystyle')
    os.system('pip install pybase64')
    os.system('pip install fade')
    os.system('pip install console')
    os.system('pip install requests')
    os.system('pip install pathlib')
    os.system('pip install os-sys')
