:: run using cmd.exe /c "createdbs.bat" on Windows
python manage.py makemigrations data
python manage.py migrate --database=master
python manage.py migrate --database=content