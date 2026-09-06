import re

def is_strong_password(password):
  plen = len(password)
  lc = re.search(r'[a-z]', password)
  uc = re.search(r'[A-Z'], password)
  num = re.search(r'[0-9]', password)
  sym = re.search(r'[!@#$^&*]', password)
  strength = 0
  if plen >= 8:
    strength = strength + 1
  if lc:
    strength = strength + 1
  if uc:
    strength = strength + 1
  if num:
    strength = strength + 1
  if sym:
    strength = strength + 1
  if strength >= 5:
    return 'Your password is strong.'
  if strength >= 3:
    return 'Your password is okay but it could be stronger.'
  return 'Your password is weak.'

while(1):
  password = input("Enter a password to check it's strength, or enter 'C' to exit: ")
  if password == "C":
    break
  print(is_strong_password(password))
