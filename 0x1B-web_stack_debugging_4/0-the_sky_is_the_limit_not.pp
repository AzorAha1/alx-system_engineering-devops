#web stack debugging 4

#increase ulimit
file { 'fix nginx':
  ensure  => file,
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
}

# Restart ngnx
exec { 'nginx-restart':
command => '/bin/systemctl restart nginx',
path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
