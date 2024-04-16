#include <libsolo.h>
#include <stdint.h>

#define delay for (int _=0;_<10000;_++)

void puts(const char *s) {
    do {
        uart_out(*s);
    } while (*s++);
}

void disable_watchdog2(void) {
    u32 sequence[] = {0b11, 0b10, 0b01, 0b00};
    for (int i = 0; i < 4; ++i) {
        BUS_CHPCNTL = (BUS_CHPCNTL & ~(0b1111 << 28)) | (sequence[i] << 28);
    }
}

// leds test

__attribute__ ((section(".HEADER"))) void main() {
    uart_init();
    puts("uart test 123, if you see this, uart works\n\r");
    disable_watchdog2();puts("watchdog disabled.\r\n"); 
    while (1) {
        set_leds(true, false, false);
        delay;
        set_leds(false, true, false);
        delay;
        set_leds(false, false, true);
        puts("leds sequence: repeat\n\r");
    }
    for(;;);
}
