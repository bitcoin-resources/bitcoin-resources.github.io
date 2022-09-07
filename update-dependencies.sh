#!/bin/sh
bundle update --bundler
git add .
git commit -m "build: bundle update --bundler"

npx npm-check-updates -u
git add .
git commit -m "build: ncu -u"

npm install
git add .
git commit -m "build: npm install"

npm audit fix
git add .
git commit -m "build: npm audit fix"

bundle update
git add .
git commit -m "build: bundle update"
