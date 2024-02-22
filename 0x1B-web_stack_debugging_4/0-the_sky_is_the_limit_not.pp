#web stack debugging 4

#increase ulimit
file { '/etc/default/nginx'
  ensure  => file,
  content => template('nginx/nginx_ulimit.erb'),
  notify  => Exec['nginx restart']
}

#restart nginx
exec { 'nginx restart':
  command => 'service nginx restart',
  require => File['/etc/default/nginx'],
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin']
}
