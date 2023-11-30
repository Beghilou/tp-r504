#!/bin/bash
docker build -t im-nginx-lb -f dockerfile .


mkdir shared1
mkdir shared2
echo "<h1>Hello1</h1>" > shared1/index.html
echo "<h1>Hello2</h1>" > shared2/index.html
