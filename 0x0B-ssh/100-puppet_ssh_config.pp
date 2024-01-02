# using puppet to make changes to my configuration file
include stdlib
file_line {'turn off password auth':
  line => 'PasswordAuthentication no',
  path => '/etc/ssh/ssh_config',
}
file_line{'Declare identity file':
  line => 'IdentityFile ~/.ssh/school',
  path => '/etc/ssh/ssh_config',
}
