ENTRY(main)

SECTIONS
{
    . = 0x80800000;
    approm_start = .;
    .text : {
        *(.HEADER)
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
}