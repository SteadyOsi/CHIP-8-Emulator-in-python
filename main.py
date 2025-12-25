import chip8_cpu as chip

cpu = chip.Chip8_CPU()
cpu.reset()
cpu.load_rom("/home/minion/Documents/GitHub/CHIP8-Roms/chip8-roms/programs/IBM Logo.ch8")

opcode = cpu.fetch()
print(hex(opcode))
cpu.decode(opcode)