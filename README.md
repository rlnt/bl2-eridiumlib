# **Eridium Lib** [![Workflow Status][workflow_status_badge]][workflow_status_link] [![Total Downloads][total_downloads_badge]][total_downloads_link] [![License][license_badge]][license] [![Code Style][black_badge]][black_link]

> A [PythonSDK] library for Borderlands which holds utility functions for all our mods.

- PythonSDK: `v0.7.9`
- Mod Menu: `v2.4`

---

## **📑 Notes**
- this is a [PythonSDK] library, you **can't** install it with BLCMM
- it doesn't need to be activated in the Mod Menu within the game


## **🔧 Installation**
1. download the latest **release** from [releases]
2. extract it to:
   - `Borderlands 2\Binaries\Win32\Mods`


## **💻 Developing**
In order to work on this library, you need the latest python files from the `requirements.txt`.

### **Update `dist`**
1. download the embedded Win32 Version of Python 3.7.9 from [here][python_download] and copy the following files into `dist`:
   - `_asyncio.pyd`
   - `_overlapped.pyd`
   - `_queue.pyd`
   - `_socket.pyd`
   - `_ssl.pyd`
   - `libcrypto-1_1.dll`
   - `libssl-1_1.dll`
   - `select.pyd`
   - `unicodedata.pyd`
2. install pipenv:
   - `pip install --user pipenv`
3. run update packages from pypi:
   - `pipenv run pip install -t dist -r requirements.txt --upgrade`.


## **⏰ Changelog**
Everything related to versions and their release notes can be found in the [changelog].


## **🎓 License**
This project and all containing files, except for those in `dist`, are licensed under [LGPL-2.1-or-later][license].

- OpenSSL 1.1 is licensed under [the dual OpenSSL and SSLeay license][openssl_license]
- Python 3.7 is licensed under [the Python License][python_license]

You can find licenses for python packages downloaded with `pip` in their respective `*.dist-info` directory.


<!-- Badges -->
[workflow_status_badge]: https://img.shields.io/github/workflow/status/DAmNRelentless/bl2-eridiumlib/CI?style=flat-square
[workflow_status_link]: https://github.com/DAmNRelentless/bl2-eridiumlib/actions/workflows/main.yml
[total_downloads_badge]: https://img.shields.io/github/downloads/DAmNRelentless/bl2-eridiumlib/total?style=flat-square
[total_downloads_link]: https://github.com/DAmNRelentless/bl2-eridiumlib/releases/latest
[license_badge]: https://img.shields.io/github/license/DAmNRelentless/bl2-eridiumlib?style=flat-square
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square
[black_link]: https://github.com/psf/black

<!-- Links -->
[pythonsdk]: http://borderlandsmodding.com/sdk-mods/
[releases]: https://github.com/DAmNRelentless/bl2-eridiumlib/releases
[python_download]: https://www.python.org/ftp/python/3.7.9/python-3.7.9-embed-win32.zip
[changelog]: CHANGELOG.md
[license]: LICENSE
[openssl_license]: licenses/OpenSSL-1_1
[python_license]: licenses/Python37
