{
  description = "Generation of random strings from the command line";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
       in rec {
        packages = rec {
          randomstring = pkgs.python3Packages.buildPythonPackage rec {
            name = "randomstring";
            src = self;
            propagatedBuildInputs = [
              pkgs.python3Packages.setuptools
            ];
          };
          default = randomstring;
        };

        apps = rec {
          randomstring = flake-utils.lib.mkApp {
            drv = packages.randomstring;
          };
          default = randomstring;
        };
       }
    );
}
