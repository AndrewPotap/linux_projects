def get_color(letter, number):
    our_dict = {symbol: {num: 'Black!' if num % 2 == 0 else 'White!' for num in range(1, 9)}
                if 'abcdefgh'.index(symbol) % 2 == 0 else {num: 'Black!' if num % 2 == 1
                else 'White!' for num in range(1, 9)} for symbol, num in zip('abcdefgh', range(1, 9))}
    print(our_dict[letter][number])


get_color(input('Enter letter index: '), int(input('Enter number index: ')))
