# AGENTS.md

Image transformations (resize + background removal) — distribution `entirius-py-image-transformations`, import `image_transformations`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the import package `image_transformations` — it is a public API contract.
- Default: do not commit — git is the user's call.

## Architecture

`image_transformations/`: `resize_methods` (ratio-safe and fill-crop resizes with white/black/pink/
transparent backgrounds), `background_removal_methods` (`remove_background_with_kernel`,
`remove_background_flood_fill`), `lib` (shared Pillow/OpenCV helpers).
Runtime deps: `pillow`, `opencv-contrib-python`, `matplotlib`.
Tests are smoke transformations over `tests/examples/` (matplotlib forced to Agg via `tests/conftest.py`).
