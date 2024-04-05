#!/bin/bash
if [ -f "/etc/wsl.conf" ]; then
   export DOMAIN=localhost
else
   export DOMAIN=dadaforest.net
fi
docker compose up -d --build
