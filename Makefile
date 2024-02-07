OBJ = header.o test.o

build: link

%.o: %.S
	@echo "  [  AS] $@"
	@mips64-gcc -march=r5k $< -o $@ -c -O0

%.o: %.c
	@echo "  [  CC] $@"
	@mips64-gcc -march=r5k $< -o $@ -c


link: $(OBJ)
	@echo "  [  LD] approm.elf"
	@mips64-ld -T link.ld header.o test.o -o approm.elf -no-pie
	@echo "  [ GEN] approm_not_fixed.o"
	@mips64-objcopy -O binary approm.elf approm_not_fixed.o
	@echo "  [ FIX] approm.o"
	@python3 fix_hdr.py

rm:
	@rm $(OBJ)