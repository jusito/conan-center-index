import os
import shutil
from contextlib import contextmanager
from conans import AutoToolsBuildEnvironment, ConanFile, tools


class SkiaConan(ConanFile):
    name = "skia"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://skia.org"
    description = "The 2D Graphics Library"
    topics = ("conan", "skia", "chromium")
    license = "BSD-3-Clause"
    short_paths = True
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "depot_tools/cci.20201009"

    skia_options = {
        "skia_enable_android_utils": [True, False],
        "skia_enable_api_available_macro": [True, False],
        "skia_enable_direct3d_debug_layer": [True, False],
        "skia_enable_discrete_gpu": [True, False],
        "skia_enable_flutter_defines": [True, False],
        "skia_enable_fontmgr_FontConfigInterface": [True, False],
        "skia_enable_fontmgr_android": [True, False],
        "skia_enable_fontmgr_custom_directory": [True, False],
        "skia_enable_fontmgr_custom_embedded": [True, False],
        "skia_enable_fontmgr_custom_empty": [True, False],
        "skia_enable_fontmgr_empty": [True, False],
        "skia_enable_fontmgr_fontconfig": [True, False],
        "skia_enable_fontmgr_fuchsia": [True, False],
        "skia_enable_fontmgr_win": [True, False],
        "skia_enable_fontmgr_win_gdi": [True, False],
        "skia_enable_gpu": [True, False],
        "skia_enable_gpu_debug_layers": [True, False],
        "skia_enable_graphite": [True, False],
        "skia_enable_metal_debug_info": [True, False],
        "skia_enable_particles": [True, False],
        "skia_enable_pdf": [True, False],
        "skia_enable_skgpu_v1": [True, False],
        "skia_enable_skgpu_v2": [True, False],
        "skia_enable_skottie": [True, False],
        "skia_enable_skparagraph": [True, False],
        "skia_enable_skrive": [True, False],
        "skia_enable_skshaper": [True, False],
        "skia_enable_sksl": [True, False],
        "skia_enable_sktext": [True, False],
        "skia_enable_skvm_jit_when_possible": [True, False],
        "skia_enable_spirv_validation": [True, False],
        "skia_enable_svg": [True, False],
        "skia_enable_tools": [True, False],
        "skia_enable_vulkan_debug_layers": [True, False],
        "skia_enable_winuwp": [True, False],
        "skia_use_angle": [True, False],
        "skia_use_dawn": [True, False],
        "skia_use_direct3d": [True, False],
        "skia_use_dng_sdk": [True, False],
        "skia_use_egl": [True, False],
        "skia_use_expat": [True, False],
        "skia_use_experimental_xform": [True, False],
        "skia_use_ffmpeg": [True, False],
        "skia_use_fixed_gamma_text": [True, False],
        "skia_use_fontconfig": [True, False],
        "skia_use_fonthost_mac": [True, False],
        "skia_use_freetype": [True, False],
        "skia_use_gl": [True, False],
        "skia_use_harfbuzz": [True, False],
        "skia_use_icu": [True, False],
        "skia_use_libfuzzer_defaults": [True, False],
        "skia_use_libgifcodec": [True, False],
        "skia_use_libheif": [True, False],
        "skia_use_libjpeg_turbo_decode": [True, False],
        "skia_use_libjpeg_turbo_encode": [True, False],
        "skia_use_libpng_decode": [True, False],
        "skia_use_libpng_encode": [True, False],
        "skia_use_libwebp_decode": [True, False],
        "skia_use_libwebp_encode": [True, False],
        "skia_use_lua": [True, False],
        "skia_use_metal": [True, False],
        "skia_use_ndk_images": [True, False],
        "skia_use_piex": [True, False],
        "skia_use_runtime_icu": [True, False],
        "skia_use_sfml": [True, False],
        "skia_use_sfntly": [True, False],
        "skia_use_system_expat": [True, False],
        "skia_use_system_harfbuzz": [True, False],
        "skia_use_system_icu": [True, False],
        "skia_use_system_libjpeg_turbo": [True, False],
        "skia_use_system_libpng": [True, False],
        "skia_use_system_libwebp": [True, False],
        "skia_use_system_zlib": [True, False],
        "skia_use_vma": [True, False],
        "skia_use_vulkan": [True, False],
        "skia_use_webgl": [True, False],
        "skia_use_wuffs": [True, False],
        "skia_use_x11": [True, False],
        "skia_use_xps": [True, False],
        "skia_use_zlib": [True, False],
    }

    options = {
        **skia_options,
        "shared": [True, False],
    }

    default_options = {
        "shared": False,
        "skia_enable_android_utils": False,
        "skia_enable_api_available_macro": True,
        "skia_enable_direct3d_debug_layer": False,
        "skia_enable_discrete_gpu": True,
        "skia_enable_flutter_defines": False,
        "skia_enable_fontmgr_FontConfigInterface": False,
        "skia_enable_fontmgr_android": False,
        "skia_enable_fontmgr_custom_directory": False,
        "skia_enable_fontmgr_custom_embedded": False,
        "skia_enable_fontmgr_custom_empty": False,
        "skia_enable_fontmgr_empty": False,
        "skia_enable_fontmgr_fontconfig": False,
        "skia_enable_fontmgr_fuchsia": False,
        "skia_enable_fontmgr_win": False,
        "skia_enable_fontmgr_win_gdi": False,
        "skia_enable_gpu": True,
        "skia_enable_gpu_debug_layers": False,
        "skia_enable_graphite": False,
        "skia_enable_metal_debug_info": False,
        "skia_enable_particles": True,
        "skia_enable_pdf": False,
        "skia_enable_skgpu_v1": True,
        "skia_enable_skgpu_v2": False,
        "skia_enable_skottie": True,
        "skia_enable_skparagraph": True,
        "skia_enable_skrive": True,
        "skia_enable_skshaper": True,
        "skia_enable_sksl": True,
        "skia_enable_sktext": True,
        "skia_enable_skvm_jit_when_possible": False,
        "skia_enable_spirv_validation": False,
        "skia_enable_svg": True,
        "skia_enable_tools": False,
        "skia_enable_vulkan_debug_layers": False,
        "skia_enable_winuwp": False,
        "skia_use_angle": False,
        "skia_use_dawn": False,
        "skia_use_direct3d": False,
        "skia_use_dng_sdk": True,
        "skia_use_egl": False,
        "skia_use_expat": True,
        "skia_use_experimental_xform": False,
        "skia_use_ffmpeg": False,
        "skia_use_fixed_gamma_text": False,
        "skia_use_fontconfig": False,
        "skia_use_fonthost_mac": True,
        "skia_use_freetype": False,
        "skia_use_gl": True,
        "skia_use_harfbuzz": True,
        "skia_use_icu": True,
        "skia_use_libfuzzer_defaults": True,
        "skia_use_libgifcodec": True,
        "skia_use_libheif": False,
        "skia_use_libjpeg_turbo_decode": True,
        "skia_use_libjpeg_turbo_encode": True,
        "skia_use_libpng_decode": True,
        "skia_use_libpng_encode": True,
        "skia_use_libwebp_decode": True,
        "skia_use_libwebp_encode": True,
        "skia_use_lua": False,
        "skia_use_metal": False,
        "skia_use_ndk_images": False,
        "skia_use_piex": True,
        "skia_use_runtime_icu": False,
        "skia_use_sfml": False,
        "skia_use_sfntly": True,
        "skia_use_system_expat": True,
        "skia_use_system_harfbuzz": True,
        "skia_use_system_icu": True,
        "skia_use_system_libjpeg_turbo": True,
        "skia_use_system_libpng": True,
        "skia_use_system_libwebp": True,
        "skia_use_system_zlib": True,
        "skia_use_vma": False,
        "skia_use_vulkan": False,
        "skia_use_webgl": False,
        "skia_use_wuffs": False,
        "skia_use_x11": False,
        "skia_use_xps": False,
        "skia_use_zlib": True,
    }

    def requirements(self):
        if self.options.skia_use_system_icu:
            self.requires("icu/69.1")
        if self.options.skia_use_system_libjpeg_turbo:
            self.requires("libjpeg-turbo/2.1.1")
        if self.options.skia_use_system_harfbuzz:
            self.requires("harfbuzz/3.0.0")
        if self.options.skia_use_system_libpng:
            self.requires("libpng/1.6.37")
        if self.options.skia_use_system_libwebp:
            self.requires("libwebp/1.2.1")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], destination=self.source_folder)
        self.run("python2 tools/git-sync-deps")

    @property
    def _gn_os(self):
        if tools.is_apple_os(self.settings.os):
            if self.settings.os == "Macos":
                return "mac"
            else:
                return "ios"
        return {
            "Windows": "win",
        }.get(str(self.settings.os), str(self.settings.os).lower())

    @property
    def _gn_arch(self):
        return {
            "x86_64": "x64",
            "armv8": "aarch64",
            "x86": "x86",
        }.get(str(self.settings.arch), str(self.settings.arch))

    @contextmanager
    def _build_context(self):
        if self.settings.compiler == "Visual Studio":
            with tools.vcvars(self.settings):
                yield
        else:
            env_defaults = {}
            if self.settings.compiler == "gcc":
                env_defaults.update({
                    "CC": "gcc",
                    "CXX": "g++",
                    "LD": "g++",
                })
            elif self.settings.compiler in ("clang", "apple-clang"):
                env_defaults.update({
                    "CC": "clang",
                    "CXX": "clang++",
                    "LD": "clang++",
                })
            env = {}
            for key, value in env_defaults.items():
                if not tools.get_env(key):
                    env[key] = value
            with tools.environment_append(env):
                yield

    def build(self):
        skia_args =["{}={}".format(opt, str(val).lower())
                    for opt, val in self.options.items() if opt.startswith('skia_')]

        autotools = AutoToolsBuildEnvironment(self)
        extra_cflags = autotools.flags + ["-D{}".format(d) for d in autotools.defines]
        extra_cflags_c = []
        extra_cflags_cc = autotools.cxx_flags
        extra_ldflags = autotools.link_flags
        # Separate multi-work flags
        extra_ldflags = [flag for long_flag in extra_ldflags for flag in long_flag.split(' ')]
        if self.options.get_safe("fPIC"):
            extra_cflags.append("-fPIC")
        extra_cflags.extend("-I{}".format(inc) for inc in autotools.include_paths)
        if self.settings.compiler == "Visual Studio":
            extra_ldflags.extend("-{}{}".format("LIBPATH:" if self.settings.compiler == "Visual Studio" else "L ", libdir) for libdir in autotools.library_paths)
        else:
            for libdir in autotools.library_paths:
                extra_ldflags = extra_ldflags + ["-L", libdir]
        if self.settings.compiler == "clang":
            if self.settings.compiler.get_safe("libcxx"):
                stdlib = {
                    "libstdc++11": "libstdc++",
                }.get(str(self.settings.compiler.libcxx), str(self.settings.compiler.libcxx))
                extra_cflags_cc.append("-stdlib={}".format(stdlib))
                extra_ldflags.append("-stdlib={}".format(stdlib))
        gn_args = [
            *skia_args,
            "host_os=\\\"{}\\\"".format(self._gn_os),
            "host_cpu=\\\"{}\\\"".format(self._gn_arch),
            "is_debug={}".format(str(self.settings.build_type == "Debug").lower()),
            "extra_cflags=[{}]".format(", ".join(
                ['\\"{}\\"'.format(flag) for flag in extra_cflags])),
            "extra_cflags_c=[{}]".format(", ".join(
                ['\\"{}\\"'.format(flag) for flag in extra_cflags_c])),
            "extra_cflags_cc=[{}]".format(", ".join(
                ['\\"{}\\"'.format(flag) for flag in extra_cflags_cc])),
            "extra_ldflags=[{}]".format(", ".join(
                ['\\"{}\\"'.format(flag) for flag in extra_ldflags])),
        ]
        with self._build_context():
            self.run("gn gen out/Default --args=\"{}\"".format(" ".join(gn_args)), run_environment=True)
            self.run("ninja -C out/Default -j{}".format(tools.cpu_count()), run_environment=True)


    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_folder)
        self.copy(pattern="*", dst="bin", src=self.source_folder)

    def package_info(self):
        bin_path = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH env var with : {}".format(bin_path))
        self.env_info.PATH.append(bin_path)

        self.env_info.DEPOT_TOOLS_UPDATE = "0"
