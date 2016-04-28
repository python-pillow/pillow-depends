pillow-depends
==============

Pillow dependency sources -- cached for ci builds

AppVeyor
--------

These are used in Pillow's [AppVeyor configuration file](https://github.com/python-pillow/Pillow/blob/master/appveyor.yml#L15) like so:

```
install:
- git clone https://github.com/python-pillow/pillow-depends.git c:\pillow-depends
- xcopy c:\pillow-depends\*.zip c:\pillow\winbuild\
- xcopy c:\pillow-depends\*.tar.gz c:\pillow\winbuild\
- cd c:\pillow\winbuild\
- c:\python34\python.exe c:\pillow\winbuild\build_dep.py
- c:\pillow\winbuild\build_deps.cmd
```
