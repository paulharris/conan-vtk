#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
from conan import ConanFile #, tools
# from conans.tools import os_info, collect_libs
from conan.tools.cmake import CMakeToolchain, CMake #, cmake_layout


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    requires = "vtkbundle/9.1.0"
    options = { "shared": [True,False], "fPIC": [True,False] }
    default_options = {
              "fPIC": True
            , "shared": True
            , "vtk:use_64bit_ids": False
            , "vtk:qt": True
            }

    def build(self):
        cmake = CMake(self)
        print("configuring in the test script")
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.a", dst="bin", src="bin")
        self.copy("*.so*", dst="bin", src="lib")
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        self.run(bin_path)
