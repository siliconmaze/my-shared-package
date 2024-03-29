import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mysharedmodule',
    version='0.0.1',
    author='Steve Robinson',
    author_email='steve@cloudy.dog',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mike-huls/toolbox',
    #project_urls = {
    #    "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    #},
    license='MIT',
     packages=['mysharedmodule'],
     #install_requires=['requests'],
)