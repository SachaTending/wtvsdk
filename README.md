# WTV Homebrew sdk
This sdk was made by TendingStream73(github: sachatending), with help from webtv wiki

# How i can create homebrew application, and compile it?
1. Get gcc cross compiler for mips, precompiled version ![is here](https://tendhost.ddns.net/stuff/webtv_toolchain.tar.gz), or compile yourself(Note: when you configuring gcc and binutils, use target mips64)
2. (If precompiled)Add to path bin folder(this is where gcc and other stuff located)
3. For fix_hdr.py, you need python version 3.9=< and numpy(because it has normal realization of uint32(important for code checksum generation)

Now you can compile this, as a result, you get approm.o. This is your homebrew app

# I want to interact with solo asic, where i can get documentation

Documentation of solo1(solo3 and solo2 are backwards compatible) asic can be found on ![webtv wiki](http://wiki.webtv.zone/misc/SOLO1/SOLO1_ASIC_Spec.pdf), or ![on my server](https://tendhost.ddns.net/data/SOLO1_ASIC_Spec.pdf)

# How i can run approm.o on my webtv?
There are 2 ways to sideload approm.o and run it

1. You need to setup ![minsrv](https://github.com/zefie/zefie_wtvp_minisrv), and via disk download save it to webtv's internal hdd, then, via client:boota, you can boot it
2. Connect webtv's hdd to your pc(DO NOT FORMAT IT OR YOUR WEBTV WILL STUCK IN MINIBROWSER), use ![this util](https://github.com/wtv-411/emac-webtv-partition-editor) to save approm.o at browser approm segment(BACKUP THIS SEGMENT BEFORE OVERWRITING IT WITH YOUR approm.o)/

# Why approm_not_fixed.o is small, but approm.o is big
This is because romfs
# What is romfs
romfs is filesystem used by webtv to store files in firmware(static files), you can interact with fs if you write fs driver to work with it

# Can i support this project?

No, bcz i live in Russia lol.

# I want to add some code to interact with solo asic to this repo
Just send pull requests(store this src in folder libsolo)

# Special thanks to:
WebTV wiki and webtv redialed members for helping with this sdk.
