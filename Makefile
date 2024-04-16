OBJ = header.o test.o

TOOLCHAIN=mips

build: link
CFLAGS = -march=r5k -I libsolo

include libsolo/Makefile

%.o: %.S
	@echo "  [  AS] $@"
	@$(TOOLCHAIN)-gcc $(CFLAGS) $< -o $@ -c -O0

%.o: %.c
	@echo "  [  CC] $@"
	@$(TOOLCHAIN)-gcc $(CFLAGS) $< -o $@ -c


link: $(OBJ)
	@echo "  [  LD] approm.elf"
	@$(TOOLCHAIN)-ld -T link.ld $(OBJ) -o bin/approm.elf -no-pie
	@echo "  [ GEN] approm_not_fixed.o"
	@$(TOOLCHAIN)-objcopy -O binary bin/approm.elf bin/approm_not_fixed.o
	@echo "  [ FIX] approm.o"
	@python3 scripts/fix2.py bin/approm_not_fixed.o approm.o

clean: rm

rm:
	@-rm $(OBJ) approm.o bin/approm_not_fixed.o bin/approm.elf
