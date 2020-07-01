CALL env\Scripts\activate.bat

pip install -r requirements.txt

SET FLASK_APP=run.py
SET FLASK_ENV=development
SET SECRET_KEY=$(python -c 'import uuid; print (uuid.uuid4().hex)')

flask manage init
flask db init

flask run

pause >nul
