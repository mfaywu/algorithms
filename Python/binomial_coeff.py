#Binomial Coefficient

def bin_coeff (n, k):
    if (n == k or k == 0): 
        return 1
    else:
        return bin_coeff(n-1,k-1) + bin_coeff(n-1, k)

n = input ("Enter n: ")
k = input ("Enter k: ")
print (bin_coeff(n,k))
