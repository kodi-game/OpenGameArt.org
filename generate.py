#!/usr/bin/env python3
################################################################################
#
#  Copyright (C) 2019 Garrett Brown
#  SPDX-License-Identifier: MIT
#
################################################################################

#
# Dependencies:
#
#   xmltodict - https://github.com/martinblech/xmltodict
#

import json
import os
import sys
import xmltodict


def main():
    directory = os.path.dirname(os.path.realpath(__file__))

    avatarcount = 0

    avatardir = os.path.join(directory, 'avatars')

    for avatarfolder in os.listdir(avatardir):
        avatarxmlpath = os.path.join(avatardir, avatarfolder, 'avatars.xml')
        avatarjsonpath = os.path.join(avatardir, avatarfolder, 'avatars.json')

        if os.path.exists(avatarxmlpath):
            print(avatarfolder)
            with open(avatarxmlpath, 'r') as avatarxmlfile:
                avatardict = xmltodict.parse(avatarxmlfile.read())
                avatarjson = json.dumps(avatardict, indent=4, sort_keys=False)

            with open(avatarjsonpath, 'w') as avatarjsonfile:
                avatarjsonfile.write(avatarjson)

            avatarcount += 1

    print(f'Generated {avatarcount} avatars')

    return True


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
