#!/bin/bash -eu
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



#!/bin/bash

set -e -x

# Grabs the current libc generated by the Dockerfile and puts it in attachments/

I=pwn-assignement-libc-copy
docker rm $I || true
docker rmi $I || true

docker build -t $I .
libc=$(docker run --rm $I find /  2>/dev/null | grep libc.so.6)
echo "Libc is ${libc}"

docker run --name $I $I /bin/true
docker cp -L ${I}:${libc} attachments/$(basename $libc)

docker rm $I
docker rmi $I
