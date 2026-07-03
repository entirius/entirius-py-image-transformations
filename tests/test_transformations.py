# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import glob
import os
import shutil
import unittest
from pathlib import Path

from image_transformations import (
    remove_background_flood_fill,
    remove_background_with_kernel,
    resize_fill_crop_bg_black,
    resize_fill_crop_bg_pink,
    resize_fill_crop_bg_transparent,
    resize_fill_crop_bg_white,
    resize_ratio_safe_bg_black,
    resize_ratio_safe_bg_pink,
    resize_ratio_safe_bg_transparent,
    resize_ratio_safe_bg_white,
)

TEST_SIZES = [
    # (width, height)
    (250, 250),
    # (1200, 1200),
    (500, 500),
    (600, 200),
    (200, 600),
    (426, 658),
]

TEST_DIR = Path(__file__).resolve().parent
OUT_DIR = os.path.join(TEST_DIR, "out")
EXAMPLES_DIR = os.path.join(TEST_DIR, "examples")


def ensure_dir_exists(path):
    if not os.path.isdir(path):
        os.makedirs(path)


class TestResizeRatioSafe(unittest.TestCase):
    def test_resize_ratio_safe_bg_pink_jpg(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_ratio_safe_bg_pink_jpg")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.jpg"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_ratio_safe_bg_pink(path_source, path_to, width, height)

    def test_resize_ratio_safe_bg_white_jpg(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_ratio_safe_bg_white_jpg")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.jpg"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_ratio_safe_bg_white(path_source, path_to, width, height)

    def test_resize_ratio_safe_bg_black_jpg(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_ratio_safe_bg_black_jpg")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.jpg"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_ratio_safe_bg_black(path_source, path_to, width, height)

    def test_resize_ratio_safe_bg_transparent_png(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_ratio_safe_bg_transparent_png")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.png"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_ratio_safe_bg_transparent(path_source, path_to, width, height)

    def test_resize_ratio_safe_bg_transparent_webp(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_ratio_safe_bg_transparent_webp")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.webp"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_ratio_safe_bg_transparent(path_source, path_to, width, height)


class TestResizeFillCrop(unittest.TestCase):
    def test_resize_fill_crop_bg_pink_jpg(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_fill_crop_bg_pink_jpg")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.jpg"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_fill_crop_bg_pink(path_source, path_to, width, height)

    def test_resize_fill_crop_bg_white_jpg(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_fill_crop_bg_white_jpg")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.jpg"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_fill_crop_bg_white(path_source, path_to, width, height)

    def test_resize_fill_crop_bg_black_jpg(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_fill_crop_bg_black_jpg")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.jpg"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_fill_crop_bg_black(path_source, path_to, width, height)

    def test_resize_fill_crop_bg_transparent_png(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_fill_crop_bg_transparent_png")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.png"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_fill_crop_bg_transparent(path_source, path_to, width, height)

    def test_resize_fill_crop_bg_transparent_webp(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "resize/resize_fill_crop_bg_transparent_webp")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        for width, height in TEST_SIZES:
            TEST_TRANSFORMATION_SIZE_DIR = os.path.join(TEST_TRANSFORMATION_DIR, f"{width}x{height}")
            ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
            for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
                file_name_to = f"{os.path.basename(path_source)[:-4]}.webp"
                path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
                resize_fill_crop_bg_transparent(path_source, path_to, width, height)


class TestRemoveBackgroundExperimental(unittest.TestCase):
    def test_example_V1_png(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "remove/remove_background_kernel_png")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        TEST_TRANSFORMATION_SIZE_DIR = TEST_TRANSFORMATION_DIR
        ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
        for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
            file_name_to = "{}.png".format(os.path.basename(path_source).split(".")[0])
            path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
            remove_background_with_kernel(path_source, path_to)

    def test_example_V1_webp(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "remove/remove_background_kernel_webp")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        TEST_TRANSFORMATION_SIZE_DIR = TEST_TRANSFORMATION_DIR
        ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
        for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
            file_name_to = "{}.webp".format(os.path.basename(path_source).split(".")[0])
            path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
            remove_background_with_kernel(path_source, path_to)

    def test_example_V2_png(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "remove/remove_background_flood_png")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        TEST_TRANSFORMATION_SIZE_DIR = TEST_TRANSFORMATION_DIR
        ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
        for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
            file_name_to = "{}.png".format(os.path.basename(path_source).split(".")[0])
            path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
            remove_background_flood_fill(path_source, path_to)

    def test_example_V2_webp(self):
        TEST_TRANSFORMATION_DIR = os.path.join(OUT_DIR, "remove/remove_background_flood_webp")
        ensure_dir_exists(TEST_TRANSFORMATION_DIR)
        TEST_TRANSFORMATION_SIZE_DIR = TEST_TRANSFORMATION_DIR
        ensure_dir_exists(TEST_TRANSFORMATION_SIZE_DIR)
        for path_source in glob.glob(os.path.join(EXAMPLES_DIR, "*.*")):
            file_name_to = "{}.webp".format(os.path.basename(path_source).split(".")[0])
            path_to = os.path.join(TEST_TRANSFORMATION_SIZE_DIR, file_name_to)
            remove_background_flood_fill(path_source, path_to)


if __name__ == "__main__":
    print(f"\nImages transformed by tests are saved to: \n   {OUT_DIR}\n")
    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    ensure_dir_exists(OUT_DIR)
    unittest.main()
