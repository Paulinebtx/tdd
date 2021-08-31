# class intRom:
#     def conv_intRom(num):
#         val = [
#                 1000, 900, 500, 400,
#                 100, 90, 50, 40,
#                 10, 9, 5, 4,
#                 1
#                 ]
#         syb = [
#                 "M", "CM", "D", "CD",
#                 "C", "XC", "L", "XL",
#                 "X", "IX", "V", "IV",
#                 "I"
#                 ]
synb = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
       (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def conv_intRom(num):
        
    romanNum = ''

    while num > 0:
        for i, r in synb:
            while num >= i:
                romanNum += r
                num -= i

    return romanNum

# print(intRom().conv_intRom(2))
# print(intRom().conv_intRom(19))
