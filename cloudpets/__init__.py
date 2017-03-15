from __future__ import print_function

from bluetooth.ble import GATTRequester


STATE = {
    'IDLE': chr(0x1),
    'AUDIO_UPLOAD': chr(0x3),
    'PLAYBACK': chr(0x5),
    'AUDIO_DOWNLOAD': chr(0x7),
    'BUFFER_PRIME': chr(0x9)
}

HANDLES = {
    'cmd': 0x0012,
    'audio_send': 0x0015,
    'audio_recv': 0x0018,
    'state': 0x001c,
    'data_req': 0x0020,
    'config': 0x0024,
    'led': 0x0027,
    'volume': 0x002a
}


class Led(object):
    def __init__(self, cloudpet):
        self.cloudpet = cloudpet

    def blink(self, msec):
        cmd = [2, msec & 0xff, msec >> 8, 100, 0]
        self.cloudpet._send_command(HANDLES['led'], cmd)

    def turn_off(self):
        cmd = [0, 0, 0, 100, 0]
        self.cloudpet._send_command(HANDLES['led'], cmd)

    def turn_on(self):
        cmd = [1, 0, 0, 100, 0]
        self.cloudpet._send_command(HANDLES['led'], cmd)


class Speaker(object):
    def __init__(self, cloudpet):
        self.cloudpet = cloudpet

    def play(self, slot=2):
        self.cloudpet._send_command(HANDLES['cmd'], [8, 1, slot])

    def stop(self):
        self.play(0)

    @property
    def volume(self):
        response = self.cloudpet._read_value(HANDLES['volume'])[0]
        return ord(response[0])

    @volume.setter
    def volume(self, level):
        self.cloudpet._send_command(HANDLES['volume'], [0, level])


class Microphone(object):
    def __init__(self, cloudpet):
        self.cloudpet = cloudpet

    def record(self):
        self.cloudpet._send_command(HANDLES['cmd'], [8, 2])


class Cloudpets(object):
    def __init__(self, address):
        self._requester = GATTRequester(address, False)
        self.led = Led(self)
        self.speaker = Speaker(self)
        self.microphone = Microphone(self)
        self.state = None

    def connect(self):
        self._requester.connect(True)

    def disconnect(self):
        self._requester.disconnect()

    def _read_value(self, handle):
        return self._requester.read_by_handle(handle)

    def _send_command(self, handle, cmd):
        self._requester.write_by_handle(handle, str(bytearray(cmd)))
