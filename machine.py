#!/usr/bin/env python3
import os
from enum import Enum
from typing import List

import platform
import typer

app = typer.Typer()


class PLATFORMS(Enum):
    NIXOS = "nixosConfigurations"
    DARWIN = "darwinConfigurations"
    HOME_MANAGER = "homeManagerConfigurations"


class COLORS(Enum):
    SUCCESS = typer.colors.GREEN
    INFO = typer.colors.CYAN
    ERROR = typer.colors.RED


if os.system("command -v nixos-rebuild > /dev/null") == 0:
    # if we're on nixos, this command is built in
    PLATFORM = PLATFORMS.NIXOS
elif (
    os.system("command -v darwin-rebuild > /dev/null") == 0 or
    platform.uname().system.lower() == "darwin".lower()
):
    # if we're on darwin, we might have darwin-rebuild or the distro id will be 'darwin'
    PLATFORM = PLATFORMS.DARWIN
else:
    # in all other cases of linux
    PLATFORM = PLATFORMS.HOME_MANAGER


def select(nixos: bool, darwin: bool, home_manager: bool):
    if sum([nixos, darwin, home_manager]) > 1:
        typer.secho(
            "Cannot apply more than one of [--nixos, --darwin, --home-manager]. Aborting...",
            fg=COLORS.ERROR.value,
        )
        return None

    if nixos:
        return PLATFORMS.NIXOS

    elif darwin:
        return PLATFORMS.DARWIN

    elif home_manager:
        return PLATFORMS.HOME_MANAGER

    else:
        return PLATFORM

def test_cmd(cmd: str):
    return os.system(f"{cmd} > /dev/null") == 0

def fmt_command(cmd: str):
    return f"> {cmd}"

def run_cmd(cmd: str):
    typer.secho(fmt_command(cmd), fg=COLORS.INFO.value)
    return os.system(cmd)


@app.command(help="set up disk for nix-darwin", hidden=PLATFORM != PLATFORMS.DARWIN)
def disk_setup():
    typer.secho("Setting up disks for nix-darwin", fg=COLORS.INFO.value)

    if PLATFORM != PLATFORMS.DARWIN:
        typer.secho(
            "nix-darwin does not apply on this platform. aborting...",
            fg=COLORS.ERROR.value,
        )
        raise typer.Exit(code=1)

    if not test_cmd("grep -q '^run\\b' /etc/synthetic.conf 2>/dev/null"):
        typer.secho("setting up /etc/synthetic.conf", fg=COLORS.INFO.value)
        run_cmd(
            'echo "run\\tprivate/var/run" | sudo tee -a /etc/synthetic.conf >/dev/null'
        )
        run_cmd(
            "/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs.util -B 2>/dev/null || true"
        )
        run_cmd(
            "/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs.util -t 2>/dev/null || true"
        )
    if not test_cmd("test -L /run"):
        typer.secho("linking /run directory", fg=COLORS.INFO.value)
        run_cmd("sudo ln -sfn private/var/run /run")
    typer.secho("Disk setup complete", fg=COLORS.SUCCESS.value)


@app.command(help="builds an initial configuration", hidden=PLATFORM == PLATFORMS.NIXOS)
def bootstrap(
    host: str =typer.Argument(..., help="the hostname of the configuration to build"),
    nixos: bool = False,
    darwin: bool = False,
    home_manager: bool = False,
    show_trace: bool = typer.Argument(False, help="showing traces from nix commands", envvar="MACHINE_SHOW_TRACE")
):
    typer.secho("Bootstrapping an initial configuration", fg=COLORS.INFO.value)
    cfg = select(nixos=nixos, darwin=darwin, home_manager=home_manager)
    flags = "-v --experimental-features 'flakes nix-command'"
    if cfg is None:
        raise typer.Exit(code=1)

    if cfg == PLATFORMS.DARWIN:
        disk_setup()
        flake = f".#{cfg.value}.{host}.config.system.build.toplevel {flags}"
        #run_cmd(f'nix build {flake} --show-trace')
        run_cmd(f'nix build {flake}')
        run_cmd("./result/activate-user && ./result/activate")
    else:
        typer.secho("Could not infer system type. Aborting.", fg=COLORS.ERROR.value)


if __name__ == "__main__":
    app()
