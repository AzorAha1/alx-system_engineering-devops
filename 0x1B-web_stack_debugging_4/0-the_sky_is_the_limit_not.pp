#web stack debugging 4

#increase ulimit
file { '/etc/default/nginx'
  ensure  => file,
  content => template('nginx/nginx_ulimit.erb'),
  notify  => Exec['nginx restart']
}

# restart nginx
-> exec { 'nginx-restart':
command => 'nginx restart',
path    => '/etc/init.d/',
}
