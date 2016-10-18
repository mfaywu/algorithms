from bitarray import bitarray

bits = bitarray(6000000)
bits.setall(0)

bits[1] = 1

print bits[:10]

import sys

sys.getsizeof(3)