import os

from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration
from conans.tools import Version


class MagicEnumConan(ConanFile):
    name = "magic_enum"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/Neargye/magic_enum"
    description = "Static reflection for enums (to string, from string, iteration) for modern C++, work with any enum type without any macro or boilerplate code"
    topics = ("cplusplus",
              "cplusplus-17",
              "c-plus-plus",
              "c-plus-plus-17",
              "cpp",
              "cpp17",
              "enum-to-string",
              "string-to-enum",
              "serialization",
              "reflection",
              "metaprogramming",
              "header-only",
              "single-file",
              "no-dependencies")
    license = "MIT"
    no_copy_source = True
    settings = "compiler"

    _source_subfolder = "source_subfolder"

    def configure(self):
        if self.settings.compiler.cppstd:
            tools.check_min_cppstd(self, "17")
        minimum_version = {
            "clang": 5,
            "gcc": "9",
            "Visual Studio": 14.11,
        }.get(str(self.settings.compiler))
        if not minimum_version:
            self.output.warn(
                "Unknown compiler: assuminging compiler supports C++17")
        else:
            if Version(self.settings.compiler.version) < minimum_version:
                raise ConanInvalidConfiguration(
                    "Compiler does not support C++17")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(
            "magic_enum.hpp",
            dst="include",
            src=os.path.join(self._source_subfolder, "include"))
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
