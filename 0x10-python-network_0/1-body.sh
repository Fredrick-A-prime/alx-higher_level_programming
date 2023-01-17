#!/bin/bash
# sends GET req to URL and display response body
curl -sI cle"$1" | grep -i Content-Length | cut -d " " -f2