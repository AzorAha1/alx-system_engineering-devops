#adding new user

user { 'holberton':
  ensure   => present,
  password => 'changeme',
  shell    => '/bin/bash',
  uid      => '501',
  gid      => '20',
}

exec { 'permission':
  command => 'usermod -aG sudo holberton',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
