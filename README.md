# machine
> 🖥 Purely functional declarations of all my machines

## Prerequisites
### Get this repo
Yeah, thanks Captain Obvious.

```console
git clone https://github.com/rameezk/machine ~/.nixpkgs
```

### Installing Nix package manager
Run the script to perform a multi-user install on Darwin on any Linux. 
```console
./install-nix.sh
```
Reboot terminal when complete.

> **NOTE 1:** On MacOS, git will not be installed (but you will prompted to install developer tools).

> **NOTE 2:** On MacOS, the above script may not succeed at first, you will need to reboot and run the script again in order for it to succeed.

### Installing Nix Flakes
Nix doesn't ship with Flakes yet.

Run the script to install Flakes.
```console
./install-nix-flakes.sh
```
Reboot terminal when complete.


## Bootstrapping System
### Darwin
You can bootstrap a new nix-darwin system using
```console
nix develop -c ./machine.py bootstrap --darwin [host]
```

> **NOTE 1:** On MacOS, the host should first be set via `Preferences > Sharing`. You might have to reboot.


## References
1. Based heavily off the work done in [this fantastic project](https://github.com/kclejeune/system).

## License

MIT License

Copyright (c) 2021 Rameez Khan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
