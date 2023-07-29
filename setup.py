#!/usr/bin/env python

from setuptools import dist

dist.Distribution().fetch_build_eggs(['setuptools_rust'])

from setuptools import setup

from setuptools_rust import Binding, RustExtension


setup(
    name="hc-fib-rust-py",
    version="0.2",
    rust_extensions=[RustExtension(
        ".hc_fib_rust_py.hc_fib_rust_py",
        path="Cargo.toml", binding=Binding.PyO3)],
    packages=["hc_fib_rust_py"],
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Rust",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X",
    ],
    requirements=[
        "pyyaml>=3.13",
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'fib-number = hc_fib_rust_py.fib_number_command:fib_number_command',
            'config-fib = hc_fib_rust_py.config_number_command:config_number_command',            
        ],
    },        
    zip_safe=False,
)
