#!/bin/bash

# full save path
# full path to Cmake + cpp folder
save_dir=$1
project_dir=$2

rudion_tools_path="$HOME"/.arduino15/packages/Rudiron/tools

cp "$save_dir"/block.cpp "$project_dir"

touch "$project_dir"/libraries.txt

rm -rf build && mkdir build

"$rudion_tools_path"/cmake/default/bin/cmake \
DCMAKE_BUILD_TYPE:STRING=Debug \
-DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE \ 
--no-warn-unused-cli \
-S "$project_dir" \
-B "$project_dir"/build \
-G Ninja

"$rudion_tools_path"/cmake/default/bin/cmake \
  --build "$project_dir"/build \
  --target all --


