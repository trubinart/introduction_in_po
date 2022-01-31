def get_polish(string: str):
    result = []
    stack = []

    PRIORITY = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        None: 3,
        '(': 0
    }

    for item in string.replace(' ', ''):

        if item not in PRIORITY:
            result.append(item)

        else:
            last = None if not stack else stack.pop()
            if PRIORITY[last] > PRIORITY[item]:
                result.append(last)

            while PRIORITY[last] < PRIORITY[item]:
                result.append(last)
                last = None if not stack else stack.pop()

            stack.append(item)

    stack.append(eval(string))
    result += stack
    result = ' '.join([str(elem) for elem in result])
    result = result.replace('(', '').replace(')', '').replace('None', '')
    return f'Результат: {result}'


if __name__ == '__main__':
    # assert get_polish('(1 + 2) * 4 + 3') != '1 2 + 4 × 3 + 15', "Что-то сломалось"

    user_input = input('Введите выражение: ')
    print(get_polish(user_input))
