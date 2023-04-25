def get_user_input():
    examination_grade = input("Write examination grade: ")
    while True:
        try:
            examination_grade = float(examination_grade)
            if examination_grade < 1 or examination_grade > 6:
                raise ValueError
            break
        except ValueError:
            examination_grade = input("Examination grade must be a float number between 1 and 6. Write examination grade: ")
    eye_color = input("What eye color (dark or light): ")
    while eye_color.lower() not in ["dark", "light"]:
        eye_color = input("Please write only dark or light. What eye color (dark or light): ")
    hair_length = input("What hair length (short or long): ")
    while hair_length.lower() not in ["short", "long"]:
        hair_length = input("Please write only short or long. What hair length (short or long): ")
    weather = input("How is Weather (good or bad): ")
    while weather.lower() not in ["good", "bad"]:
        weather = input("Please write only good or bad. How is Weather (good or bad): ")
    return examination_grade, eye_color, hair_length, weather

def grade_exam(final_grade, eye_color, hair_length, weather):
    eye_color_grade = 1 if eye_color.lower() == "dark" else 0
    hair_length_grade = 1 if hair_length.lower() == "short" else 0
    weather_grade = 1 if weather.lower() == "good" else 0
    if eye_color_grade == 1 and hair_length_grade == 1:
        final_grade += final_grade * 0.1
    elif eye_color_grade == 1 and hair_length_grade == 0:
        final_grade -= final_grade * 0.1
    elif eye_color_grade == 0 and hair_length_grade == 1:
        final_grade -= final_grade * 0.1
    elif eye_color_grade == 0 and hair_length_grade == 0:
        final_grade += final_grade * 0.1
    if weather_grade == 0:
        final_grade -= 1

    average_grade = (final_grade + eye_color_grade + hair_length_grade + weather_grade) / 4
    rounded_grade = round(average_grade, 1)
    return rounded_grade