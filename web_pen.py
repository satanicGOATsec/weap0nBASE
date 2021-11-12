#!/usr/bin/python3
from rich import print as rp
## import the identify
import os
from colorama import Fore as fore
import sys
from core import console
if sys.argv[1] == "console":
    rp("[ [dim]default[/dim] ] console mode.")
    console()
    
else:
    exit(1)    
