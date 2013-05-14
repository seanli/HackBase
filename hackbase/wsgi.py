import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = PROJECT_ROOT.split(os.sep)[-1]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % PROJECT_DIR)

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
