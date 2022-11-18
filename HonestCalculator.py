def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


msg_list = ["Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"
            ]
answer = 'y'
memory = 0
while answer == 'y':
    print("Enter an equation")
    (x, operator, y) = input().split()

    if x == 'M':
        x = memory

    if y == 'M':
        y = memory

    if type(float(x)) == str or type(float(y)) == str:
        print("Do you even know what numbers are? Stay focused!")
        continue
    elif operator not in ['-', '+', '*', '/']:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    check(float(x), float(y), operator)

    if operator == '+':
        result = float(x) + float(y)

    elif operator == '-':
        result = float(x) - float(y)

    elif operator == '*':
        result = float(x) * float(y)

    elif operator == '/' and float(y) != 0:
        result = float(x) / float(y)

    else:
        print("Yeah... division by zero. Smart move...")
        continue

    print(result)

    while True:
        print("Do you want to store the result? (y / n):")
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 0
                while True:
                    print(msg_list[msg_index])
                    answer = input()
                    if answer == 'y':
                        if msg_index < 2:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    else:
                        if answer != 'n':
                            continue
                        else:
                            break
                break
            else:
                memory = result
                break
        else:
            if answer != 'n':
                continue
            else:
                break

    while True:
        print("Do you want to continue calculations? (y / n):")
        answer = input()
        if answer == 'y':
            break
        else:
            if answer != 'n':
                continue
            else:
                break
