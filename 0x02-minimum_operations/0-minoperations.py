def minOperations(n):
    if n <= 1:
        return 0
    
    divisor = 2
    number_of_operations = 0

    while n > 1:
        if n % divisor == 0:
            n /= divisor
            number_of_operations += divisor
        else:
            divisor += 1
    
    return number_of_operations
