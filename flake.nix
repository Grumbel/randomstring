{
  description = "Generation of random strings from the command line";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-21.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
       in rec {
        packages = flake-utils.lib.flattenTree rec {
          randomstring = pkgs.python3Packages.buildPythonPackage rec {
            name = "randomstring";
            src = self;
            propagatedBuildInputs = [
              pkgs.python3Packages.setuptools
            ];
          };
        };
        defaultPackage = packages.randomstring;
      });
}
