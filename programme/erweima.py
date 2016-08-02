# -*- coding:utf-8 -*-
from PIL import Image
import qrcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1
)
# 参数 version 表示生成二维码的尺寸大小，取值范围是 1 至 40，最小尺寸 1 会生成 21 * 21 的二维码，version 每增加 1，生成的二维码就会添加 4 尺寸，例如 version 是 2，则生成 25 * 25 的二维码。
# 参数 error_correction 指定二维码的容错系数，分别有以下4个系数：
# ERROR_CORRECT_L: 7%的字码可被容错
# ERROR_CORRECT_M: 15%的字码可被容错
# ERROR_CORRECT_Q: 25%的字码可被容错
# ERROR_CORRECT_H: 30%的字码可被容错
# 参数 box_size 表示二维码里每个格子的像素大小。
# 参数 border 表示边框的格子厚度是多少（默认是4）
qr.add_data("http://www.baidu.com")
qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

icon =Image.open("aaa.png")

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
print "aa"
img.paste(icon, (w, h))
#paste函数的参数为(需要修改的图片，粘贴的起始点的横坐标，粘贴的起始点的纵坐标）

img.save("test_qrcode.png")