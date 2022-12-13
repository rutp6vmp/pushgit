set -o errexit
pip install --upgrade pip
python manage.py migrate
python manage.py superuser

