#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
import lxc
import sys

def main():
    """
    Comentario de la función
    """
    for container in lxc.list_containers(as_object=True):
	# Start the container (if not started)
    	#started = False
    	#if not container.running:
        #	if not container.start():
        #    		continue
        #	started = True
        print(container)

    print(dir(lxc))
    print(lxc.list_containers())

if __name__ == "__main__":
    main()

