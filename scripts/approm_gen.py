from ctypes import BigEndianStructure, c_uint32, sizeof
import argparse

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