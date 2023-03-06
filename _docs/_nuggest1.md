# Nuggets 1
On Thursday 01 March 2023 13:05 I started ...

https://towardsdatascience.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893

How do I use in my Flask Container?

1. I could clone it during the build, and install it into the Docker Container?
pip install git+https://github.com/siliconmaze/my-shared-package

2. I could reference it as a local folder and install it into a container
 - create a container called my_shared_module
 - install the code on the file-system, and share are a volume with the flask container!
