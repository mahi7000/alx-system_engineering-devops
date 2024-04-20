# use puppet to set up ssh configuration

file { '/etc/ssh/ssh_config':
  content  => "
    Host 34.229.55.170
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
}
