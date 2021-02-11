# machine
> 🖥 Purely functional declarations of all my machines

# Prerequisites
## Installing Nix package manager
Run the script to perform a multi-user install on Darwin on any Linux. 
```bash
./install-nix.sh
```
Reboot terminal when complete.

## Installing Nix Flakes
Nix doesn't ship with Flakes yet.

Run the script to install Flakes.
```bash
./install-nix-flakes.sh
```
Reboot terminal when complete.

# Bootstrapping System
## Darwin
Clone repo with
```bash
git clone https://github.com/rameezk/machine ~/.nixpkgs
```

You can bootstrap a new nix-darwin system using
```bash
nix develop -c ./machine.py bootstrap && ./machine.py build --darwin [host]
```
