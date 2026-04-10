from PIL import Image
import os
import sys
import math

WIDTH_INCHES = 6.0
HEIGHT_INCHES = 4.0
PRINT_WIDTH  = 1800
PRINT_HEIGHT = 1200
INCHES_TO_MM = 25.4

TARGET_HEIGHT_MM = 47.0
TARGET_WIDTH_MM = 37.0

DPI = 300.0
H_MARGIN_MM = 2.5
W_MARGIN_MM = 10.0
heightPix = int(round(TARGET_HEIGHT_MM / INCHES_TO_MM * DPI))
widthPix = int(round(TARGET_WIDTH_MM / INCHES_TO_MM * DPI))
hMarginPix = int(round(H_MARGIN_MM / INCHES_TO_MM * DPI))
wMarginPix = int(round(W_MARGIN_MM / INCHES_TO_MM * DPI))

print("Width: " + str(widthPix) + "px")
print("Height: " + str(heightPix) + "px")
print("Width Margin: " + str(wMarginPix) + "px")
print("Height Margin: " + str(hMarginPix) + "px")

newSize = (widthPix, heightPix)

infile = sys.argv[1]
f, e = os.path.splitext(infile)
outfile = f + '.jpg'
if infile == outfile:
    outfile = f + "print.jpg"

if os.path.exists(infile):
    inImg = Image.open(infile, 'r')
    outImg = Image.new("RGB", (PRINT_WIDTH, PRINT_HEIGHT), "grey")
    scaledImg = inImg.resize(newSize, Image.Resampling.LANCZOS)
    boxWidth = widthPix + wMarginPix
    boxHeight = heightPix + hMarginPix
    nW = int(math.floor((PRINT_WIDTH - wMarginPix) / boxWidth))
    nH = int(math.floor((PRINT_HEIGHT - hMarginPix) / boxHeight))
    for col in range(nW):
        for row in range(nH):
            left = wMarginPix + col * boxWidth
            upper = hMarginPix + row * boxHeight
            right = left + widthPix
            lower = upper + heightPix
            box = (left, upper, right, lower)
            outImg.paste(scaledImg, box)
    outImg.save(outfile)
                             
    