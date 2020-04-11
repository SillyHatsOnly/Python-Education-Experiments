'''
(Жак Арсак. Программирование игр и головоломок.) Для заданной цифры k найти
такое минимальное целое неотрицательное число, оканчивающееся на k, что,
умножая его на k, мы получим новое число, полученное из предыдущего
вычеркиванием цифры k на конце и приписыванием ее в начале. Строки/кортежи и
иные последовательности не использовать.

Пример:
Input:
4
Output:
102564
'''

'''
ABCDEp = n     ->  ABCDE * 10 + p = n        ->  ABCDE = ( n - p ) / 10
pABCDE = n * p ->  p * 10**k + ABCDE = n * p ->  ABCDE = n * p - p * 10**k

(n - p) / 10 = n * p - p * 10**k
n - p = 10 * n * p - p * 10**(k+1)
n - 10 * n * p = p - p * 10**(k+1)
n * (1 - 10 * p) = p * (1 - 10**(k+1))
n = p*(1-10**(k+1)) / (1-10*p)

'''
def swapfive(n):
    for degree in range(0, 10000):
        numerator =  n*(1 - 10**(degree+1))
        denominator = (1 - 10*n)
        answer = numerator//denominator
        if numerator%denominator == 0:
            return print('your number =', n,'\nAnswer =', int(answer));

swapfive(4)
