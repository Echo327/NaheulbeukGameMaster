@echo off

echo Please make sure you have gradio installed (pip install --upgrade gradio)
echo or make sure you have jupyter-notebook installed (pip install --upgrade jupyter)
echo for the appropriate option to work

echo Possible options : build, clean, gradio, ipynb

set /p user_input="Enter the desired option : "

if "%user_input%"=="build" (
    call :build
) else if "%user_input%"=="clean" (
    call :clean
) else if "%user_input%"=="gradio" (
    call :launch_gradio
) else if "%user_input%"=="ipynb" (
    call :launch_ipynb
) else (
    echo Error: Invalid input. Please enter either "gradio" or "ipynb".
    pause
    exit /b 1
)

pause
exit /b 1

rem LABELS

rem build
:build
python backend\resources\generate_jsons.py
exit /b

rem clean
:clean
del /s /q "backend\resources\*.json"
echo All json files in resources have been deleted.
exit /b

rem gradio
:launch_gradio
python frontend\gradio\main.py
exit /b

rem Launch Jupyter-Notebook
:launch_ipynb
jupyter-notebook frontend\fights.ipynb
exit /b
