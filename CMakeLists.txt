cmake_minimum_required(VERSION 2.6)
include("common.cmake")

# ----------------------------------------
# UVLite
# ----------------------------------------
project(UVLite C)
set(CMAKE_BUILD_TYPE RelWithDebInfo)

add_definitions(-std=gnu99)
#add_definitions(-mavx)
add_definitions(-msse4.1)
add_definitions(-pedantic)
add_definitions(-O3)
add_definitions(-Wall)
add_definitions(-Wextra)
add_definitions(-Wcast-align)
add_definitions(-w)

if (UNIX)
    add_definitions(-DUNIX)
endif (UNIX)

file(GLOB_RECURSE UVLITE_SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/src/UVLite/*.h
    ${CMAKE_CURRENT_SOURCE_DIR}/src/UVLite/*.hpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/UVLite/*.c
    ${CMAKE_CURRENT_SOURCE_DIR}/src/UVLite/*.cpp)

list(SORT UVLITE_SOURCES)
create_source_group("Source Files" "${CMAKE_CURRENT_SOURCE_DIR}/src" ${UVLITE_SOURCES})
include_directories(${CMAKE_SOURCE_DIR}/lib/libuv/include)
include_directories(${CMAKE_SOURCE_DIR}/include)

find_package(Threads REQUIRED)

add_library(UVLite STATIC ${UVLITE_SOURCES})

target_link_libraries (UVLite ${CMAKE_THREAD_LIBS_INIT}
    ${CMAKE_SOURCE_DIR}/lib/libuv/.libs/libuv.a)

GET_PROPERTY(UVLite_location TARGET UVLite PROPERTY LOCATION)

# ----------------------------------------
# Hello world sample
# ----------------------------------------
file(GLOB_RECURSE HELLOWORLD_SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/src/samples/HelloWorld/*.h
    ${CMAKE_CURRENT_SOURCE_DIR}/src/samples/HelloWorld/*.hpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/samples/HelloWorld/*.c
    ${CMAKE_CURRENT_SOURCE_DIR}/src/samples/HelloWorld/*.cpp)

list(SORT HELLOWORLD_SOURCES)
create_source_group("Source Files" "${CMAKE_CURRENT_SOURCE_DIR}/src" ${HELLOWORLD_SOURCES})
include_directories(${CMAKE_SOURCE_DIR}/lib/libuv/include)
include_directories(${CMAKE_SOURCE_DIR}/include)

find_package(Threads REQUIRED)

add_executable (HelloWorld
    ${HELLOWORLD_SOURCES})

add_dependencies(HelloWorld UVLite)

# Libraries to link in reverse order because that's what ld requires.
target_link_libraries (HelloWorld
    ${UVLite_location}
    ${CMAKE_SOURCE_DIR}/lib/libuv/.libs/libuv.a
    ${CMAKE_THREAD_LIBS_INIT})

if (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    target_link_libraries (HelloWorld rt)
endif (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
