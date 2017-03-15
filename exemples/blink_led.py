from __future__ import print_function

import sys
from time import sleep
from cloudpets import Cloudpets

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <addr>".format(sys.argv[0]))
        sys.exit(1)

    cloudpet = Cloudpets(sys.argv[1])
    cloudpet.connect()
    print("Connected")
    cloudpet.led.blink(100)
    sleep(2)
    cloudpet.led.turn_off()
