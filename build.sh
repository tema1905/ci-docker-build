#!/bin/bash
set -e

IMAGE_NAME="allframes-image"

docker build -t $IMAGE_NAME .
