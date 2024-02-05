#!/usr/bin/python3
"""module to upload zip compressed file to remote server
using fabric
"""
from os import path
from fabric.api import env, put, run


env.hosts = ["54.209.208.34", "54.87.234.46"]


def do_deploy(archive_path):
    """deploy compressed web_static archive file using
    fabric and uncompress compressed files
    """
    if path.isfile(archive_path) is False:
        return False
    archive = archive_path.split("/")[-1]
    file_name = archive.split(".")[0]
    if put(archive_path, "/tmp/{}".format(archive)).failed is True:
        return False
    f_path = "/data/web_static/releases/{}/".format(file_name)
    if run("mkdir -p {}".format(f_path)).failed:
        return False
    if run("tar -xzf /tmp/{} -C {}".format(archive, f_path)).failed:
        return False
    if run("rm -f /tmp/{}".format(archive)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s {} /data/web_static/current".format(f_path)).failed:
        return False
    return True
