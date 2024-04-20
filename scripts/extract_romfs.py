from ctypes import BigEndianStructure, c_uint32, sizeof
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("INPUT")
parser.add_argument("-o", "--output", default="romfs.bin")

args = parser.parse_args()

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

inp = open(args.INPUT, "rb")

appr = AppRomHeader.from_buffer_copy(inp.read(sizeof(AppRomHeader)))

romfs_offset = appr.romfs_base_address - appr.rom_base_address

print(f"Extracting ROMFS from offset {romfs_offset}")
out = open(args.output, 'wb')
inp.seek(romfs_offset)
out.write(inp.read())