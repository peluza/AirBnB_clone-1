#!/usr/bin/python3
"""packs and distributes an archive to two web servers"""
from fabric.api import *
from datetime import datetime
from os.path import isfile, getsize

env.hosts = ['35.190.152.71', '34.75.218.253']


def do_pack():
    """generates a .tgz archive from the contents of the web_static
        folder of your AirBnB Clone repo, using the function do_pack.

        Returns:
        path: the archive path if the archive has been correctly generated.
    """
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


def deploy():
    """creates and distributes an archive to your web servers

    Returns:
        funtion: distributes an archive to your web servers
    """
    path = do_pack()
    if path is not None:
        return do_deploy(path)
    else:
        return False


def do_deploy(archive_path):
    """distributes an archive to your web servers, using the function do_deploy

        Returns:
        booleano: False if the file at the path archive_path doesn’t exist
                Returns True if all operations have been done correctly,
    """

    if isfile(archive_path):
        pre_path = archive_path.split("/")[1]
        put(archive_path, "/tmp/")
        tmp_path = "/tmp/" + pre_path
        releases_path = "/data/web_static/releases/" + pre_path.split(".")[0]
        sudo("mkdir -p {:s}".format(releases_path))
        sudo("tar -xzf {:s} -C {:s}".format(tmp_path, releases_path))
        sudo("rm {:s}".format(tmp_path))
        all_path_w = releases_path + "/web_static/*"
        dictory_path = releases_path + "/web_static/"
        sudo("mv {:s} {:s}".format(all_path_w, releases_path))
        sudo("rm -rf {:s}".format(dictory_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    else:
        return False


def do_clean(number=0):
    """deletes out-of-date archives, using the function do_clean

        Args:
            number (int, optional): is the number of the archives
    """
    if int(number) <= 1:
        number = 1
    number = int(number) + 1
    with lcd("versions"):
        local("ls -1t | tail -n +{:d} | xargs rm -rf".format(number))
    with cd("/data/web_static/releases/"):
        sudo("ls -1t -I test | tail -n +{:d} | xargs rm -rf".format(number))
