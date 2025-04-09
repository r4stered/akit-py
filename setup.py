from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext

__version__ = "0.1.0"

# Define the extension module
ext_modules = [
    Pybind11Extension(
        "conduit._cpp",  # The name of the extension module
        [
            "conduit/cc/ds_reader.cc",
            "conduit/cc/pdp_reader.cc",
            "conduit/cc/pdp_util.cc",
            "conduit/cc/system_reader.cpp",
            "conduit/cc/wpilibio.cpp",
        ],
        include_dirs=["conduit/include"],
        cxx_std=20,  # Use C++17
    ),
]

setup(
    name="conduit",
    version=__version__,
    author="Drew Williams",
    author_email="southerntierrobotics@gmail.com",
    description="Python version of akit's conduit",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    packages=find_packages(where="src"),
    package_dir={"": "conduit"},
    zip_safe=False,
    python_requires=">=3.12",
)
