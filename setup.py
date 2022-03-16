import setuptools

with open("README.txt", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AmaraNarasMG",
    version="0.0.1",
    author="Narasimhan M.G.",
    author_email="narasimhanmg@gmail.com",
    description="Amarakosha Based word/sentence generator and analyzer",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="https://github.com/pypa/AmarakoshaBasedGeneratorAnalyzer",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/AmarakoshaBasedGeneratorAnalyzer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True
)