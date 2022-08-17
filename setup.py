from setuptools import find_packages, find_namespace_packages, setup


setup(
    name="hydra_app",
    version="0.1.0",
    license="MIT",
    author="Ricardo Hernández Medina",
    author_email="ricardo.medina@cpr.ku.dk",
    packages=find_packages(exclude=("tests",))
     + find_namespace_packages(include=("hydra_plugins.*",)),
    include_package_data=True,
    install_requires=["hydra-core>=1.0.0"],
)
