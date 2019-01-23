#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostAccumulatorsConan(base.BoostBaseConan):
    name = "boost_accumulators"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_accumulators"
    lib_short_names = ["accumulators"]
    header_only_libs = ["accumulators"]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_circular_buffer",
        "boost_concept_check",
        "boost_config",
        "boost_core",
        "boost_fusion",
        "boost_iterator",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_numeric_ublas",
        "boost_parameter",
        "boost_preprocessor",
        "boost_range",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_tuple",
        "boost_type_traits",
        "boost_typeof"
    ]



