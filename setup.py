from setuptools import setup, find_packages
"""
The setup to handle the gcp-robot-framework-library
"""

setup(
    name='gcp-robot-framework-library',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'robotframework',
        'google-cloud-compute',
        'google-cloud-pubsub',
        'google-cloud-bigquery',
        # Add other dependencies here
    ],
)
