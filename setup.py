from setuptools import setup, find_packages

setup(
    name="virtual_toy",
    version="0.56",
    packages=find_packages(),
    install_requires=[
        "PyQt5",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "virtually=virtual_toy.main:launch"
        ]
    },
    author="William Isaiah Jones",
    author_email="babyyodacutefry@gmail.com",
    description="Virtual Toy 0.56 - create and test custom virtual environments",
    url="https://github.com/sussybocca/virtual_toy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
