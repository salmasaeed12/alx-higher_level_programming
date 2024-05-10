#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
echo $(curl -I $1 | grep -w 'Content-Length:' | awk '{print $2}')
