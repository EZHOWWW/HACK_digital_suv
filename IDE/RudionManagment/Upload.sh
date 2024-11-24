#!/bin/bash

# needs to build
build_path=$1
rudion_tools_path="$HOME"/.arduino15/packages/Rudiron/tools
#chmod a+rw /dev/ttyUSB0

"$rudion_tools_path"/Rudiron\ Programmer/default/Rudiron\ Programmer \ 
  "$rudion_tools_path"/bootloaders/default/MDR32F9Qx_default.hex \
  "$build_path"/Sketch.hex \
  --erase \
  --load \
  --run \
  --speed 8
