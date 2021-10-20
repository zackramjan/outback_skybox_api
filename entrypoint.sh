#!/bin/bash
cd /outback_skybox_api
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git pull 
/usr/bin/env python3 /outback_skybox_api/skyboxInflux.py