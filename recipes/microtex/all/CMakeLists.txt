cmake_minimum_required(VERSION 3.1)
project(cmake_wrapper)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR})
list(APPEND CMAKE_PREFIX ${CMAKE_CURRENT_LIST_DIR})

include(conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)

add_subdirectory(source_subfolder)
