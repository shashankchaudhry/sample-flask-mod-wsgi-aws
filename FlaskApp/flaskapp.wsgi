import sys
import logging

logging.basicConfig(stream=sys.stderr)

activate_this = '/var/www/FlaskApp/FlaskApp/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application