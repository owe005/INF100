# du kan definere flere hjelpefunksjoner om du trenger dem



def print_prime_factors(N): # ikke endre den linjen
    num_list = []
    print('Input:', N)
    ######## din kode her ####
    for i in range(2,N + 1):
        while N % i == 0:
            num_list.append(i)
            N = N / i
        if N == 1:
            break
    
    for i in num_list:
        print(i)
    ##########################
    
    
    
# ikke endre noe nedenfor
if __name__ == "__main__":
    print_prime_factors(10)
    print()
    
    print_prime_factors(27)
    print()
    
    print_prime_factors(28)
    print()
    
    print_prime_factors(53)
    print()
    
    print_prime_factors(14092020)
