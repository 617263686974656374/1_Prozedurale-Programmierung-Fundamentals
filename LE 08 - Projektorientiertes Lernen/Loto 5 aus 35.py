import random
lottoNumbers = []
start_game = 0
#record of winnings
win_jackpot = 0
win_5_plus_zz = 0
win_5 = 0
win_4_plus_zz = 0
win_4 = 0
win_3_plus_zz = 0
win_3 = 0
win_1 = 0
while True:
    try:
        how_many_repeat = int(input("How many times you want repeat: "))
        if how_many_repeat > 10000:
            print("Write max 10000 times !")
            continue
        yourNumbers = input("Write your 6 numbers:  ")
        ls = [int(i) for i in yourNumbers.split()]
        control_input_numbers = {x for x in ls if ls.count(x) > 1}
        numbers_max_min = max(ls)
        if len(ls) < 6 or len(ls) > 6:
            print("Write only 6 Numbers (1 2 3 4 5 6)")
            continue
        elif control_input_numbers:
            print("You cant write duplicate number")
            continue
        elif numbers_max_min > 45:
            print("Write number only from 1 to 45 !")
            continue
        else:
            while start_game < how_many_repeat:
                start_game += 1
                try:  # random numbers from 1 to 45

                    lottoNumbers.extend(range(1, 46))
                    six_numbers_from_lottoNumbers = random.sample(lottoNumbers, 6)

                    for i in six_numbers_from_lottoNumbers:
                        if i in six_numbers_from_lottoNumbers:
                            six_numbers_from_lottoNumbers = random.sample(lottoNumbers, 6)

                    six_numbers_from_lottoNumbers.sort()
                    one_number = random.sample(lottoNumbers, 1)
                    control_one = list(set(six_numbers_from_lottoNumbers) & set(one_number))
                    if control_one:
                        del one_number[0]
                        one_number = random.sample(lottoNumbers, 1)
                        if control_one:
                            del one_number[0]
                            one_number = random.sample(lottoNumbers, 1)

                    controlNumbers = list(set(six_numbers_from_lottoNumbers) & set(ls))
                    yourNumbers_sorted = ls.sort()
                    control_zz = list(set(ls) & set(one_number))

                    # jackpot
                    if len(controlNumbers) == 6:
                        win_jackpot += 1

                        # five plus zz
                    elif len(controlNumbers) == 5 and len(control_zz) == 1:
                        win_5_plus_zz += 1

                        # five
                    elif len(controlNumbers) == 5:
                        win_5 += 1

                        # four plus zz
                    elif len(controlNumbers) == 4 and len(control_zz) == 1:
                        win_4_plus_zz += 1

                        # four
                    elif len(controlNumbers) == 4:
                        win_4 += 1

                        # three plus zz
                    elif len(controlNumbers) == 3 and len(control_zz) == 1:
                        win_3_plus_zz += 1

                        # three
                    elif len(controlNumbers) == 3:
                        win_3 += 1

                    elif len(controlNumbers) == 0:
                        win_1 += 1
                except:
                    print("error")

            print("Your winnig list:")
            print(win_jackpot, " x Jackpot")
            print(win_5, " x 5 numbers")
            print(win_4_plus_zz, " x Four numbers plus one extra")
            print(win_4, " x Four numbers")
            print(win_3_plus_zz, " x Three numbers")
            print(win_3, " x Three numbers")
            print(win_1, " x Nothing")
    except:
        print("Write only correct NUMBERS !")