from setuptools import setup


version = '0.1.0'

install_requires = (
    'djangorestframework>=3.1.0,<3.2',
    'django-push-notifications>=1.2,<1.3',
)

setup(
    name='rest-framework-push-notifications',
    packages=['rest_framework_push_notifications'],
    include_package_data=True,
    version=version,
    description='Rest Framework Serializers and Views for Django push notifications.',
    author='Incuna',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/rest-framework-push-notifications',
    install_requires=install_requires,
    zip_safe=False,
    license='BSD',
)
