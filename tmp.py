from z_n import *

# Perform fermat's primality test
n = 15
witnesses = [6, 14, 4]
print "n = {}".format(n)
for witness in witnesses:
    print "{}^{}, mod {}".format(witness, n-1, n)
    print "= {}".format(zn_pow(witness, n-1, n))
    print "prime?", is_prime_by_fermat_test(n, witness)
print

# Generate the coset of 12 in Z_15
g = 12
# elts_generated_by_g_in_zn(g, n)
from pprint import pprint
t = gen_times_table(n)
for row in t:
    print row
find_generator(n)

a = 61
b = 34
print extended_euclidean(a, b)
