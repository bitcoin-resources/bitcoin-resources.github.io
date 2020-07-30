#!/bin/sh
bundle update --bundler
git add .
git commit -m "bundle update --bundler"

ncu -u
git add .
git commit -m "ncu -u"

npm install
git add .
git commit -m "npm install"

npm audit fix
git add .
git commit -m "npm audit fix"

bundle update
git add .
git commit -m "bundle update"
