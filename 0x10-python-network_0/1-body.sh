#!/bin/bash
# sends GET req to URL and display response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2