def validate_pin(num):
    if num.isdigit():
        if len(num) == 4:
            print(True)
        else:
            print(False)
    else:
        print(False)


validate_pin("1240")
