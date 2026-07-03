# image-transformations

Image resize and background-removal transformations built on Pillow and OpenCV —
ratio-safe and fill-crop resizes with white/black/pink/transparent backgrounds,
plus kernel- and flood-fill-based background removal.

## Installation

```shell
pip install entirius-py-image-transformations
```

## Usage

```python
from image_transformations import resize_ratio_safe_bg_white, remove_background_flood_fill

resize_ratio_safe_bg_white("in.jpg", "out.jpg", 500, 500)
remove_background_flood_fill("in.jpg", "out.png")
```

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest) — smoke transformations over tests/examples/
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
