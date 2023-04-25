import random
import statistics
is_horible = 0
is_good = 0
is_perfect = 0
how_many = int(input("How many people will controll it: "))
new_number = []
for i in range(1, how_many + 1):
    rating = random.randrange(1, 4)
    new_number.append(rating)
    if rating == 1:
        is_horible += 1
    elif rating == 2:
        is_good += 1
    elif rating == 3:
        is_perfect +=1
x = statistics.harmonic_mean((new_number))
average1 = (is_horible / how_many)*100
average2 = (is_good / how_many)*100
average3 = (is_perfect / how_many)*100
print("Overall product rating is: ", round(x, 2))
print("Iphone is not good: ", is_horible, "people said it and that is: ", int(average1), "%" )
print("Iphone is good: ", is_good, "people said it and that is: ", int(average2), "%")
print("Iphone is perfect: ", is_perfect, "people said it and that is: ", int(average3), "%")


