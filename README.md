#LTE AES TOOL


## GUI 
### Windows Executable
* Batch Process: dist/cryp-bat-GUI.exe
* Single Entry:  dist/cryp-GUI.exe
### Mac and Unix
You could build with pyinstaller: 
pyinstaller -F --noconsole crypt-GUI.py
pyinstaller -F --noconsole crypt-bat-GUI.py


## Script
### Environment
* Unix/ Mac OS/ Windows
* Python 2.7 or above
* WxPython, PyCrypto installed

### How-to
* Batch Process: python crypt-bat.py [batch csv] [out csv]
* Single Entry: python crypt.py -h for more information

## Thanks to: 
* @mitshell for mitshell/CryptoMobile
* @mousevspython for mousevspython/wxpython_by_example /
* @pyinstaller for pyinstaller/pyinstaller 