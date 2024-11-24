#!/bin/bash

# need to CmakeList.txt in cpp_file dir
project_dir=$1
rudion_tools_path=/home/dima/.arduino15/packages/Rudiron/tools

touch "$project_dir"/libraries.txt


rm -rf build
mkdir build

"$rudion_tools_path"/cmake/default/bin/cmake DCMAKE_BUILD_TYPE:STRING=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=TRUE --no-warn-unused-cli -S "$project_dir" -B "$project_dir"/build -G Ninja

"$rudion_tools_path"/cmake/default/bin/cmake --build "$project_dir"/build --target all --


