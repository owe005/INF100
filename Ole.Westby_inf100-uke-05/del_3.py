# du kan definere flere hjelpefunksjoner om du trenger dem

def print_diamond(N):
    print("Tall:", N)
    for i in range(1, N):
        print(' '*(N-i) + 'X'*(i*2-1) + ' '*(N-i))
    
    for i in range(N, 0, -1):
        print(' '*(N-i) + 'X'*(i*2-1) + ' '*(N-i))
      
    
# ikke endre noe nedenfor
if __name__ == "__main__":
    print_diamond(1)
    print()
    
    print_diamond(2)
    print()
    
    print_diamond(3)
    print()
    
    print_diamond(4)
    print()
    
    print_diamond(10)
