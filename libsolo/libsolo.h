#pragma once
#include <stdbool.h>

typedef unsigned int u32;
#define SOLO_BASE 0xa4000000

#define MEM(type, addr) *((volatile type *)addr) // volatile tells compiler that writing to address does something

//u32 *fb = (u32 *)0xa400300c;
#define LEDs MEM(u32, SOLO_BASE+0x4004)
#define WATCHDOG MEM(u32, SOLO_BASE+0x1018)

#define VSIZE MEM(u32, SOLO_BASE+0x9084)
#define HSIZE MEM(u32, SOLO_BASE+0x9090)

#define FBSTART MEM(u32, SOLO_BASE+0x300C)
#define FBSIZE MEM(u32, SOLO_BASE+0x3010)

void feed_watchdog(); // watchdog.c

void set_leds(bool power_led, bool connect_led, bool msg_led); // leds.c