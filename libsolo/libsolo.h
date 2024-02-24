#pragma once
typedef unsigned int u32;
#define SOLO_BASE 0xa4000000

//u32 *fb = (u32 *)0xa400300c;
#define LEDs *((u32 *)SOLO_BASE+0x4004)
#define WATCHDOG *((u32 *)SOLO_BASE+0x1018)

#define VSIZE *((u32 *)SOLO_BASE+0x9084)
#define HSIZE *((u32 *)SOLO_BASE+0x9090)

#define FBSTART *((u32 *)SOLO_BASE+0x300C)
#define FBSIZE *((u32 *)SOLO_BASE+0x3010)

void feed_watchdog(); // watchdog.c