pillow-depends
==============

Pillow dependency sources -- cached for CI builds

Pillow Wheels
-------------

These are used in the [Pillow Wheel Builder](https://github.com/python-pillow/pillow-wheels)

GitHub Actions
--------------

These are used in GitHub Actions through the [Pillow depends scripts](https://github.com/python-pillow/Pillow/tree/master/depends)

AppVeyor
--------

These are used in Pillow's [AppVeyor configuration file](https://github.com/python-pillow/Pillow/blob/master/.appveyor.yml#L21) like so:

```yaml
install:
- curl -fsSL -o pillow-depends.zip https://github.com/python-pillow/pillow-depends/archive/master.zip
- 7z x pillow-depends.zip -oc:\
- mv c:\pillow-depends-master c:\pillow-depends
- xcopy /S /Y c:\pillow-depends\test_images\* c:\pillow\tests\images
- 7z x ..\pillow-depends\nasm-2.14.02-win64.zip -oc:\
- ..\pillow-depends\gs9540w32.exe /S
- path c:\nasm-2.14.02;C:\Program Files (x86)\gs\gs9.54.0\bin;%PATH%
- cd c:\pillow\winbuild\
- ps: |
        c:\python37\python.exe c:\pillow\winbuild\build_prepare.py -v --depends=C:\pillow-depends\
        c:\pillow\winbuild\build\build_dep_all.cmd
        $host.SetShouldExit(0)
- path C:\pillow\winbuild\build\bin;%PATH%
- '%PYTHON%\%EXECUTABLE% -m pip install -U setuptools'
```
