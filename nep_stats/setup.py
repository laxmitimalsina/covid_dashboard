from distutils.core import setup

setup(
    name='nep_stats',
    version='0.1',
    packages=['nep_stats', ],
    license='(c) Sanjaya Subedi/Laxmi Timalsina',
    long_description='Nepalese data visualization dashboards',
    install_requires=[
        'dash==1.12.0',
        'dash-bootstrap-components==0.10.0',
        'pandas==1.0.3',
        'SQLAlchemy==1.3.17',
        'psycopg2-binary==2.8.5',
        'requests==2.31.0',
    ],
    extras_require={
        'dev': [
            'jupyter==1.0.0',
            'pytest==5.4.2',
            'autopep8==1.5.2',
        ]
    }
)
