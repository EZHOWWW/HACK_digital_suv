#!/bin/bash

# needs to build
cpp_file_paht=$ realpath $1
fullpath=$2
rudion_tools_path=/home/dima/.arduino15/packages/Rudiron/tools
chmod a+rw /dev/ttyUSB0

"$rudion_tools_path"/Rudiron\ Programmer/default/Rudiron\ Programmer "$rudion_tools_path"/bootloaders/default/MDR32F9Qx_default.hex ./build/Sketch.hex --erase --load --run --speed 8
