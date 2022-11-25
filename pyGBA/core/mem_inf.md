# Memory!!! (only for development purposes)
## Memory regions are as follows:
### General Internal Memory
00000000-00003FFF   BIOS - System ROM         (16 KBytes)
00004000-01FFFFFF   Not used
02000000-0203FFFF   WRAM - On-board Work RAM  (256 KBytes) 2 Wait
02040000-02FFFFFF   Not used
03000000-03007FFF   WRAM - On-chip Work RAM   (32 KBytes)
03008000-03FFFFFF   Not used
04000000-040003FE   I/O Registers
### Internal Display Memory
05000000-050003FF   BG/OBJ Palette RAM        (1 Kbyte)
05000400-05FFFFFF   Not used
06000000-06017FFF   VRAM - Video RAM          (96 KBytes)
06018000-06FFFFFF   Not used
07000000-070003FF   OAM - OBJ Attributes      (1 Kbyte)
## Memory information copied from https://problemkaputt.de/gbatek.htm
#### Thank you