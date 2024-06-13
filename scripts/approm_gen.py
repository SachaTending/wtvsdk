from ctypes import BigEndianStructure, c_uint32, sizeof
import argparse
from struct import unpack
from os import SEEK_END

parser = argparse.ArgumentParser()
parser.add_argument("INPUT", help="Approm that needs to be fixed")
parser.add_argument("OUTPUT", help="Patched approm output")
parser.add_argument("-r", "--romfs", default="romfs.bin", help="ROMFS file to inject to approm")
args = parser.parse_args()

print(f"Approm generator, made by TendingStream73\nInput: {args.INPUT}\nOutput: {args.OUTPUT}")

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
        ('unknown1', c_uint32), # wtf
        ('unknown2', c_uint32), # wtf
        ('rom_base_address', c_uint32),
        ('build_flags', c_uint32),
        ('heap_data_compressed_size', c_uint32),
        ('compressed_code_addr', c_uint32),
        ('compressed_code_size', c_uint32)
    ]
    _pack_ = 0

inp = open(args.INPUT, 'rb') # open input

hdr_data = bytearray(inp.read(sizeof(AppRomHeader)))
inp.seek(0)

hdr = AppRomHeader.from_buffer(hdr_data)

l = hdr.rom_length - hdr.checksum
code_len = (l / 4) + 3

joeb = 0
while (code_len-int(code_len)) != 0.0:
    joeb += 1
    l += 1
    code_len = (l / 4) + 3

del l

inp.seek(0, SEEK_END)
size = inp.tell()
inp.seek(0)

hdr.code_length = int(code_len)

out = open(args.OUTPUT, "wb+") # open output
out.write(hdr_data)
inp.seek(0x44)

out.write(inp.read())

rfs = open(args.romfs, 'rb')
out.write(rfs.read())
rfs.close()
inp.close()

rl = out.tell()
hdr.rom_length = int((rl / 4) + 3)
out.seek(0)
out.write(hdr_data)

out.seek(0)
checksum = unpack(">I", out.read(4))[0]
out.seek(0xc)
l = (code_len - 3) * 4
l -= 0xc
for i in range(round(l / 4)):
    checksum += unpack(">I", out.read(4))[0]

hdr.checksum = checksum & 0xffffffff
out.seek(0)
out.write(hdr_data)