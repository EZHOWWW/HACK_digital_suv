#!/bin/bash

# need to CmakeList.txt in cpp_file dir
cpp_file_paht=$1
rudion_tools_path=/home/dima/.arduino15/packages/Rudiron/tools

touch "$cpp_file_paht"/../libraries.txt

rm -r build
mkdir build

"$rudion_tools_path"/cmake/default/bin/cmake -DCMAKE_BUILD_TYPE=Release -G Ninja -S "&cpp_file_paht"/.. -B ./build

"$rudion_tools_path"/cmake/default/bin/cmake --build build --target all --

