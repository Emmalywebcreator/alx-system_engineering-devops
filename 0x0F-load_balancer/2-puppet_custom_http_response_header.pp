#!/usr/bin/env bash

# Puppet configuration for Nginx

exec { 'install_nginx':
  command => 'sudo apt-get update -y && sudo apt-get install nginx -y',
  provider => shell,
}

exec { 'configure_nginx':
  command => 'sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME" /etc/nginx/sites-available/default && sudo systemctl restart nginx',
  provider => shell,
  require => Exec['install_nginx'],
}
