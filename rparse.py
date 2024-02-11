from ctypes import BigEndianStructure, c_uint32, sizeof


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

file = open("approm.o", "rb")

data = file.read(sizeof(AppRomHeader))
approm = AppRomHeader.from_buffer(bytearray(data), 0)

rsize = (approm.rom_length - 3) * 4
clen = (approm.code_length - 3) * 4
print("rom size(from offset 0xC):", rsize)
print("code size(from offset 0xC):", clen)
print("ROMFS Size(rsize - clen - 0xC):",(rsize-clen)-0xC)

romfs_off = approm.romfs_base_address - approm.rom_base_address

print("ROMFS Loacted at", romfs_off)

file.seek(romfs_off)
romfs = file.read()

class ROMFS_footer(BigEndianStructure):
    romfs_size: int
    romfs_checksum: int
    _fields_ = [
        ('romfs_size', c_uint32),
        ('romfs_checksum', c_uint32)
    ]
    _pack_ = 0

a = len(romfs)-sizeof(ROMFS_footer)

rf = ROMFS_footer.from_buffer_copy(romfs[a:])

print("ROMFS Cheksum:", rf.romfs_checksum)
print("ROMFS Size:", rf.romfs_size)