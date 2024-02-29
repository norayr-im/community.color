# A 'blue' test plugin
# ansible-galaxy collection init local.colors --init-path ./collections/ansible_collections

def is_blue(string):
  blue_values = [
    'blue',
    '#000ff'
  ]

  if string in blue_values:
    return True
  else:
    return False


class TestModule(object):
  ''' Ansible blue test '''

  def tests(self):
    return {
      'blue': is_blue,
    }
