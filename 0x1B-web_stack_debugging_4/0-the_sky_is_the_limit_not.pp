file { '/etc/default/nginx'
  ensure  => file,
  content => template('nginx/nginx_ulimit.erb'),
}

exec { 'nginx restart':
  command => 'systemctl restart nginx',
}
