#!/usr/bin/python3
"""fabfile to create an archive of web_static contents"""

from os import path
from datetime import datetime
from fabric.api import local


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
