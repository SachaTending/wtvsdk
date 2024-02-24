#include <libsolo.h>

void feed_watchdog() {
    WATCHDOG = 0x1;
}