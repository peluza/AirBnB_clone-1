#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    local("mkdir -p versions")
    name_file = "versions/web_static_{:s}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    create_file = local("tar -cvzf {:s} web_static".format(name_file))
    if os.path.isfile(name_file):
        print(name_file)
    else:
        return None
