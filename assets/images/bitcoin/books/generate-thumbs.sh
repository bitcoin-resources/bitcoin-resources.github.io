#!/bin/sh
magick mogrify -resize "400x400>" -format webp -quality 69 -path ./ highres/*.jpg
magick mogrify -resize "400x400>" -format jpg -quality 69 -path ./jpg highres/*.jpg
