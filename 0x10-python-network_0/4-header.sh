#!/bin/bash
# curl sends GET req to URL, displays response body
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L