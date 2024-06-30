#This script instals flask from pip3 using puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

#This script install werkzeug from pip3 using puppet

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
