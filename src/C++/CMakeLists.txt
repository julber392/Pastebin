cmake_minimum_required(VERSION 3.10)
project(hash_module)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenSSL REQUIRED)

add_library(hash_module SHARED hashlib.cpp)

target_link_libraries(hash_module PRIVATE OpenSSL::SSL OpenSSL::Crypto)

set_target_properties(hash_module PROPERTIES POSITION_INDEPENDENT_CODE ON)

set_target_properties(hash_module PROPERTIES
        OUTPUT_NAME "Сhash"
)
