
.section .HEADER
.extern main
.extern approm_start
.extern CODE_END
.extern CODE_REAL_START
hdr:
    beq   $0,$0, main
    .long CODE_START; // code checksum, TODO: Calculate it when fixing header
    .long CODE_END; // rom length, TODO: Calculate it when fixing header
CODE_START:
    .long CODE_REAL_START;  // code length, TODO: Calculate it when fixing header
    .long 1; // rom build number. Free to edit, doesn't do anything lol
    .long 0; // heap data, aaddress what the fuck
    .long 0; // heap data size, what the fuck
    .long 0; // heap free size, what the fuck
    .long 0; // romfs base aaddress, TODO: Calculate it when fixing header
    .long 0; // unknown1, STORE ONLY NOTHING.
    .long 0; // unknown2, what the fuck
    .long approm_start; // rom base, DO NOT EDIT IT!!!
    .long 0; // build flags, DO NOT EDIT IT!!!
    .long 0; // heap data compressed size, what the fuck
    .long 0; // compressed code address, rom IS NOT compressed, store only nothing.
    .long 0; // compressed code size, store, you guested it, nothing.
    .word 0; // Important, needs to jump become 0x10000012
    .byte 0;

// CODE_START AND CODE_END are for fixing header
.globl hdr
