# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import cv2
import numpy as np


def remove_bg_cv2_kernel(src_path, out_path):
    """
    1st version of the background removal function which uses the cv2 library.
    """
    img = cv2.imread(src_path, -1)
    img_pix = img[0][0]
    if len(img_pix) == 4 and img_pix[3] == 0:
        tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
        b, g, r, a = cv2.split(img)
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)
        cv2.imwrite(out_path, dst)
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)[1]
        mask = 255 - mask
        kernel = kernel_create()
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = (2 * (mask.astype(np.float32)) - 255.0).clip(0, 255).astype(np.uint8)
        result = img.copy()
        result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
        result[:, :, 3] = mask
        cv2.imwrite(out_path, result)


def remove_bg_cv2_flood(src_path, out_path):
    """
    2nd version of the background removal function which uses the cv2 library.
    """
    img = cv2.imread(src_path, -1)
    img_pix = img[0][0]
    if len(img_pix) == 4 and img_pix[3] == 0:
        tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
        b, g, r, a = cv2.split(img)
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)
        cv2.imwrite(out_path, dst)
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask = cv2.threshold(gray, 251, 255, cv2.THRESH_BINARY)[1]
        masks = 255 - mask
        mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=2, sigmaY=2, borderType=cv2.BORDER_DEFAULT)
        im_floodfill = masks.copy()
        h, w = masks.shape[:2]
        mask = np.zeros((h + 2, w + 2), np.uint8)
        mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=2, sigmaY=2, borderType=cv2.BORDER_DEFAULT)
        cv2.floodFill(im_floodfill, mask, (0, 0), 255)
        cv2.floodFill(im_floodfill, mask, (w - 3, 0), 255)
        cv2.floodFill(im_floodfill, mask, (0, h - 3), 255)
        cv2.floodFill(im_floodfill, mask, (w - 3, h - 3), 255)
        im_floodfill_inv = cv2.bitwise_not(im_floodfill)
        im_out = masks | im_floodfill_inv
        result = img.copy()
        result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
        result[:, :, 3] = im_out
        cv2.imwrite(out_path, result)


#
# Helpers
#


def kernel_create():
    """
    Kernel counting function used to create a mask.
    """
    # regural matrix filled with ones
    ones = np.ones((3, 3), np.uint8)
    # elliptical matrix
    ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # cross-shaped matrix
    cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    # unit matrix
    unit = np.eye(3)
    # zero matrix
    zero = np.zeros(3)
    # return type of kernel you need
    res = [ones, ellipse, cross, unit, zero]
    return res[0]
