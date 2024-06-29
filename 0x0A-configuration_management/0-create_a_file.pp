file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  group   => 'www-data',
  content => 'I love Puppet',
}
