set -o errexit
pip install --upgrade pip
pip install django
pip install django-mathfilters
pip install django-simpleui
pip install django-filter
python -m pip install Pillow

python manage.py migrate
python manage.py superuser



