const1 = 3141592653589793238462643383279502884197169399375105820974944592
const2 = 2718281828459045235360287471352662497757247093699959574966967627

def integer_mult(int1, int2):
  str1 = str(int1)
  str2 = str(int2)
  a = str1[:len(str1)//2]
  b = str1[len(str1)//2:]
  c = str2[:len(str1)//2]
  d = str2[len(str1)//2:]

  if len(a) != 1:
    return (int( '1' + len(str1) * '0') * (integer_mult(a, c)) + int( '1' + len(str1)//2 * '0') * (integer_mult(a, d) + integer_mult(b, c)) + integer_mult(b, d))

  return (int( '1' + len(str1) * '0') * (int(a) * int(c)) + int( '1' + len(str1)//2 * '0') * (int(a) * int(d) + int(b) * int(c)) + int(b) * int(d))

print(integer_mult(const1, const2))