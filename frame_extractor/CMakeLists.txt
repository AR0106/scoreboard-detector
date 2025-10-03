cmake_minimum_required(VERSION 3.10) # Specify the minimum required CMake version
project(FrameExtractor LANGUAGES CXX)      # Define your project name and language(s)

if(POLICY CMP0167)
    cmake_policy(SET CMP0167 NEW)
endif()
set(CMAKE_CXX_STANDARD 17) # Specify the desired C++ standard (e.g., 11, 14, 17, 20, 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON) # Ensure the specified standard is strictly enforced

find_package(Boost REQUIRED)
find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS})
add_executable(FrameExtractor src/main.cpp) # Add an executable target and its source files
target_link_libraries(FrameExtractor ${OpenCV_LIBS} ${Boost_LIBRARIES})
