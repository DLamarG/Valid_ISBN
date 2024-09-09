def valid_ISBN10(isbn): 
  import re
  resultL = []
  for i in isbn:
      ind_10_match_X = re.match(r'[^X]', i)
      ind_10_match_L = re.match(r'[A-Z]', i)
      if isbn.index(i)==9 and ind_10_match_L and ind_10_match_X:
          return False
      if isbn.index(i)!=9 and ind_10_match_L:
          return False
      if len(isbn) != 10:
          return False
      else:
          if i=='X':
              resultL.append(10)
          else:
              resultL.append(int(i))
  count = 1
  mult_Nums = []
  while(len(resultL) > 0):
    num = resultL.pop(0) * count
    mult_Nums.append(num)
    count += 1
  return sum(mult_Nums)%11==0


print(valid_ISBN10('1112223339')) #True
print(valid_ISBN10('048665088X')) #True
print(valid_ISBN10('1234512345')) #True
print(valid_ISBN10('1293')) #True