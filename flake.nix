{
  description = "Nix system configurations";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    stable.url = "github:nixos/nixpkgs/nixos-20.09";

    mach-nix = {
      url = "github:DavHau/mach-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    inputs@{ self, nixpkgs, mach-nix, flake-utils, ... }:
    let
      name = "Rameez Khan";
    in
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
