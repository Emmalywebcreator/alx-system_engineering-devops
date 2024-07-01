file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => @("EOF")
    # SSH Client Configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
    | EOF
}

