#include "libsolo.h"

void uart_out(char c) {
    while (SUCGPU_TFFMAX <= SUCGPU_TFFCNT);
    SUCGPU_TFFHR = (int)c;
}

void uart_init(void)
{
    SUCGPU_MCD0 = 0;
    SUCGPU_SCD1 = 1;
    SUCGPU_SCD0 = 0xd;
    SUCGPU_CCR = 3;
    SUCGPU_IOOD = 0x3f;
    SUCGPU_SPIOCR = 0;
    SUCGPU_SPIOCR = 2;
    SUCGPU_SPIOEN = 2;
    SUCGPU_LCR = 0x3a;
    SUCGPU_LSCR = 0;
    SUCGPU_LSTPBITS = 2;
    SUCGPU_TSRCR = 1;
    SUCGPU_RSRCR = 1;
    SUCGPU_TFFCR = 2;
    SUCGPU_RFFCR = 2;
}
