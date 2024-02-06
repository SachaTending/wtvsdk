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

for i in AppRomHeader._fields_:
    i = i[0]
    print(f"{i}: {getattr(approm, i)}, {hex(getattr(approm, i))}")
    if i == "build_flags":
        build_flags = getattr(approm, i)

build_flags: int

def flag_check(flag) -> bool:
    return (build_flags & flag) == flag

print("build flags:")
if (flag_check(0x01)): print("can handle compressed data")
if (flag_check(0x04)): print("debug build")
if (flag_check(0x10)): print("windows ce build")
if (flag_check(0x20)): print("satelite build")