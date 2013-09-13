seedrecruit_github
==================

a challenge from seedrecruit

instructions
===
make a virtual enviroment for this...

in postactivate.sh make sure you put the line `export DJANGO_SETTINGS_MODULE="seedrecruit.config.settings"` make sure to source the file afterwards.

then you'll need the dependencies - `pip install -r requirements.txt`
then `cd seedrecruit`
then `python setup.py develop`
