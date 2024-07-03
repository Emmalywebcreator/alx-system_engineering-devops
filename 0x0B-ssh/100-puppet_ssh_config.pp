#!/usr/bin/env bash
# using puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.

file {  '/etc/ssh/ssh_config':
  ensure =>  'present',
}

file_line { 'Turn off passed auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication yes',
  replace => true,
}

file_line { 'Declare Identity file':
  ensure => 'present',
  line   => 'IdentityFile ~/.ssh.school',
  match  => '^IdentityFile',
  path   => '/etc/ssh/ssh_config',
}
