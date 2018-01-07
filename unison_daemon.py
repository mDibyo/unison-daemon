#!/usr/bin/env python

import os.path as osp
import subprocess

PREFERENCE_FILE_TEMPLATE = """\
root = {local_root}
root = ssh://{remote_host}/{remote_root}
sshargs = -C
perms = 0
repeat = watch
terse = true
"""

UNISON_DIRECTORY = osp.expanduser('~/.unison')

LOCAL_BASE = osp.expanduser('~/workspace')
REMOTE_BASE = '/mnt/d/workspace'


def create_remote_root(remote_host, root):
    remote_cmd = 'mkdir {}'.format(osp.join(REMOTE_BASE, root))
    subprocess.check_call(' '.join([
        'ssh', remote_host,
        '-C', '"{}"'.format(remote_cmd),
    ]), shell=True)


def create_preference_file(remote_host, name, root):
    filename = osp.join(UNISON_DIRECTORY, '{}.prf'.format(name))
    with open(filename, 'x') as f:
        f.write(PREFERENCE_FILE_TEMPLATE.format(
            local_root=osp.join(LOCAL_BASE, root),
            remote_root=osp.join(REMOTE_BASE, root),
            remote_host=remote_host,
        ))


REMOTE_HOST = 'surface'


if __name__ == '__main__':
    import sys

    name = sys.argv[1]
    root = sys.argv[2]
    create_remote_root(REMOTE_HOST, root)
    create_preference_file(REMOTE_HOST, name, root)
