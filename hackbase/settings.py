import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = PROJECT_ROOT.split(os.sep)[-1]

try:
    # Generated global environment variable. Format: APPNAME_ENV
    env_name = '%s_ENV' % PROJECT_DIR.upper()
    environment = os.environ[env_name]
    if environment == 'PROD':
        from settings_prod import *
    elif environment == 'QA':
        from settings_qa import *
    else:
        from settings_dev import *
except KeyError:
    from settings_dev import *

# You can add a settings_extra.py file for additional personal configurations
if os.path.isfile(os.path.join(PROJECT_ROOT, 'settings_extra.py')):
    from settings_extra import *
