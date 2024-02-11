from ctypes import BigEndianStructure, c_uint32, sizeof
from struct import unpack, pack, pack_into
import numpy as np
from io import BytesIO

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
    romfs_base_address: int
    rom_base_address: int
    _pack_ = 0

def replace_bytes(buf, ofs, fmt, *args):
    ba = bytearray(buf)
    pack_into(fmt, ba, ofs, *args)
    return bytes(ba)

STEPS = 3

PACK_INT = ">I"

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
print("joeb padings needs to be added:", joeb)

file.seek(0)
out = bytearray(file.read())
out += b"joeb" * joeb
print("added joeb padding.")
print("injecting code length...")
out[0x10:0x14] = pack(PACK_INT, int(al))
print("2/{}: Fixing code cheksum...".format(STEPS))

code = out[0xc:] # get data from offset 0xc
c = np.uint32(approm.jump)
clen = len(code)
if clen > 0x2000000: 
    print("rom size is over 0x2000000")
    clen = 0x2000000
for i in range(0xc ,clen, 4):
    c += np.uint32(unpack(PACK_INT, out[i:i+4])[0])

print("code cheksum:", c)
print("Injecting code checksum...")
out[0x8:0xc] = pack(PACK_INT, c)

s = 1024*1024*4
s -= len(out)

def inject_romfs():
    global out
    global s
    print("3/{}: Injecting ROMFS...".format(STEPS))
    rfs = open("rfs.bin", "rb").read()
    s -= len(rfs)
    out += b"\x00"*s
    romfs_off = len(out)
    out += rfs
    print("Injecting ROMFS base address...")
    out[0x24:0x28] = pack(PACK_INT, approm.rom_base_address+romfs_off)

inject_romfs()

print("Injecting rom size...")
rl = ((len(out[0xc:])) / 4) + 3
out[0xc:0x10] = pack(PACK_INT, int(rl))
print("Recalculating code checksum...")
c = np.uint32(approm.jump)

a = BytesIO(out)
a.seek(0xc)
for i in range(0, clen-24, 4):
    d = a.read(4)
    #print(i, hex(i), c, hex(c), hex(unpack(PACK_INT, d)[0]))
    c += np.uint32(unpack(PACK_INT, d)[0])
out[0x8:0xc] = pack(PACK_INT, c)
print("all done(i think), saving to file...")
open("approm.o", "wb").write(out)