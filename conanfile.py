from conans import ConanFile, tools, os

class BoostAccumulatorsConan(ConanFile):
    name = "Boost.Accumulators"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-accumulators"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["accumulators"]
    requires =  "Boost.Array/1.65.1@bincrafters/testing", \
                      "Boost.Assert/1.65.1@bincrafters/testing", \
                      "Boost.Circular_Buffer/1.65.1@bincrafters/testing", \
                      "Boost.Concept_Check/1.65.1@bincrafters/testing", \
                      "Boost.Config/1.65.1@bincrafters/testing", \
                      "Boost.Core/1.65.1@bincrafters/testing", \
                      "Boost.Fusion/1.65.1@bincrafters/testing", \
                      "Boost.Iterator/1.65.1@bincrafters/testing", \
                      "Boost.Mpl/1.65.1@bincrafters/testing", \
                      "Boost.Numeric_Conversion/1.65.1@bincrafters/testing", \
                      "Boost.Numeric_Ublas/1.65.1@bincrafters/testing", \
                      "Boost.Parameter/1.65.1@bincrafters/testing", \
                      "Boost.Preprocessor/1.65.1@bincrafters/testing", \
                      "Boost.Range/1.65.1@bincrafters/testing", \
                      "Boost.Static_Assert/1.65.1@bincrafters/testing", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
                      "Boost.Tuple/1.65.1@bincrafters/testing", \
                      "Boost.Type_Traits/1.65.1@bincrafters/testing", \
                      "Boost.Typeof/1.65.1@bincrafters/testing"

                      #array3 assert1 circular_buffer8 concept_check5 config0 core2 fusion5 iterator5 mpl5 numeric~conversion6 numeric~ublas12 parameter10 preprocessor0 range7 static_assert1 throw_exception2 tuple4 type_traits3 typeof5
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()