#!/usr/bin/python3
"""full archiving and deployment module to compress
files and unzip files
"""
from os import path
from datetime import datetime
from fabric.api import run, local, put, env


env.hosts = ["54.209.208.34", "54.87.234.46"]


def do_pack():
    """a fab task to generate an archive of all
    files in the web_static folder
    """
    date = datetime.now()
    time = date.strftime('%Y%m%d%H%M%S')
    arch = "versions/web_static_{}.tgz".format(time)
    if not path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    cmd = "cd web_static && tar -cvzf ../{} . && cd ..".format(arch)
    if local(cmd).failed is True:
        return None
    return arch


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
    if run("rm -rf {}".format(f_path)).failed:
        return False
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


def deploy():
    """compress web application static files using do_pack
    and deploy to server using do_deploy
    """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
