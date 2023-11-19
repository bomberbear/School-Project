@echo off

rem Start the DB
call start_db.bat

rem Get the container ID
rem Implementation abuses FOR loop in order to save variables
for /f "tokens=* USEBACKQ" %%F IN (`docker ps -q -f "name=Automated_Labeling_System"`) DO (
    SET container_id=%%F
)

:health_check_loop

rem Get the health status of the container
for /f "tokens=* USEBACKQ" %%F in (`docker inspect -f {{.State.Health.Status}} %container_id%`) DO (
    echo %%F
    if %%F neq healthy (
        echo.
        echo Waiting for DB to start. Please wait.
        timeout /t 5 /nobreak
        goto health_check_loop
    )
)

python .\app\main.py

echo Stopping db...
docker stop %container_id%