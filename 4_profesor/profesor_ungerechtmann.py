import all_function as alf

examination_grade, eye_color, hair_length, weather = alf.get_user_input()
final_grade = alf.grade_exam(examination_grade, eye_color, hair_length, weather)
print("Final grade: ", round(final_grade, 2))