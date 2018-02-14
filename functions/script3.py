#coding: utf-8

def shut_down(s):
  if s == 'yes':
    return "Shutting down"
  elif s == 'no':
    return "Shutdown aborted"
  else:
    return 'Sorry'

s = raw_input('shut down yes or not? ')

print shut_down(s)
