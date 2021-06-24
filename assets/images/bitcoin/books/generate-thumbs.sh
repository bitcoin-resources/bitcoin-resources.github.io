#!/bin/sh
magick mogrify -resize "400x400>" -format webp -quality 69 highres/*.jpg
