#!/usr/bin/env bash
# Configuration with puppet

exec { 'http header':
  command => 'sudo apt-get update -y;
  sudo apt-get install nginx -y;
  sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME" /etc/nginx/sites-enabled/default
  sudo nginx service nginx restart',
  provider => shell,
}
