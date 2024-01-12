@echo off

rem Set the source and destination directories
set "source_directory=Excel"
set "destination_directory=Backup"

rem Create a timestamp for the backup folder
set "backup_timestamp=%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%%time:~6,2%"

rem Check if the destination folder already exists
if exist "%destination_directory%" (
    set "destination_directory=%destination_directory%\backup_%backup_timestamp%"
)

rem Create a backup by copying and replacing the entire folder
xcopy "%source_directory%" "%destination_directory%" /E /H /C /Y

echo Backup completed at %date% %time%
