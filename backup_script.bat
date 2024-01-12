@echo off

rem Set the source and destination directories
set "source_directory=Excel"
set "destination_directory=Backup"

rem Create a timestamp for the backup folder
set "backup_timestamp=%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%%time:~6,2%"

rem Create a backup by copying and replacing the entire folder
robocopy "%source_directory%" "%destination_directory%\backup_%backup_timestamp%" /MIR

echo Backup completed at %date% %time%
