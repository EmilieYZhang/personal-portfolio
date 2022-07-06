#!/bin/bash

cd personal-portfolio

git fetch && git reset origin/main --hard

echo #all the environment variables >> .env

# Spin containers down to prevent out of memory issues
docker compose -f docker-compose.prod.yml down

# build new docker container
docker compose -f docker-compose.prod.yml up -d --build
