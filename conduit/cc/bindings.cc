#include <pybind11/pybind11.h>
#include "wpilibio.h"

namespace py = pybind11;

PYBIND11_MODULE(_cpp, m) {
    m.doc() = "C++ extension module for conduit";

}