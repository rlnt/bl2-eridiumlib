# **Eridium Lib**

> A [PythonSDK] library for Borderlands which holds utility functions for all our mods.

- [Discord][discord]
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


## **🐞 Troubleshooting**
What you can do if this website was opened automatically upon starting the game:

- make sure you installed the latest **release** from [releases]
- make sure the EridiumLib sits in the right path
  - `Borderlands 2\Binaries\Win32\Mods\EridiumLib`
- make sure you have the `dist` folder within the mod directory and there are files in it
- if it's still not working, contact us on [Discord]


## **💻 Developing**
In order to work on this library, you need the latest python files from the `requirements.txt`.

### **Update `dist`**
1. download the embedded Win32 Version of Python 3.7.9 from [here][python_download] and copy the following files into `dist`:
   - `_queue.pyd`
   - `_socket.pyd`
   - `_ssl.pyd`
   - `libcrypto-1_1.dll`
   - `libssl-1_1.dll`
   - `select.pyd`
   - `unicodedata.pyd`
2. run update packages from pypi:
   - `pip install -t dist -r requirements.txt --upgrade`.


## **⏰ Changelog**
Everything related to versions and their release notes can be found in the [changelog].


## **🎓 License**
This project and all containing files, except for those in `dist`, are licensed under [GPL-3.0-or-later][license].

- OpenSSL 1.1 is licensed under [the dual OpenSSL and SSLeay license][openssl_license]
- Python 3.7 is licensed under [the Python License][python_license]

You can find licenses for python packages downloaded with `pip` in their respective `*.dist-info` directory.


<!-- Links -->
[pythonsdk]: http://borderlandsmodding.com/sdk-mods/
[discord]: https://discordapp.com/invite/Q3qxws6
[releases]: https://github.com/RLNT/bl2_eridium/releases
[python_download]: https://www.python.org/ftp/python/3.7.9/python-3.7.9-embed-win32.zip
[changelog]: CHANGELOG.md
[license]: LICENSE
[openssl_license]: licenses/OpenSSL-1_1
[python_license]: licenses/Python37
