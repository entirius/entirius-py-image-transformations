# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from .lib import resize_fill_crop, resize_ratio_safe


def resize_ratio_safe_bg_white(path_source, path_to, width, height, quality=85):
    fill_color = (255, 255, 255)
    resize_ratio_safe(
        src_path=path_source,
        out_path=path_to,
        out_x=width,
        out_y=height,
        fill_color=fill_color,
        is_transparent=False,
        quality=quality,
    )


def resize_ratio_safe_bg_black(path_source, path_to, width, height, quality=85):
    fill_color = (0, 0, 0)
    resize_ratio_safe(
        src_path=path_source,
        out_path=path_to,
        out_x=width,
        out_y=height,
        fill_color=fill_color,
        is_transparent=False,
        quality=quality,
    )


def resize_ratio_safe_bg_pink(path_source, path_to, width, height, quality=85):
    fill_color = (250, 37, 125)
    resize_ratio_safe(
        src_path=path_source,
        out_path=path_to,
        out_x=width,
        out_y=height,
        fill_color=fill_color,
        is_transparent=False,
        quality=quality,
    )


def resize_ratio_safe_bg_transparent(path_source, path_to, width, height, quality=85):
    resize_ratio_safe(
        src_path=path_source,
        out_path=path_to,
        out_x=width,
        out_y=height,
        is_transparent=True,
        quality=quality,
    )


def resize_fill_crop_bg_white(path_source, path_to, width, height, quality=85):
    fill_color = (255, 255, 255)
    resize_fill_crop(
        src_path=path_source,
        out_path=path_to,
        out_x=width,
        out_y=height,
        fill_color=fill_color,
        is_transparent=False,
        quality=quality,
    )


def resize_fill_crop_bg_black(path_source, path_to, width, height, quality=85):
    fill_color = (0, 0, 0)
    resize_fill_crop(
        src_path=path_source,
        out_path=path_to,
        out_x=width,
        out_y=height,
        fill_color=fill_color,
        is_transparent=False,
        quality=quality,
    )


def resize_fill_crop_bg_pink(path_source, path_to, width, height, quality=85):
    fill_color = (250, 37, 125)
    resize_fill_crop(
        src_path=path_source,
        out_path=path_to,
        out_x=width,
        out_y=height,
        fill_color=fill_color,
        is_transparent=False,
        quality=quality,
    )


def resize_fill_crop_bg_transparent(path_source, path_to, width, height, quality=85):
    resize_fill_crop(
        src_path=path_source,
        out_path=path_to,
        out_x=width,
        out_y=height,
        is_transparent=True,
        quality=quality,
    )
