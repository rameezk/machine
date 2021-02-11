#! /usr/bin/env bash

nix-env -iA nixpkgs.nixFlakes

if ! command -v nixos-rebuild > /dev/null; then
    echo "Non Nixos environment. Enabling nix flakes via ~/.config/nix/nix.conf"
    if [[ ! -f ~/.config/nix/nix.conf ]]; then
        mkdir -p ~/.config/nix
        echo "experimental-features = nix-command flakes" > ~/.config/nix/nix.conf
    fi
fi

echo "Reboot terminal"
