@echo off

rem Check if font is installed
for /f "delims=" %%f in ('reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /s') do (
    if "%%~f" equ "CHILLER" (
        goto :python_check
    )
)
if exist "%LOCALAPPDATA%\Microsoft\Windows\Fonts\CHILLER.TTF" (
    echo Font is already installed.
    goto :python_check
)

rem Open font installer
echo A font installer will show up. It is recommended to install the font.
app\UI\assets\CHILLER.TTF

rem Perform check again
for /f "delims=" %%f in ('reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /s') do (
    if "%%~f" equ "CHILLER" (
        goto :python_check
    )
)
if exist "%APPDATA%\Local\Microsoft\Windows\Fonts\CHILLER.TTF" (
    goto :python_check
)

echo Font not installed. Application might not appear as expected.

:python_check

rem Check if Python is installed
python --version > nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
    goto docker
)

echo.
echo Python is not installed. The Microsoft Store will open up for installation.
pause
rem Typing in the 'python' command will open up the Microsoft Store.
python

echo.
echo Come back here when the installation is complete.
pause

rem Check if installation was successful
python --version > nul 2>&1
if %errorlevel% equ 0 (
    echo Python has been installed successfully.
) else (
    echo Failed to install Python. Please install it manually.
    goto end
)

:docker

rem Check if Docker is installed
rem If not, install it

rem Check if Docker is installed
if not exist "C:\Program Files\Docker\Docker\Docker Desktop.exe" (

rem Install Docker
echo Installing Docker...

rem Install docker from winget
winget install Docker.DockerDesktop

rem Display a message
echo Docker installation complete.

) else (

rem Docker is already installed
echo Docker is already installed.

)

:acrobat

rem Install Acrobat Reader
winget install Adobe.Acrobat.Reader.64-bit

:pip

rem Install the pip modules
pip install -r requirements_win.txt

:wsl

rem Install/Update WSL for Docker
wsl --update

:end

echo Installation is complete.
pause