def number_name(N):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if (N < 20):
        return d[N]

    if (N < 100):
        if N % 10 == 0: return d[N]
        else: return d[N // 10 * 10] + '-' + d[N % 10]

    if (N < k):
        if N % 100 == 0: return d[N // 100] + ' hundred'
        else: return d[N // 100] + ' hundred and ' + number_name(N % 100)

    if (N < m):
        if N % k == 0: return number_name(N // k) + ' thousand'
        else: return number_name(N // k) + ' thousand, ' + number_name(N % k)
    
def all_numbernames(N):
    number_name(N)

    sum_nummer = 0
    for i in range(1,N+1):
        sum_nummer2 = number_name(i)
        for c in sum_nummer2:
            if c.isalpha():
                sum_nummer += 1
    return sum_nummer

    
def solve_euler_17():
    solve_euler_17 = all_numbernames(1000)
    return solve_euler_17

    
# koden nedover er ikke en del av løsning og 
# brukes ikke i automatisk vurdering. Du kan endre eksemplene eller 
# legge til input() / print() her om du vil, under if __name__...
if __name__ == "__main__": 
    
    if number_name(12) == "twelve":
        print('Yay!')
    else:
        print('Oh! I thought it was twelve')


    if number_name(115) == 'one hundred and fifteen':
        print('115 works')
    else:
        print('115 is broken')
        

    if number_name(342) == 'three hundred and forty-two':
        print('342 works')
    else:
        print('342 is broken')
        

    if all_numbernames(5) == len("one"+"two"+"three"+"four"+"five"):
        print('up to 5 works')
    else:
        print('up to 5 is broken')
    

    if all_numbernames(115) == 1133:
        print('up to 115 works')
    else:
        print('up to 115 is broken')
        

    if all_numbernames(342) == 6117:
        print('up to 342 works')
    else:
        print('up to 342 is broken')
        

    
    if solve_euler_17() == 21124:
        print('Good! You solved Euler 17')
    else:
        print('Try some more')