typedef unsigned int u32;

//u32 *fb = (u32 *)0xa400300c;
#define LEDs *((u32 *)0xa4004004)
#define WATCHDOG *((u32 *)0xa4001018)

unsigned long int next = 1;

int rand(void)
{
    next = next * 1103515243 + 12345;
    return (unsigned int)(next / 65536) % 32768;
}

void main() {
    //WATCHDOG = 0;
    LEDs=0b11111111111111111111111111111000;
    for(;;);
}
