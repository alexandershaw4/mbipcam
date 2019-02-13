#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Rumps menu bar item for security ipcam selection.

Config ip cameras in view_ipcam.py

Simplest method to launch is to add an alias to ~/.bash_profile, e.g.

# alias the menubar ipc item
alias ipc='python ~/mbipcam/mbipc.py & disown'

then launch from the terminal with 'ipc'. Disowning means you can 
close the terminal without closing the manubar app.

AS
"""

import rumps
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    # try:
    #     # PyInstaller creates a temp folder and stores path in _MEIPASS
    #     base_path = sys._MEIPASS
    # except Exception:
    #     base_path = os.path.abspath(".")
    #base_path = '~/code/mbipcam/'

    # comment this line & uncomment above is bundling with pyinstaller
    base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)

rumps.debug_mode(True)

localfun = resource_path('view_ipcam.py')

@rumps.clicked('Back Camera')
def print_something(_):
	#os.system('python view_ipcam.py 0')
	os.system('python ' + localfun + ' 0')


@rumps.clicked('Front Camera')
def print_something(_):
	#os.system('python view_ipcam.py 1')
	os.system('python ' + localfun + ' 1')
	
@rumps.clicked('Quit')
def clean_up_before_quit(_):
    print('execute clean up code')
    rumps.quit_application()


app = rumps.App('IPC', menu=['Back Camera', 'Front Camera', 'Quit'], quit_button=None)
app.run()


