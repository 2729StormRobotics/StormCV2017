# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot

# Include any dependencies generated for this target.
include CMakeFiles/RobotVision.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/RobotVision.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/RobotVision.dir/flags.make

CMakeFiles/RobotVision.dir/RobotVision.cpp.o: CMakeFiles/RobotVision.dir/flags.make
CMakeFiles/RobotVision.dir/RobotVision.cpp.o: RobotVision.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/RobotVision.dir/RobotVision.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/RobotVision.dir/RobotVision.cpp.o -c /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot/RobotVision.cpp

CMakeFiles/RobotVision.dir/RobotVision.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/RobotVision.dir/RobotVision.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot/RobotVision.cpp > CMakeFiles/RobotVision.dir/RobotVision.cpp.i

CMakeFiles/RobotVision.dir/RobotVision.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/RobotVision.dir/RobotVision.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot/RobotVision.cpp -o CMakeFiles/RobotVision.dir/RobotVision.cpp.s

CMakeFiles/RobotVision.dir/RobotVision.cpp.o.requires:

.PHONY : CMakeFiles/RobotVision.dir/RobotVision.cpp.o.requires

CMakeFiles/RobotVision.dir/RobotVision.cpp.o.provides: CMakeFiles/RobotVision.dir/RobotVision.cpp.o.requires
	$(MAKE) -f CMakeFiles/RobotVision.dir/build.make CMakeFiles/RobotVision.dir/RobotVision.cpp.o.provides.build
.PHONY : CMakeFiles/RobotVision.dir/RobotVision.cpp.o.provides

CMakeFiles/RobotVision.dir/RobotVision.cpp.o.provides.build: CMakeFiles/RobotVision.dir/RobotVision.cpp.o


# Object files for target RobotVision
RobotVision_OBJECTS = \
"CMakeFiles/RobotVision.dir/RobotVision.cpp.o"

# External object files for target RobotVision
RobotVision_EXTERNAL_OBJECTS =

RobotVision: CMakeFiles/RobotVision.dir/RobotVision.cpp.o
RobotVision: CMakeFiles/RobotVision.dir/build.make
RobotVision: /usr/local/lib/libopencv_videostab.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_ts.a
RobotVision: /usr/local/lib/libopencv_superres.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_stitching.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_contrib.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_nonfree.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_ocl.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_gpu.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_photo.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_objdetect.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_legacy.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_video.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_ml.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_calib3d.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_features2d.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_highgui.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_imgproc.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_flann.2.4.13.dylib
RobotVision: /usr/local/lib/libopencv_core.2.4.13.dylib
RobotVision: CMakeFiles/RobotVision.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable RobotVision"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/RobotVision.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/RobotVision.dir/build: RobotVision

.PHONY : CMakeFiles/RobotVision.dir/build

CMakeFiles/RobotVision.dir/requires: CMakeFiles/RobotVision.dir/RobotVision.cpp.o.requires

.PHONY : CMakeFiles/RobotVision.dir/requires

CMakeFiles/RobotVision.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/RobotVision.dir/cmake_clean.cmake
.PHONY : CMakeFiles/RobotVision.dir/clean

CMakeFiles/RobotVision.dir/depend:
	cd /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot /Users/kunalpatel/Documents/Storm/StormCV2017/src/org/usfirst/frc/team2729/robot/CMakeFiles/RobotVision.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/RobotVision.dir/depend

