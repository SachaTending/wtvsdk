from struct import pack

romfs = open("rfs.bin", "wb")

def add32(d: int):
    romfs.write(pack(">I", d))

#romfs.write(b'\x10\x00\x00\x12\x00\x00\x00\x00')
# write autodisk data
add32(0x39592841) # 0x0
add32(0) # 0x4
add32(0) # 0x8
add32(0) # 0xC
add32(0) # 0xC
add32(0) # 0x10
add32(0x14) # 0x14, len of metadata
chksum = 0x39592841 + 0x14
romfs.write(pack(">I", romfs.tell()+8))
romfs.write(pack(">I", chksum)) # checksum
#romfs.write(b"\x00"*(1024*4))
romfs.close()