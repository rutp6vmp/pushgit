set -o errexit
pip install -r
python manage.py migrate
python manage.py superuser

