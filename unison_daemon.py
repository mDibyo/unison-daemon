#!/usr/bin/env python

import os.path as osp

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
REMOTE_HOST = 'surface'


def create_preference_file(name, root):
    filename = osp.join(UNISON_DIRECTORY, '{}.prf'.format(name))
    with open(filename, 'x') as f:
        f.write(PREFERENCE_FILE_TEMPLATE.format(
            local_root=osp.join(LOCAL_BASE, root),
            remote_root=osp.join(REMOTE_BASE, root),
            remote_host=REMOTE_HOST,
        ))


if __name__ == '__main__':
    import sys
    create_preference_file(sys.argv[1], sys.argv[2])
