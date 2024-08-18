#fixing wordpress 501 error by changing phpp to php in /var/www/wp_settings.php

exec { 'fix-word_press_server_error':
    command => 'sed -i s/phpp/php/g /var/html/wp-settings',
    path    => '/usr.bin/:bin',
}
