#!/usr/bin/python3
import fabric
import datetime
import os


def do_pack():
    fabric.api.local("mkdir -p versions")
    name_file = "versions/web_static_{:s}.tgz".format(
        datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    create_file = fabric.api.local(
        "tar -cvzf {:s} web_static".format(name_file))
    if os.path.isfile(name_file):
        print("web_static packed: {:s} -> {}Bytes".format(
            name_file, os.path.getsize(name_file)))
        return name_file
    else:
        return None
