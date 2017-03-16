from __future__ import print_function

import sys
from cloudpets import Cloudpets

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <addr> <slot>".format(sys.argv[0]))
        sys.exit(1)

    cloudpet = Cloudpets(sys.argv[1])
    cloudpet.connect()
    print("Connected")
    cloudpet.volume = 255
    cloudpet.speaker.play(int(sys.argv[2]))
