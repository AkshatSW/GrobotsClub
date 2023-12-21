@echo off
setlocal enabledelayedexpansion

set "counter=1"
set "dir=%~dp0"

for %%F in ("%dir%*") do (
    if /I not "%%~nxF"=="%~nx0" (
        ren "%%F" "!counter!.%%~xF"
        set /a "counter+=1"
    )
)

endlocal
