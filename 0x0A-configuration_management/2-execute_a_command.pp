#This code kills a process

exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
}
