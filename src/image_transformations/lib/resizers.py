# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from PIL import Image, ImageOps


def resize_ratio_safe(
    src_path,
    out_path,
    out_x,
    out_y,
    fill_color=(255, 255, 255),  # RGB if is_transparent=False
    is_transparent=False,
    quality=85,
):
    src_image = Image.open(src_path)
    src_x, src_y = src_image.size
    if is_transparent:
        fill_color = (0, 0, 0, 0)
        if src_image.mode != "RGBA":
            src_image = src_image.convert("RGBA")
        out_image = Image.new("RGBA", (out_x, out_y), fill_color)
    else:
        if src_image.mode == "RGBA":
            #  transparency i dodaje tlo w ustalonym kolorze
            background = Image.new("RGBA", src_image.size, fill_color)
            src_image = Image.alpha_composite(background, src_image)
            src_image = src_image.convert("RGB")
        out_image = Image.new("RGB", (out_x, out_y), fill_color)
    if src_x == out_x and src_y == out_y:
        out_image = src_image
    else:
        resized_x, resized_y = size_to_size_with_ratio(src_x, src_y, out_x, out_y)
        resized_image = src_image.resize((resized_x, resized_y), Image.Resampling.LANCZOS)
        out_image.paste(resized_image, (round((out_x - resized_x) / 2), round((out_y - resized_y) / 2)))
    out_image.save(out_path, quality=quality)
    src_image.close()
    out_image.close()


def resize_fill_crop(
    src_path,
    out_path,
    out_x,
    out_y,
    fill_color=(255, 255, 255),  # RGB if is_transparent=False
    is_transparent=False,
    quality=85,
):
    src_image = Image.open(src_path)
    src_x, src_y = src_image.size
    if is_transparent:
        if src_image.mode != "RGBA":
            src_image = src_image.convert("RGBA")
    else:
        if src_image.mode == "RGBA":
            #  transparency i dodaje tlo w ustalonym kolorze
            background = Image.new("RGBA", src_image.size, fill_color)
            src_image = Image.alpha_composite(background, src_image)
            src_image = src_image.convert("RGB")
    if src_x == out_x and src_y == out_y:
        pass
    else:
        dif_h = abs(src_x - out_x)
        dif_w = abs(src_y - out_y)
        if dif_h > dif_w:
            wpercent = out_x / float(src_x)
            hsize = int(float(src_y) * float(wpercent))
            src_image = src_image.resize((out_x, hsize), Image.Resampling.LANCZOS)
        else:
            wpercent = out_y / float(src_y)
            wsize = int(float(src_x) * float(wpercent))
            src_image = src_image.resize((wsize, out_y), Image.Resampling.LANCZOS)
    out_image = ImageOps.fit(src_image, (out_x, out_y), Image.Resampling.LANCZOS)
    out_image.save(out_path, quality=quality)
    src_image.close()
    out_image.close()


#
# Helpers
#
def size_to_size_with_ratio(src_x, src_y, out_x, out_y):
    ratio_x = out_x / src_x
    ratio_y = out_y / src_y
    if ratio_x > ratio_y:
        resize_ratio = ratio_y
        resized_y = out_y
        resized_x = round(src_x * resize_ratio)
    else:
        resize_ratio = ratio_x
        resized_x = out_x
        resized_y = round(src_y * resize_ratio)
    return (resized_x, resized_y)
