file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @("EOF")
    # SSH Client Configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
    | EOF
}

