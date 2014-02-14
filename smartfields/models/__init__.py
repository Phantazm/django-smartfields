from django.conf import settings
from smartfields.models.base import Model
from smartfields.models.fields import *
from smartfields.models.fields.files import *

if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules(
        [], ["^smartfields\.models\.%sField" % f for f in [
            "Char", "Slug", "File", "Image", ]]) #"Audio", "Video", "PDF", "KML", "HTML"]])