#!/bin/bash
cd /outback_skybox_api
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git pull -b skybox https://github.com/zackramjan/outback_skybox_api.git
/usr/bin/env python3 /outback_skybox_api/skyboxInflux.py