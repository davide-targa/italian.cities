#!/bin/sh

# see https://community.plone.org/t/not-using-bootstrap-py-as-default/620
rm -r ./lib ./include ./local ./bin
python3.7 -m venv .
./bin/pip install -r requirements.txt
./bin/buildout
