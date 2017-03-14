#!/bin/bash

# Delete build output.
rm -rf builds

# Delete gyp related files.
rm -rf gyp-mac-tool
rm -rf bin/gyp

# Delete make related files.
rm -rf Makefile
rm -rf UVLite.Makefile
rm -rf UVLite.target.mk
rm -rf hello_world.target.mk

# Delete Visual Studio related files.
rm -rf _ReSharper.UVLite
rm -rf UVLite.sln
rm -rf UVLite.sdf
rm -rf UVLite.v11.suo
rm -rf UVLite.vcxproj
rm -rf UVLite.vcxproj.filters
rm -rf UVLite.vcxproj.user
rm -rf hello_world.vcxproj
rm -rf hello_world.vcxproj.filters

# Delete Xcode related files.
rm -rf UVLite.xcodeproj

# Delete submodules
rm -rf bin/wrk
rm -rf lib/libuv