# Fix WordPress 501 error by changing phpp to php in wp-settings.php

file { 'fix_wordpress_error':
  path     => '/var/www/wp-settings.php',
  ensure   => present,
  replace  => {
    'phpp' => 'php',
  },
}
