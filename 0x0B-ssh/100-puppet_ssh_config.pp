# using puppet to make changes to my configuration file
include stdlib
file_line {'turn off password auth':
  line => 'PasswordAuthentication no',
  path => '/home/vboxuser/.ssh/config',
}
file_line{'Declare identity file':
  line => 'IdentityFile',
  path => '/home/vboxuser/.ssh/config',
}
