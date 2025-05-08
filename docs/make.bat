@ECHO OFF

REM Command file for Sphinx documentation

SET SPHINXBUILD=sphinx-build
SET SOURCEDIR=source
SET BUILDDIR=build

IF "%SPHINXBUILD%" == "" (
    ECHO.
    ECHO The 'sphinx-build' command was not found. Make sure you have Sphinx installed,
    ECHO then set the SPHINXBUILD environment variable to point to the full
    ECHO path of the 'sphinx-build' executable. Alternatively, add it to your PATH.
    ECHO.
    EXIT /B 1
)

%SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR%\html
IF ERRORLEVEL 1 EXIT /B 1

ECHO.
ECHO Build finished. The HTML pages are in %BUILDDIR%\html.


