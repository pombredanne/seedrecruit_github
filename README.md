seedrecruit_github
===

a challenge from seedrecruit

instructions
===

* make a virtual environment - i reccomend using virtualenv wrapper - https://virtualenvwrapper.readthedocs.org/en/latest/
* append the line `export DJANGO_SETTINGS_MODULE="seedrecruit.config.settings"` to postactivate.sh in your virtual env.
* make sure you're inside the virtual env.
* install the dependencies - `$ pip install -r requirements.txt`
* `$ cd seedrecruit`
* `$ python setup.py develop`
* fill in an oauth key for in `src/seedrecruit/config/local.py.dist`, removing `.dist` extension
* you should now be able to run tests and the web application `$ django-admin.py runserver`
