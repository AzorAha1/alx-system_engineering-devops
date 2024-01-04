# using puppet to install nginx webserver
include stdlib
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}
package { 'nginx':
  ensure => installed,
}
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!'
}
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "server{
    listen 80;
    server_name localhost;
    location / {
      root /var/www/html;
    }
    location /redirect_me{
      return 301 http://54.197.131.36;
    }
  }",
}
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}

