#!/bin/bash

# Check if URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send DELETE request using curl and display the response body
response=$(curl -X DELETE -s -o /dev/null -w "%{http_code}" "$1")
if [ $response -eq 200 ]; then
    curl -X DELETE -s "$1"
else
    echo "Error: HTTP status code $response"
fi
