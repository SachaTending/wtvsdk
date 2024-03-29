#include <libsolo.h>
#include <stdint.h>

#define delay for (int _=0;_<5000;_++)

void main() {
    uint8_t *addr = (uint8_t *)0xbfc00000;
    uint8_t bit = 0;
    uint8_t val = 0;

    for (int i=0;i<10000;i++) {
        val = addr[i];
        for (int a=0;a<7;a++) {
            bit = val & (1 << a);
            if (bit) {
                set_leds(true, true, false);
            } else {
                set_leds(true, false, false);
            }
            delay;
            set_leds(false, false, false);
        }
        set_leds(false, false, true);
        delay;
        set_leds(false, false, false);
        feed_watchdog();
    }
    for(;;) feed_watchdog();
}
