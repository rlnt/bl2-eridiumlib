## Development

### Update `dist`

Download the embedded Win32 Version of Python 3.7.9 from [here](https://www.python.org/ftp/python/3.7.9/python-3.7.9-embed-win32.zip) and copy the following files into `dist`:

- `_queue.pyd`
- `_socket.pyd`
- `_ssl.pyd`
- `libcrypto-1_1.dll`
- `libssl-1_1.dll`
- `select.pyd`
- `unicodedata.pyd`

Installing `ujson` may require *Microsoft Visual C++ 14.0 or greater*. Download [build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and install `Microsoft C++ Build Tools`.

Install `pipenv` with `pip`:
```
pip install --user pipenv
```

Pipenv is used to ensure the right version of python is used and the correct package versions are installed.

Then update packages from pypi with
```
pipenv run pip install -t dist -r requirements.txt --upgrade
```

## Licenses

This project and all containing files, except for those in `dist` are licensed under `GPL-3.0-or-later`.

- OpenSSL 1.1 is licensed under [the dual OpenSSL and SSLeay license](licenses/OpenSSL-1_1)
- Python 3.7 is licensed under [the Python License](licenses/Python37)

You can find licenses for python packages downloaded with `pip` in their respective `*.dist-info` directory.