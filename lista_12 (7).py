
def roman(num):
    roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_num = ''
    for value, numeral in roman_map.items():
        count = num // value
        roman_num += numeral * count
        num -= value * count
    return roman_num

def roman_to_int(s):
    roman_map = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    result = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman_map:
            result += roman_map[s[i:i+2]]
            i += 2
        else:
            result += roman_map[s[i]]
            i += 1
    return result

num = int(input("Podaj liczbę:"))
roman_num = roman(num)
print(f'{num} w zapisie rzymskim to {roman_num}')
int_num = roman_to_int(roman_num)
print(f'{roman_num} w zapisie dziesiętnym to {int_num}')
