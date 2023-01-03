# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [6.1.4](https://github.com/taoqf/node-fast-html-parser/compare/v6.1.3...v6.1.4) (2022-11-15)


### Bug Fixes

* [#224](https://github.com/taoqf/node-fast-html-parser/issues/224) ([0719bf0](https://github.com/taoqf/node-fast-html-parser/commit/0719bf031c3fec51611f9dff922f46bfe4acb060))

### [6.1.3](https://github.com/taoqf/node-fast-html-parser/compare/v6.1.2...v6.1.3) (2022-11-14)

### [6.1.2](https://github.com/taoqf/node-fast-html-parser/compare/v6.1.1...v6.1.2) (2022-11-14)


### Bug Fixes

* [#224](https://github.com/taoqf/node-fast-html-parser/issues/224) ([fc367fa](https://github.com/taoqf/node-fast-html-parser/commit/fc367fa294d72794a0dea49edbd986d527a6314b))

### [6.1.1](https://github.com/taoqf/node-fast-html-parser/compare/v6.1.0...v6.1.1) (2022-09-24)


### Bug Fixes

* parse comments ([82b68ff](https://github.com/taoqf/node-fast-html-parser/commit/82b68ff9eb944e0c55ca2e0ea13fb714e2004803))

## [6.1.0](https://github.com/taoqf/node-fast-html-parser/compare/v6.0.0...v6.1.0) (2022-09-19)


### Features

* Add docs ([8a38eed](https://github.com/taoqf/node-fast-html-parser/commit/8a38eedab6b20906ee89dea86c4271960afbad2d))

## [6.0.0](https://github.com/taoqf/node-fast-html-parser/compare/v5.4.2-0...v6.0.0) (2022-09-08)


### Bug Fixes

* Preserve invalid nested A tags in AST (see [#215](https://github.com/taoqf/node-fast-html-parser/issues/215) for detail) ([374188f](https://github.com/taoqf/node-fast-html-parser/commit/374188f1c6d6c6d0567348b8e8d20957f5a93fb8))

### [5.4.2](https://github.com/taoqf/node-fast-html-parser/compare/v5.4.2-0...v5.4.2) (2022-08-30)

## [5.1.0](https://github.com/taoqf/node-fast-html-parser/compare/v4.1.5...v5.1.0) (2021-10-28)

### Features

* Exposed `HTMLElement#rawAttrs` (made public) ([34f1595](https://github.com/taoqf/node-fast-html-parser/commit/34f1595756c0974b6ae7ef5755a615f09e421f32))

## [5.0.0](https://github.com/taoqf/node-fast-html-parser/compare/v4.1.5...v5.0.0) (2021-10-10)


### ⚠ BREAKING CHANGES

* Added esm named export support ([0d4b922](https://github.com/taoqf/node-fast-html-parser/commit/0d4b922eefd6210fe802991e464b21b0c69d5f63))

### Features

* Added esm named export support (closes [#160](https://github.com/taoqf/node-fast-html-parser/issues/160) closes [#139](https://github.com/taoqf/node-fast-html-parser/issues/139)) ([0d4b922](https://github.com/taoqf/node-fast-html-parser/commit/0d4b922eefd6210fe802991e464b21b0c69d5f63))
* Added HTMLElement#getElementsByTagName ([d462e44](https://github.com/taoqf/node-fast-html-parser/commit/d462e449e7ebb00a5a43fb574133681ad5a62475))
* Improved parsing performance + matching (closes [#164](https://github.com/taoqf/node-fast-html-parser/issues/164)) ([3c5b8e2](https://github.com/taoqf/node-fast-html-parser/commit/3c5b8e2a9104b01a8ca899a7970507463e42adaf))


### Bug Fixes

* Add null to return type for HTMLElement#querySelector (closes [#157](https://github.com/taoqf/node-fast-html-parser/issues/157)) ([2b65583](https://github.com/taoqf/node-fast-html-parser/commit/2b655839bd3868c41fb19cae5786ca097565bc7f))
* blockTextElements incorrectly matching partial tag (detail) (fixes [#156](https://github.com/taoqf/node-fast-html-parser/issues/156) fixes [#124](https://github.com/taoqf/node-fast-html-parser/issues/124)) ([6823349](https://github.com/taoqf/node-fast-html-parser/commit/6823349fdf1809c7484c70d948aa24930ef4983f))
