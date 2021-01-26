# Exercise 3: Algorithmic Test
def romanNumeralConverter(num: int) -> str:

    rule = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }

    romanNum: str = ''
    digitList = [int(digit) for digit in str(num)]
    digitList.reverse()
    for i, digit in enumerate(digitList):
        if digit == 9:
            romanNum = romanNum + rule[10 ** (i+1)] + rule[10 ** i]
        elif 5 <= digit < 9:
            romanNum = romanNum + ((digit - 5) * rule[10 ** i]) + rule[5 * (10 ** i)]
        elif digit == 4:
            romanNum = romanNum + rule[5 * (10 ** i)] + rule[10 ** i] 
        elif 1 <= digit < 4:
            romanNum = romanNum + ( digit * rule[10 ** i])
    romanNum = romanNum[::-1]
    return romanNum

for i in range(900, 1001):
    print(romanNumeralConverter(i))

# total time used: 55 mins
            
        
   
        
