#!/bin/bash
convert sample.png -crop 350x50+680+310 cropped.png
sleep 0.1
tesseract cropped.png converted
