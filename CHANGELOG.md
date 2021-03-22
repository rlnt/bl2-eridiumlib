# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keep a changelog] and this project adheres to [Semantic Versioning][semantic versioning].

## [Unreleased]

- /

---

## [Released]

## [0.3.2] - 2021-03-22

### Added
- modinfo for mod database

### Fixed
- semver checks


## [0.3.1] - 2021-03-22

### Added
- Log python version

### Fixed
- Installed ujson for Win32 Python 3.7


## [0.3.0] - 2021-03-22

### Added
- Export `socket`, `ssl`, `requests`, `semver` and `ujson`

### Changed
- Rename to `EridiumLib`
- `log` now takes multiple argument to be closer to `unrealsdk.Log`


## [0.2.0] - 2021-03-20

### Added
- `dist` with `_socket`, `_ssl` and other files needed to make `requests` work
- `getLatestVersion` and `isLatestRelease` functions
- Automatic releases and linting with Github Actions
- Licenses for *OpenSSL* and *Python 3.7*

### Changed
- Moved `isClient` to `Eridium`
- Mod name to `EridiumLib`

### Removed
- Wrapped classes, they do not align with the goal of this library


## [0.1.0] - 2021-03-19
- Initial Release


<!-- Links -->
[keep a changelog]: https://keepachangelog.com/
[semantic versioning]: https://semver.org/

<!-- Versions -->
[unreleased]: https://github.com/RLNT/bl2_eridium/compare/v1.0.0...HEAD
[released]: https://github.com/RLNT/bl2_eridium/releases
[0.3.2]: https://github.com/RLNT/bl2_eridium/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/RLNT/bl2_eridium/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/RLNT/bl2_eridium/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/RLNT/bl2_eridium/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/RLNT/bl2_eridium/releases/tag/v0.1.0
