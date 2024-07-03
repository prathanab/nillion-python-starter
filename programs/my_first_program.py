from nada_dsl import *

def is_prime(n: SecretInteger) -> SecretBoolean:
    result = SecretBoolean(True)
    i = SecretInteger(2)
    zero = SecretInteger(0)
    while i * i <= n:
        result = result & (n % i != zero)
        i = i + 1
    return result

def gcd(a: SecretInteger, b: SecretInteger) -> SecretInteger:
    zero = SecretInteger(0)
    while b != zero:
        a, b = b, a % b
    return a

def nada_main():
    party1 = Party(name="Party1")
    
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    prime_int1 = is_prime(my_int1)
    prime_int2 = is_prime(my_int2)
    
    greatest_common_divisor = gcd(my_int1, my_int2)
    
    is_multiple = ((my_int1 % my_int2) == SecretInteger(0)).if_else(SecretBoolean(True), SecretBoolean(False))
    
    output_prime_int1 = Output(prime_int1, "prime_int1", party1)
    output_prime_int2 = Output(prime_int2, "prime_int2", party1)
    output_gcd = Output(greatest_common_divisor, "gcd_output", party1)
    output_multiple = Output(is_multiple, "is_multiple_output", party1)
    
    return [output_prime_int1, output_prime_int2, output_gcd, output_multiple]

print(nada_main())