
#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/adriantoro26/project_restful_api.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/project_restful_api

mkdir -p $VIRTUALENV_BASE_PATH
python3 -m venv $VIRTUALENV_BASE_PATH/restful_api_app

$VIRTUALENV_BASE_PATH/restful_api_app/bin/pip install -r $PROJECT_BASE_PATH/project_restful_api/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/project_restful_api/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/project_restful_api/deploy/supervisor_restful_api_app.conf /etc/supervisor/conf.d/restful_api_app.conf
supervisorctl reread
supervisorctl update
supervisorctl restart restful_api_app

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/project_restful_api/deploy/nginx_restful_api_app.conf /etc/nginx/sites-available/restful_api_app.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/restful_api_app.conf /etc/nginx/sites-enabled/restful_api_app.conf
systemctl restart nginx.service

echo "DONE! :)"