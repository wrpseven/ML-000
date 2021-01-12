from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import setup
from setuptools.extension import Extension
import numpy

compile_flags = ['-std=c++11']
##compile_flags = ['-stdlib=libc++','-mmacosx-version-min=10.7']

setup(
    ext_modules=cythonize(
        [
            Extension('lib.target_encoding_cpp',     
                      ['target_encoding.pyx'], 
                      languate='c++',
                      include_dirs=[numpy.get_include()],
                      extra_compile_args=compile_flags)

        ],
        build_dir='build',
        compiler_directives=dict(
            always_allow_keywords=True, language_level=3
        )
    ),
    cmdclass=dict(
        build_ext=build_ext
    )
)
