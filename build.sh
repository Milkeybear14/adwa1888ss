#!/bin/sh

# This build script will be used by Netlify to build your Django project.
# It will be executed on the Netlify servers when you deploy your project.

# First, we need to install the necessary Python packages.
pip install -r requirements.txt

# Then, we need to collect static files.
python manage.py collectstatic

# Finally, we need to copy the static files to the publish directory.
cp -r static/ dist/

# The publish directory is the directory that will be served by Netlify.