#include <libsolo.h>

void main() {
    //WATCHDOG = 0;
    // Fill fb with garbage
    for (int i=0;i<100;i++) {
        //((u32 *)SOLO_BASE+0x3010)[i] = FBSIZE;
    }
    LEDs=0b11111111111111111111111111111000;
    for(;;) feed_watchdog();
}
