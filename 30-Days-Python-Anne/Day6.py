# this code is to print the letters with even indices together followed by space and negative idices
num = int(input('number: '))
for i in range(num):
  if num < 10:
    s = input('String: ')
    if (len(s) >= 2 and len(s) <= 10000):
      s_list = list(s)
      even = [i for i in s if s_list.index(i) % 2 == 0]
      odd = [i for i in s if s_list.index(i) % 2 != 0]
      # print('{} = {}'.format(i, even))
      # print(even)
      # print(odd)
      join_even = ''.join(even)
      join_odd = ''.join(odd)
      print('{} {}'.format(join_even, join_odd))
