#!/bin/bash

cd personal-portfolio

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt

echo #all the environment variables >> .env

systemctl restart myportfolio
