## Update `vendor`

Update packages from pypi with `pip install -t vendor -r requirements.txt --upgrade`

Update _socket and _ssl by downloading the embedded 32 bit version of Python 3.7 from (here)[https://www.python.org/downloads/] and copying the required modules to `vendor`.

Optionally you can use the python dll and zip and replace them in `Bin32`. 