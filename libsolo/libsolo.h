#pragma once
#include <stdbool.h>

typedef unsigned int u32;
#define SOLO_BASE 0xa4000000

#define MEM(type, addr) *((volatile type *)addr) // volatile tells compiler that writing to address does something

//u32 *fb = (u32 *)0xa400300c;
#define BUS_CHPCNTL MEM(u32, SOLO_BASE+0x4)

#define LEDs MEM(u32, SOLO_BASE+0x4004)
#define WATCHDOG MEM(u32, SOLO_BASE+0x1018)

#define VSIZE MEM(u32, SOLO_BASE+0x9084)
#define HSIZE MEM(u32, SOLO_BASE+0x9090)

#define FBSTART MEM(u32, SOLO_BASE+0x300C)
#define FBSIZE MEM(u32, SOLO_BASE+0x3010)

#define SUCGPU_TFFHR MEM(u32, SOLO_BASE+0xA000)
#define SUCGPU_TFFCR MEM(u32, SOLO_BASE+0xA014)
#define SUCGPU_RFFCR MEM(u32, SOLO_BASE+0xA054)
#define SUCGPU_TFFCNT MEM(u32, SOLO_BASE+0xA00C)
#define SUCGPU_TFFMAX MEM(u32, SOLO_BASE+0xA010)
#define SUCGPU_TSRCR MEM(u32, SOLO_BASE+0xA080)
#define SUCGPU_RSRCR MEM(u32, SOLO_BASE+0xA0C0)
#define SUCGPU_MCD0 MEM(u32, SOLO_BASE+0xA100)
#define SUCGPU_SCD0 MEM(u32, SOLO_BASE+0xA104)
#define SUCGPU_SCD1 MEM(u32, SOLO_BASE+0xA108)
#define SUCGPU_CCR MEM(u32, SOLO_BASE+0xA10C)
#define SUCGPU_LCR MEM(u32, SOLO_BASE+0xA180)
#define SUCGPU_LSCR MEM(u32, SOLO_BASE+0xA184)
#define SUCGPU_LSTPBITS MEM(u32, SOLO_BASE+0xA188)
#define SUCGPU_IOOD MEM(u32, SOLO_BASE+0xA288)
#define SUCGPU_SPIOCR MEM(u32, SOLO_BASE+0xA28C)
#define SUCGPU_SPIOEN MEM(u32, SOLO_BASE+0xA298)

void feed_watchdog(); // watchdog.c
void disable_watchdog();

void uart_init(void); // uart.c
void uart_out(char c);

void set_leds(bool power_led, bool connect_led, bool msg_led); // leds.c