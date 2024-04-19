# kill me now please

exec {'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
  onlyif  => 'pgrep killmenow',
}
