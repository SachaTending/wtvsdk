#include <libsolo.h>

void feed_watchdog() {
    WATCHDOG = 0x1;
}

void disable_watchdog() {
    BUS_CHPCNTL = 0xc000ffff;
    BUS_CHPCNTL = 0x8000ffff;
    BUS_CHPCNTL = 0x4000ffff;
    BUS_CHPCNTL = 0x0000ffff;
}