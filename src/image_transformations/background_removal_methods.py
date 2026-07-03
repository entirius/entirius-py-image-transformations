# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from .lib import remove_bg_cv2_flood, remove_bg_cv2_kernel


def remove_background_experimental(path_source, path_to):
    remove_bg_cv2_kernel(src_path=path_source, out_path=path_to)


def remove_background_with_kernel(path_source, path_to):
    remove_bg_cv2_kernel(src_path=path_source, out_path=path_to)


def remove_background_flood_fill(path_source, path_to):
    remove_bg_cv2_flood(src_path=path_source, out_path=path_to)
