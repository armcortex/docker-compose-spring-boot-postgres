#!/bin/bash

BASE_URL="http://localhost:8080/item"

# curl GET requests
curl "${BASE_URL}?id=1"
curl "${BASE_URL}?id=2"
curl "${BASE_URL}?id=3"
curl "${BASE_URL}?id=4"
curl "${BASE_URL}?id=5"
