# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

Initial Release

[Unreleased]: https://github.com/RLNT/bl2_eridium/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/RLNT/bl2_eridium/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/RLNT/bl2_eridium/releases/tag/v0.1.0