;; RandomString - Random string generation
;; Copyright (C) 2019 Ingo Ruhnke <grumbel@gmail.com>
;;
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.

(use-modules (guix packages)
             (guix gexp)
             (guix git-download)
             (guix build-system python)
             (guix licenses)
             (gnu packages python)
             (guix-cocfree utils))

(define %source-dir (dirname (current-filename)))

(define-public randomstring
  (package
    (name "randomstring")
    (version (version-from-source %source-dir))
    (source
     (local-file %source-dir
                 #:recursive? #t
                 #:select? (source-select-function %source-dir)))
    (build-system python-build-system)
    (home-page "https://gitlab.com/grumbel/randomstring")
    (synopsis "Generate random strings based on a character set")
    (description "The `randomstring` tool allows the generation of
random strings.  The length and character set can be choosen on command
line.")
    (license gpl3+)))

randomstring

;; EOF ;;
