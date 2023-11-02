#!/bin/bash

BASE_URL="http://localhost:8080/item"
CONTENT_TYPE="Content-Type: application/json"

# curl POST requests
curl -X POST "$BASE_URL" -H "$CONTENT_TYPE" -d '{"fname": "Alice", "lname": "Smith", "country": "Canada"}'
curl -X POST "$BASE_URL" -H "$CONTENT_TYPE" -d '{"fname": "Bob", "lname": "Brown", "country": "Australia"}'
curl -X POST "$BASE_URL" -H "$CONTENT_TYPE" -d '{"fname": "Charlie", "lname": "Davis", "country": "UK"}'
curl -X POST "$BASE_URL" -H "$CONTENT_TYPE" -d '{"fname": "Diana", "lname": "Evans", "country": "USA"}'
curl -X POST "$BASE_URL" -H "$CONTENT_TYPE" -d '{"fname": "Edward", "lname": "Fisher", "country": "New Zealand"}'
