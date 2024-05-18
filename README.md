# CTF 

1. Setup [pwntools](https://github.com/Gallopsled/pwntools#readme)
```
make
source pwn/bin/activate
```
2. Setup [gef](https://hugsy.github.io/gef/)
```
cp gef.py ~/.gef.py
echo "source ~/.gef.py" >> ~/.gdbinit
```
3. (Optional) Update gef
```
python ~/.gef.py --update
```
4. (Optional Kali) Install Ghidra
```
sudo apt install ghidra
```

## Apple Silicon / aarch64 Setup
[Download the qemu-user-static](https://www.kali.org/docs/arm/x86-on-arm/) unless you can directly apt install:
```
wget https://snapshot.debian.org/archive/debian/20240509T024809Z/pool/main/q/qemu/qemu-user-static_8.2.3%2Bds-2_arm64.deb
```

Install arch specific tools:
```
sudo dpkg --add-architecture amd64
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install ./qemu-user-static_8.2.3+ds-2_arm64.deb
sudo apt install -y qemu-user-static binfmt-support
sudo apt install libc6:i386
sudo apt install gdb-multiarch
sudo apt install binutils:amd64
sudo apt install binutils:i386
```
