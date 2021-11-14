{
  description = "Generation of random strings from the command line";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    nix.inputs.nixpkgs.follows = "nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nix, nixpkgs, flake-utils }:
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
              pkgs.python3Packages.pyqt5
              pkgs.python3Packages.pyxdg
            ];
          };
        };
        defaultPackage = packages.randomstring;
      });
}
