def enter_number():
    total = 0
    while True:
        ent_num = 0
        inputStr = input("Enter a number to add (hit enter if you don't want to add any more numbers): ")
        if inputStr == "":
            break

        try:
            ent_num = int(inputStr)
            total += ent_num
        except ValueError:
            print(f'{inputStr} is not integer!!')
            continue
        #try allows to avoid error if not integer entered

    print(f' Total sum is {total}')



enter_number()