@echo off

rem Check if docker command works
docker ps
if %ERRORLEVEL% neq 0 (
    rem Start Docker Desktop
    echo Docker daemon is not running. Starting docker desktop...
    start "Docker Desktop" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    goto docker_ps_check
    
) else (
    echo Docker is accessable. Continuing with start...
    goto run_compose
)

:docker_ps_check

echo.
echo Waiting for docker daemon to start. Please wait...
echo.
docker ps
if %ERRORLEVEL% neq 0 (
    rem Run command until it works
    timeout /t 5 /nobreak
    goto docker_ps_check
)

:run_compose

cd db

rem Run the container
docker compose up -d

cd ..