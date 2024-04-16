ENTRY(main)

SECTIONS
{
    . = 0x80440000;
    approm_start = .;
    .text : {
        *(.HEADER)
        CODE_REAL_START = .;
        *(.text)
    }
    CODE_END = .;
    .rodata : {
        *(.rodata)
    }
    .data : {
        *(.data)
    }
    .bss : {
        *(.bss)
    }
    /DISCARD/ : {
        *(.eh_frame)
        *(.note .note.*)
    }
}
