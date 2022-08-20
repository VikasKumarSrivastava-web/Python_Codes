# Problem statement:
# check if input string follows below rules:
#   a) str should start with 'a'.
#   b) 'a' should be followed by 'bb' or 'a' or nothing.
#   c) 'bb' should be followed by 'a' or nothing.
def checkAB(str):
  if len(str) == 0:
    return True
  if str[0] == 'a':
    if len(str[1:]) > 1 and str[1:3] =='bb':
      return checkAB(str[3:])
    else:
      return checkAB(str[1:])
str =  input()
if checkAB(str):
  print('true');
else:
  print('false')