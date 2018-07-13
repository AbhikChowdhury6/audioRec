def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

class Breath:
    def __init__(self, bus):
        self.addr = 0x51
        self.refRate = 256
        self.vlaues = [voltage]

    def read(bus):
        return read_word_2c(self.addr)
