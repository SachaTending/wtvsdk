OBJ = header.o test.o

build: link
ARCH = r5k -mabi=32 -I libsolo

include libsolo/Makefile

%.o: %.S
	@echo "  [  AS] $@"
	@mips64-gcc -march=$(ARCH) $< -o $@ -c -O0

%.o: %.c
	@echo "  [  CC] $@"
	@mips64-gcc -march=$(ARCH) $< -o $@ -c


link: $(OBJ)
	@echo "  [  LD] approm.elf"
	@mips64-ld -T link.ld $(OBJ) -o bin/approm.elf -no-pie
	@echo "  [ GEN] approm_not_fixed.o"
	@mips64-objcopy -O binary bin/approm.elf bin/approm_not_fixed.o
	@echo "  [ FIX] approm.o"
	@python3 scripts/fix2.py bin/approm_not_fixed.o approm.o

clean: rm

rm:
	@-rm $(OBJ) approm.o bin/approm_not_fixed.o bin/approm.elf
