from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name="Flask-Matomo",
    version="1.1.1",
    url="https://github.com/Lanseuo/flask-matomo",
    license="MIT",
    author="Lucas Hild",
    author_email="contact@lucas-hild.de",
    description="Track requests to your Flask website with Matomo ",
    long_description=long_description,
    packages=["flask_matomo"],
    zip_safe=False,
    include_package_data=True,
    install_requires=["Flask"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
