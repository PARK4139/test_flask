call ".\.venv\Scripts\activate.bat"
set FLASK_APP=web_service_with_flask
set FLASK_DEBUG=true
set APP_CONFIG_FILE=config\development.py
py ".\main.py"



pause