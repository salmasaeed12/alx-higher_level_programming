#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the body of the response
curl -sL -o /dev/null -w "%{http_code}\n" "$1" | grep -q 200 && curl -sL "$1"
