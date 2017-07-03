""" finctions to compute """
def checktype(datatype):
    """ checks data type of arguments """
    if isinstance(datatype, int) and datatype > 0:
        pass
    else:
        raise TypeError('argument should be interger greater than 0')

def primenumber(number_range):
    """ Returns  a  list of prime numbers using sieve of erastothenes """
    checktype(number_range)
    number = 2
    output = []
    prime = [True for num in range(number_range+1)]
    while number*number <= number_range:
        if prime[number]:
            for num2 in range(number*2, number_range+ 1, number):
                prime[num2] = False
            number += 1
    for num in range(2, number_range):
        if prime[num]:
            output.append(num)
    return output
