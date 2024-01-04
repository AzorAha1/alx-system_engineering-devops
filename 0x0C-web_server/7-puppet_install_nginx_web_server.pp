# using puppet to install nginx webserver
include stdlib
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}
package { 'nginx':
  ensure => installed,
}
file_line {'nginx config':
  line => 'echo "Hello World" | tee /var/www/html/index.html,',
  path => '/etc/nginx/sites-enabled/default',
}
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "server{
    listen 80;
    server_name localhost;
    location / {
      root /var/www/html;
      index index.html;
    }
    location /redirect_me{
      return 301 http://54.197.131.36;
    }
  }
  ",
}

