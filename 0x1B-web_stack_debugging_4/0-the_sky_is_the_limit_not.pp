#web stack debugging 4

#increase ulimit
file { 'fix nginx'
  ensure  => file,
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
  notify  => Exec['nginx restart']
}

# restart nginx
-> exec { 'nginx-restart':
command => 'nginx restart',
path    => '/etc/init.d/',
}
