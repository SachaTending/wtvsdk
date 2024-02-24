from ctypes import BigEndianStructure, c_uint32, sizeof
from struct import pack, unpack
from numpy import uint32 as n
from sys import argv

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
    _pack_ = 0
print(f"approm header size: {sizeof(AppRomHeader)}")

file = open("approm_orig.o", "rb")

data = file.read(sizeof(AppRomHeader))

approm = AppRomHeader.from_buffer(bytearray(data), 0)

file2 = open(argv[1], "rb")

data = file.read(sizeof(AppRomHeader))
approm2 = AppRomHeader.from_buffer(bytearray(data), 0)

base = approm.rom_base_address
rbase = approm.romfs_base_address

if base != approm2.rom_base_address:
    print("WARNING: Original approm's base address is not equal to target rom base, fixing...")
    a = rbase - base
    base = approm2.rom_base_address
    rbase = base+a

file2.seek(0x44)
code = file2.read()

off = approm.jump
#if approm2.jump != off:
#    print("WARNING: Original approm's jump offset not equal to target jump offset, fixing...")
#    off = approm2.jump

whatever = off

off = ((off & 0xFFFF) << 2) + 4

out = open(argv[2], "w+b")

file.seek(0)
out.write(file.read())
file.seek(0)
out.seek(0)

out.seek(off)
b = out.write(code)

print("Wrote code at", hex(off))
print("Bytes written:", hex(b), b)

print("Fixing header...")

def p(a: int):
    return pack(">I",a)

out.seek(0)
out.write(p(whatever))
print("Fixing checksum...")

chksm = n(whatever)
l = (approm.code_length - 3) * 4

out.seek(0xC)
b = out.read(l)

for i in range(0, l, 4):
    chksm += n(unpack(">I", b[i:i+4])[0])

print("checksum:", chksm)
out.seek(0x8)
out.write(pack(">I", chksm))
print("all done.")