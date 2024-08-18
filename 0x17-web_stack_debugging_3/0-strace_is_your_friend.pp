#puppet code that fixes wordpress 501 error by changing phpp to php in /var/www/wp_settings.php

exec { 'fix-wordpress-server-error':,
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/',
}
