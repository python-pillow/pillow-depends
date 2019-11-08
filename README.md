pillow-depends
==============

Pillow dependency sources -- cached for CI builds

Pillow Wheels
-------------

These are used in the [Pillow Wheel Builder](https://github.com/python-pillow/pillow-wheels)

Travis CI
---------

These are used in Travis CI through the [Pillow depends scripts](https://github.com/python-pillow/Pillow/tree/master/depends)

AppVeyor
--------

These are used in Pillow's [AppVeyor configuration file](https://github.com/python-pillow/Pillow/blob/master/.appveyor.yml#L34) like so:

```yaml
install:
- ps: |
      if ($env:PYTHON -eq "C:\Python38rc1-x64") {
        curl -o install_python.ps1 https://raw.githubusercontent.com/matthew-brett/multibuild/d0cf77e62028704875073e3dc4626f61d1c33b0e/install_python.ps1
        .\install_python.ps1
      }
- curl -fsSL -o pillow-depends.zip https://github.com/python-pillow/pillow-depends/archive/master.zip
- 7z x pillow-depends.zip -oc:\
- mv c:\pillow-depends-master c:\pillow-depends
- xcopy c:\pillow-depends\*.zip c:\pillow\winbuild\
- xcopy c:\pillow-depends\*.tar.gz c:\pillow\winbuild\
- xcopy /s c:\pillow-depends\test_images\* c:\pillow\tests\images
- cd c:\pillow\winbuild\
- ps: |
      if ($env:PYTHON -eq "c:/vp/pypy2")
      {
        c:\pillow\winbuild\appveyor_install_pypy2.cmd
      }
- ps: |
      if ($env:PYTHON -eq "c:/vp/pypy3")
      {
        c:\pillow\winbuild\appveyor_install_pypy3.cmd
      }
- ps: |
      if ($env:PYTHON -eq "c:/msys64/mingw32")
      {
        c:\msys64\usr\bin\bash -l -c c:\\pillow\\winbuild\\appveyor_install_msys2_deps.sh
      }
      else
      {
        c:\python37\python.exe c:\pillow\winbuild\build_dep.py
        c:\pillow\winbuild\build_deps.cmd
        $host.SetShouldExit(0)
      }
```
