# du kan definere flere hjelpefunksjoner om du trenger dem
def sjekk_pytag(a, b, c):
    return (a**2) + (b**2) == (c**2)

def pytag_trippel(sum_abc): # ikke endre denne linjen

    for i in range(1, sum_abc):
        for j in range(i+1, sum_abc):
            c = sum_abc - (i + j)
            if(sjekk_pytag(i, j, c)):
                if i + j + c == sum_abc:
                    return i * j * c
                

# ikke endre noe nedenfor
if __name__ == "__main__":
    solution = pytag_trippel(1000)
    print(solution)
    if solution == 31875000:
        print("That's right!")