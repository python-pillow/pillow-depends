pillow-depends
==============

Pillow dependency sources -- cached for CI builds

Pillow Wheels
-------------

These are used in the [Pillow Wheel Builder](https://github.com/python-pillow/pillow-wheels)

GitHub Actions
--------------

These are used in GitHub Actions through the [Pillow depends scripts](https://github.com/python-pillow/Pillow/tree/main/depends)

AppVeyor
--------

These are used in Pillow's [AppVeyor configuration file](https://github.com/python-pillow/Pillow/blob/main/.appveyor.yml#L21) like so:

```yaml
install:
- '%PYTHON%\%EXECUTABLE% --version'
- curl -fsSL -o pillow-depends.zip https://github.com/python-pillow/pillow-depends/archive/main.zip
- curl -fsSL -o pillow-test-images.zip https://github.com/python-pillow/test-images/archive/main.zip
- 7z x pillow-depends.zip -oc:\
- 7z x pillow-test-images.zip -oc:\
- mv c:\pillow-depends-main c:\pillow-depends
- xcopy /S /Y c:\test-images-main\* c:\pillow\tests\images
- 7z x ..\pillow-depends\nasm-2.15.05-win64.zip -oc:\
- choco install ghostscript --version=10.0.0.20230317
- path c:\nasm-2.15.05;C:\Program Files\gs\gs10.00.0\bin;%PATH%
- cd c:\pillow\winbuild\
- ps: |
        c:\python38\python.exe c:\pillow\winbuild\build_prepare.py -v --depends=C:\pillow-depends\
        c:\pillow\winbuild\build\build_dep_all.cmd
        $host.SetShouldExit(0)
- path C:\pillow\winbuild\build\bin;%PATH%
```
