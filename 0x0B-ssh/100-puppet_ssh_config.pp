# using puppet to make changes to my configuration file
include stdlib
file_line {'turn off password authentication':
  line => 'PasswordAuthentication no',
  path => '/home/vboxuser/.ssh/config',
}
file_line{'file that contains the priv key':
  line => 'IdentityFile',
  path => '/home/vboxuser/.ssh/config',
}

