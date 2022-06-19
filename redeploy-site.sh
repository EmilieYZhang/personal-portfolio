#!/bin/bash

tmux kill-server

cd personal-portfolio

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt

echo #all the environment variables >> .env

tmux new-session -d -s my_session 'flask run --host=0.0.0.0'
