# machine
> 🖥 Purely functional declarations of all my machines

# Prerequisites
## Installing Nix package manager
Run the script to perform a multi-user install on Darwin on any Linux. 
```bash
./install-nix.sh
```

# Bootstrapping System
## Darwin
Clone repo with
```bash
git clone https://github.com/rameezk/machine ~/.nixpkgs
```

You can bootstrap a new nix-darwin system using
```bash
nix develop -c ./do.py disksetup && ./do.py build --darwin [host] && ./result/activate-user && ./result/activate
```
