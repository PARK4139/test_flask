set FLASK_APP=web_service_with_flask
set FLASK_DEBUG=true
set APP_CONFIG_FILE="%USERPROFILE%\Desktop\services\web_service_with_flask\config\development.py"
cd "%USERPROFILE%\Desktop\services\web_service_with_flask"
call "%USERPROFILE%\Desktop\services\web_service_with_flask\.venv\Scripts\activate.bat"
py "%USERPROFILE%\Desktop\services\web_service_with_flask\web_flask.py"