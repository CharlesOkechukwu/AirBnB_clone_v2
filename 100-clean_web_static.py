#!/usr/bin/python3
"""delete old or outdated archives both on remote
and local systems
"""
import os
from fabric.api import lcd, local, run, cd, env

env.hosts = ["54.209.208.34", "54.87.234.46"]


def do_clean(number=0):
    """delete all old files in a folders both in remote server and
    on local device
    """
    number = int(number)
    if number == 0:
        number = 1
    with lcd("versions"):
        files = local("ls -td web_static_*", capture=True)
        f_list = files.split()
        delete = f_list[number:]
        for folder in delete:
            local("rm -f {}".format(folder))

    with cd("/data/web_static/releases"):
        folders = run("ls -td web_static_*")
        f_list = folders.split()
        old = f_list[number:]
        for folder in old:
            run("rm -rf {}".format(folder))
