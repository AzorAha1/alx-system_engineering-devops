# using puppet to make changes to my configuration file
file { '/home/vboxuser/.ssh/config':
  ensure  => present,
  content => @("EOF"),
Host 54.197.131.36
    user ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  EOF
  owner   => 'root',
  group   => 'root',
  mode    => '0600'
}
