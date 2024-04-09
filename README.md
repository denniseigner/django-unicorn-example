```
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd djangoapp
python manage.py migrate
python manage.py seed
```