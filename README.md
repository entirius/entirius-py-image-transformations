# entirius-py-image-transformations

Image resize and background-removal functions built on Pillow and OpenCV, part of
Entirius, the open-source modular ecommerce platform. Each function reads a source file and writes the transformed
image to a target path.

[![PyPI](https://img.shields.io/pypi/v/entirius-py-image-transformations.svg)](https://pypi.org/project/entirius-py-image-transformations/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-py-image-transformations.svg)](https://pypi.org/project/entirius-py-image-transformations/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-py-image-transformations/blob/develop/LICENSE)

## What it does

- Ratio-safe resizes with a white, black, pink or transparent background (`resize_ratio_safe_bg_*`).
- Fill-and-crop resizes with the same four backgrounds (`resize_fill_crop_bg_*`).
- Background removal with a kernel (`remove_background_with_kernel()`).
- Background removal by flood fill (`remove_background_flood_fill()`).

## Installation

```shell
uv add entirius-py-image-transformations
pip install entirius-py-image-transformations
```

The import name is `image_transformations`.

## Quick start

```python
from image_transformations import resize_ratio_safe_bg_white, remove_background_flood_fill

resize_ratio_safe_bg_white("in.jpg", "out.jpg", 500, 500)
remove_background_flood_fill("in.jpg", "out.png")
```

## Requirements

- Python 3.11 or newer.
- `pillow`, `opencv-contrib-python` and `matplotlib` (installed as dependencies).

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Changelog: https://github.com/entirius/entirius-py-image-transformations/blob/develop/CHANGELOG.md

## Part of Entirius

This library transforms the product and content images of the Entirius backend service (Volkanos) and its modules.

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Consumer modules: https://github.com/entirius/entirius-django-pim, https://github.com/entirius/entirius-django-contentdb

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest); smoke transformations over tests/examples/
```

Development and agent instructions: https://github.com/entirius/entirius-py-image-transformations/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-py-image-transformations/blob/develop/LICENSE.
