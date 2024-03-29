#include <libsolo.h>
#include <stdbool.h>
#include <stdint.h>

uint8_t bool_flip(bool val) {
    if (val) {
        return 0;
    }
    return 1;
}

uint8_t a(bool v, uint8_t g) {
    if (v) {
        return g;
    }
    return 0;
}

uint32_t bit_clear(uint32_t number, uint32_t n) {
    return number & ~((uint32_t)1 << n);
}

void set_leds(bool power_led, bool connect_led, bool msg_led) {
    uint32_t out = 0xffffffff;
    out = bit_clear(out, a(power_led, 2));
    out = bit_clear(out, a(connect_led, 1));
    out = bit_clear(out, a(msg_led, 0));
    LEDs=out;
}