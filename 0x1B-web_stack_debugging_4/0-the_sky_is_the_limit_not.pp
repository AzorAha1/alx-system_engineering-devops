#web stack debugging 4

#increase ulimit
file { 'fix nginx':
  ensure  => file,
  path    => '/etc/default/nginx'
  content => template('nginx/nginx_ulimit.erb'),
  notify  => Exec['nginx restart']
}

# Restart ngnx
exec { 'nginx-restart':
command => '/usr/sbin/default/nginx restart',
path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
