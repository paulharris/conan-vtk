cmake_minimum_required(VERSION 3.16)
project(test_package)

set(CMAKE_VERBOSE_MAKEFILE TRUE)


set (CMAKE_FIND_DEBUG_MODE TRUE)

find_package (vtkbundle REQUIRED)
find_package (VTK
   COMPONENTS
      CommonSystem
   CONFIG
   REQUIRED
   )

set (CMAKE_FIND_DEBUG_MODE FALSE)


# include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()

file(GLOB SOURCE_FILES *.cpp)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME}
   vtkbundle::vtkbundle
   VTK::CommonSystem
   )
