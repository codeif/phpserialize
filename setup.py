from setuptools import setup

with open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="phpserialize3",
    author="Armin Ronacher",
    author_email="armin.ronacher@active-4.com",
    version="0.1.4",
    url="http://github.com/codeif/phpserialize3",
    py_modules=["phpserialize3"],
    description="fork from http://github.com/mitsuhiko/phpserializeh",
    long_description=readme,
    zip_safe=False,
    test_suite="tests",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: PHP",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
