#fix 500 server error 
exec { 'fixing php issue':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin']
}