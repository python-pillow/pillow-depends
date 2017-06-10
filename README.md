pillow-depends
==============

Pillow dependency sources -- cached for ci builds

AppVeyor
--------

These are used in Pillow's [AppVeyor configuration file](https://github.com/python-pillow/Pillow/blob/master/appveyor.yml#L18) like so:

```yaml
install:
- curl -fsSL -o pillow-depends.zip https://github.com/python-pillow/pillow-depends/archive/master.zip
- 7z x pillow-depends.zip -oc:\
- mv c:\pillow-depends-master c:\pillow-depends
- xcopy c:\pillow-depends\*.zip c:\pillow\winbuild\
- xcopy c:\pillow-depends\*.tar.gz c:\pillow\winbuild\
- xcopy /s c:\pillow-depends\test_images\* c:\pillow\tests\images
- cd c:\pillow\winbuild\
- c:\python34\python.exe c:\pillow\winbuild\build_dep.py
- c:\pillow\winbuild\build_deps.cmd
```
