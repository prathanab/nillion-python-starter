from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    sum_int = my_int1 + my_int2
    diff_int = my_int1 - my_int2
    prod_int = my_int1 * my_int2
    div_int = my_int1 / my_int2
    max_int = (my_int1 < my_int2).if_else(my_int2, my_int1)
    min_int = (my_int1 < my_int2).if_else(my_int1, my_int2)
    
    output_sum = Output(sum_int, "sum_output", party1)
    output_diff = Output(diff_int, "diff_output", party1)
    output_prod = Output(prod_int, "prod_output", party1)
    output_div = Output(div_int, "div_output", party1)
    output_max = Output(max_int, "max_output", party1)
    output_min = Output(min_int, "min_output", party1)
    
    return [output_sum, output_diff, output_prod, output_div, output_max, output_min]