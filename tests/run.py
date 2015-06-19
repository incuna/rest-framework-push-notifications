#! /usr/bin/env python3
"""From http://stackoverflow.com/a/12260597/400691"""
import logging
import sys
from optparse import make_option, OptionParser

import dj_database_url
import django
from colour_runner.django_runner import ColourRunnerMixin
from django.conf import settings
from django.test.runner import DiscoverRunner


logging.getLogger().addHandler(logging.NullHandler())


settings.configure(
    DATABASES={
        'default': dj_database_url.config(
            default='postgres://localhost/rest_framework_push_notifications',
        ),
    },
    INSTALLED_APPS=(
        'push_notifications',

        # Put contenttypes before auth to work around test issue.
        # See: https://code.djangoproject.com/ticket/10827#comment:12
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',
    ),
    MIDDLEWARE_CLASSES=(),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher',),
    ROOT_URLCONF='tests.urls',
    SITE_ID=1,
    REST_FRAMEWORK={
        'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
        'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
    },

    USE_TZ=True,
)

# must be called after the settings were configured
django.setup()


class Runner(ColourRunnerMixin, DiscoverRunner):
    pass


option_list = (
    make_option(
        '-v', '--verbosity', action='store', dest='verbosity', default='1',
        type='choice', choices=['0', '1', '2', '3'],
        help=('Verbosity level; 0=minimal output, 1=normal output, ' +
              '2=verbose output, 3=very verbose output'),
    ),
)

parser = OptionParser(option_list=option_list)
options, args = parser.parse_args()

test_runner = Runner(verbosity=int(options.verbosity))
failures = test_runner.run_tests(args)
if failures:
    sys.exit(1)
