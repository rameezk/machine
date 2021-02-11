{
  description = "Nix system configurations";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    stable.url = "github:nixos/nixpkgs/nixos-20.09";

    flake-utils.url = "github:numtide/flake-utils/master";
    flake-compat = {
      url = "github:edolstra/flake-compat";
      flake = false;
    };

    mach-nix = {
      url = "github:DavHau/mach-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    home-manager = {
      url = "github:nix-community/home-manager/master";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    darwin = {
      url = "github:kclejeune/nix-darwin/brew-bundle";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{ self, nixpkgs, home-manager, darwin, mach-nix, flake-utils, ... }:
    let
      mkDarwinConfig = { hostname, baseModules ? [
        home-manager.darwinModules.home-manager
        ./machines/darwin
      ], extraModules ? [ ] }: {
        "${hostname}" = darwin.lib.darwinSystem {
          # system = "x86_64-darwin";
          modules = baseModules ++ extraModules;
          specialArgs = { inherit inputs nixpkgs; };
        };
      };
    in {
      darwinConfigurations = mkDarwinConfig {
        hostname = "rameezk-macbook";
      };
    } //
    # dev shell
    flake-utils.lib.eachDefaultSystem (system:
    let pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShell = let
        pyEnv = (mach-nix.lib.${system}.mkPython {
          requirements = ''
            black
            pylint
            typer-cli
            typer
            colorama
            shellingham
            distro
          '';
        });
      in pkgs.mkShell {
        buildInputs = with pkgs; [ nixFlakes rnix-lsp pyEnv ];
      };
    });
}
