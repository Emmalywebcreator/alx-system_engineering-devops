#!/usr/bin/env bash
# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.

file { '/etc/ssh/ssh_config':
  ensure => present,
content  => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}

