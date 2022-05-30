from conans import ConanFile, tools, CMake
from conans.errors import ConanInvalidConfiguration
import os

required_conan_version = ">=1.33.0"


class MicroTexConan(ConanFile):
    name = "microtex"
    url = "https://github.com/NanoMichael/MicroTeX"
    description = "A dynamic, cross-platform, and embeddable LaTeX rendering library "
    license = ("MIT")
    homepage = "https://github.com/NanoMichael/MicroTeX"
    topics = ("android", "latex", "cross-platform", "ubuntu", "macros")
    requires = (
        "tinyxml2/9.0.0",
        "qt/6.2.3",
    )
    default_options = {
        "qt:shared": "True"
    }
    generators = "cmake", "cmake_find_package", "cmake_find_package_multi"
    settings = "os", "arch", "compiler", "build_type"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version],
                  strip_root=True, destination=self._source_subfolder)

    def export_sources(self):
        self.copy("CMakeLists.txt")
        for patch in self.conan_data.get("patches", {}).get(self.version, []):
            self.copy(patch["patch_file"])

    def _patch_sources(self):
        for patch in self.conan_data.get("patches", {}).get(self.version, []):
            tools.patch(**patch)

    def build(self):
        self._patch_sources()
        cmake = CMake(self)
        cmake.definitions["QT"] = "ON"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin/platforms", src="bin/archdatadir/plugins/platforms")
        self.copy("glib*.dll", dst="bin", src="bin")


    def package(self):
        self.copy("DOC/License.txt", src="", dst="licenses")
        self.copy("DOC/unRarLicense.txt", src="", dst="licenses")
        if self.settings.os == "Windows":
            self.copy("*.exe", src="CPP/7zip", dst="bin", keep_path=False)
            self.copy("*.dll", src="CPP/7zip", dst="bin", keep_path=False)

        # TODO: Package the libraries: binaries and headers (add the rest of settings)

    def package_info(self):
        bin_path = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH environment variable: {}".format(bin_path))
        self.env_info.path.append(bin_path)
