"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    ### TODO
  #step1
  xvec = x.binary_vec
  yvec = y.binary_vec

  #step2
  xvec, yvec = pad(xvec, yvec)

  #step3(base case)
  if x.decimal_val <= 1 and y.decimal_val <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)

  #step4
  x_left, x_right = split_number(xvec)
  y_left, y_right = split_number(yvec)

  #step5
  left_left = _quadratic_multiply(x_left, y_left)
  right_right = _quadratic_multiply(x_right, y_right)
  left_right = _quadratic_multiply(x_left, y_right)
  right_left = _quadratic_multiply(x_right, y_left)
  middle_term = BinaryNumber(left_right.decimal_val + right_left.decimal_val)

  #step6
  left_term = bitshift(left_left, len(xvec))
  middle_term = bitshift(middle_term, len(xvec)//2)
  right_term = right_right

  #step7
  return BinaryNumber(left_term.decimal_val + middle_term.decimal_val + right_term.decimal_val)
    ###



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000


    
    

