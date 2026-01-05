from main import password
Score = 0

def check_length():
  if (len(password) > 12):
    Score += 1

def check_uppercase():
  for letter in password:
    if (letter == letter.upper()):
      Score += 1
    return

def check_lowercase():
  for letter in password:
    if (letter == letter.lower()):
      Score += 1
    return

def check_numbers():
  return

def check_symbols():
  return 

def score():
  if (Score < 3):
    msg = "Weak"
  elif (Score >= 3 and Score < 5):
    msg = "Medium"
  else:
    msg = "Strong"
  
  result = print(f"Your Password is: {msg} Password.")
  return result