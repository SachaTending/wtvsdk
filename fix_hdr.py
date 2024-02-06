from ctypes import BigEndianStructure, c_uint32, sizeof
from struct import unpack, pack, pack_into
import numpy as np

class AppRomHeader(BigEndianStructure):
    _fields_ = [
        ('jump', c_uint32),
        ('prejump', c_uint32),
        ('checksum', c_uint32),
        ('rom_length', c_uint32),
        ('code_length', c_uint32),
        ('rom_build_number', c_uint32),
        ('heap_data_address', c_uint32),
        ('heap_data_size', c_uint32),
        ('heap_free_size', c_uint32), # ???
        ('romfs_base_address', c_uint32),
        ('unknown1', c_uint32),
        ('unknown2', c_uint32),
        ('rom_base_address', c_uint32),
        ('build_flags', c_uint32),
        ('heap_data_compressed_size', c_uint32),
        ('compressed_code_addr', c_uint32),
        ('compressed_code_size', c_uint32)
    ]
    jump: int
    checksum: int
    rom_length: int
    rom_base_address: int
    _pack_ = 0

def replace_bytes(buf, ofs, fmt, *args):
    ba = bytearray(buf)
    pack_into(fmt, ba, ofs, *args)
    return bytes(ba)

STEPS = 3

file = open("approm_not_fixed.o", "rb")

data = file.read(sizeof(AppRomHeader))
approm = AppRomHeader.from_buffer(bytearray(data), 0)

print("Fixing approm...")
print("1/{}: Fixing code length...".format(STEPS))

l = approm.rom_length - approm.checksum

al = (l / 4) + 3

joeb = 0
while (al-int(al)) != 0.0:
    joeb += 1
    l += 4
    al = (l / 4) + 3
print((al-int(al)))
print("joeb padings needs to be added:", joeb)

file.seek(0)
out = bytearray(file.read())
out += b"joeb" * joeb
print("added joeb padding.")
print("injecting code length...")
out[0x10:0x14] = pack(">I", int(al))
print("2/{}: Fixing code cheksum...".format(STEPS))

code = out[0xc:len(out)] # get data from offset 0xc
c = np.uint32(approm.jump)

for i in range(0 ,len(code), 4):
    c += np.uint32(unpack(">I", code[i:i+4])[0])

print("code cheksum:", c)
print("Injecting code checksum...")
out[0x8:0xc] = pack(">I", c)

print("3/{}: Injecting ROMFS...".format(STEPS))
rfs = open("romfs.bin", "rb").read()
romfs_off = len(out)
out += rfs
print("Injecting romfs size...")
rl = ((len(rfs)+l) / 4) + 3
out[0xc:0x10] = pack(">I", int(rl))
print("Injecting ROMFS base address...")
out[0x24:0x28] = pack(">I", romfs_off)
print("all done(i think), saving to file...")
open("approm.o", "wb").write(out)