#web stack debugging 4

#increase ulimit
file { 'fix nginx'
  ensure  => file,
  path    => '/etc/default/nginx'
  content => template('nginx/nginx_ulimit.erb'),
  notify  => Exec['nginx restart']
}

# restart nginx
-> exec { 'nginx-restart':
command => 'nginx restart',
path    => '/etc/init.d/',
}
