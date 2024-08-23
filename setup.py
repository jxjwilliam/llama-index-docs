from setuptools import find_packages, setup

setup(
    name="my_flask_app",
    version="0.1.0",
    author="ML Support Team",
    description="Python Flask App",
    url="https://artifacts.corp.xperi.com:443/artifactory/xperi-ml-pypi/my_flask_app/0.1.0/",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your package dependencies here
    ],
    package_data={
        "": ["*.env*"],  # Include all '.env' files in the package
        "my_flask_app": ["*.env", "*.txt"],
    },
)
