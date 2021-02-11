# machine
> 🖥 Purely functional declarations of all my machines

# Prerequisites
## Get this repo
Yeah, thanks Captain Obvious.

```bash
git clone https://github.com/rameezk/machine ~/.nixpkgs
```

## Installing Nix package manager
Run the script to perform a multi-user install on Darwin on any Linux. 
```bash
./install-nix.sh
```
Reboot terminal when complete.

> **NOTE 1:** On MacOS, git will not be installed (but you will prompted to install developer tools).

> **NOTE 2:** On MacOS, the above script may not succeed at first, you will need to reboot and run the script again in order for it to succeed.

## Installing Nix Flakes
Nix doesn't ship with Flakes yet.

Run the script to install Flakes.
```bash
./install-nix-flakes.sh
```
Reboot terminal when complete.


# Bootstrapping System
## Darwin
You can bootstrap a new nix-darwin system using
```bash
nix develop -c ./machine.py bootstrap --darwin [host]
```

> **NOTE 1:** On MacOS, the host should first be set via `Preferences > Sharing`. You might have to reboot.


