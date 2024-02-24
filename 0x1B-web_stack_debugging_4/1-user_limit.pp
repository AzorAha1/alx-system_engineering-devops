#adding new user

#user
user { 'holberton':
  ensure   => present,
  password => 'changeme',
}

#ulimit increase
exec { 'name':
  command => '/bin/echo "holberton soft nofile  1048576" >> /etc/security/limits.conf && ' +
            '/bin/echo "holberton hard nofile  1048578" >> /etc/security/limits.conf',
}


exec { 'permission':
  command => 'usermod -aG sudo holberton',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
