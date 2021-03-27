# **🐞 Troubleshooting**

> If this site opened automatically when you started the game, it means you have an issue with your mod installation.

## **What can be the reasons for this?**
- outdated library version
 - happens if a mod requests a newer version of this library
- module not found error
  - means you didn't install this library at all or it's not installed correctly
- import error
  - means there are functions required by a mod which are not in the library
  - ususally caused by an outdated library version

## **How do I see what the reason is?**
You can usually see the error in the console of the game.

If you don't have a console, you can also take a look at the PythonSDK log which is located here:<br>
`Borderlands2\Binaries\Win32\python-sdk.log`

## **How can I fix my problem?**
- outdated library version:
  - download the latest **release** from [releases] and install it
- module not found error:
  - make sure you installed the EridiumLib correctly
  - it has to be in the right path
    - `Borderlands 2\Binaries\Win32\Mods\EridiumLib`
    - the name of the mod folder is important
- import error:
  - download the latest **release** from [releases] and install it
- other possible solutions:
  - make sure you have the `dist` folder within the mod directory and there are files in it
  - try redownloading the latest **release** from [releases] and make sure the path is correct
  - make sure you didn't download the repository source code, use the release

## **I am still having problems!**
Join our [Discord] and ask for help.


<!-- Links -->
[discord]: https://discordapp.com/invite/Q3qxws6
[releases]: https://github.com/RLNT/bl2_eridium/releases
