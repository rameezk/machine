{ config, lib, pkgs, ... }: {
  programs.git = {
    userName = "Rameez Khan";
    extraConfig = {
      http.sslVerify = true;
      pull.rebase = false;
    };
  };
}
