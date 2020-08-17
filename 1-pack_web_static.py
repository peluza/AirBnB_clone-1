#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack.

    Returns:
        path: the archive path if the archive has been correctly generated.
    """
from fabric.api import local
from fabric.decorators import runs_once
from datetime import datetime
from os.path import isfile, getsize


@runs_once
def do_pack():
    local("mkdir -p versions")
    name_file = "versions/web_static_{:s}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    local("tar -cvzf {:s} web_static".format(name_file))
    if isfile(name_file):
        print("web_static packed: {:s} -> {}Bytes".format(
            name_file, getsize(name_file)))
        return name_file
    else:
        return None
