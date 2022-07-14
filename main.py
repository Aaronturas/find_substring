def find_substring(str, sub):
  ptr1 = 0
  ptr2 = len(sub) - 1

  while ptr2 <= len(str):
    slide = str[ptr1:ptr2+1]
    if slide == sub:
      print('Found', ptr1, '-', ptr2, '\n')
    ptr1+=1
    ptr2+=1




find_substring('catdogcat', 'dog')
