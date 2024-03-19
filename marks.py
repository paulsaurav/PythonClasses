def calculate_division(marks):
    total_marks = sum(marks)
    percentage = (total_marks/600)*100

    if percentage>= 60:
        return "1st Div"
    elif percentage >= 45:
        return "2nd Div"
    elif percentage>=30:
        return "3rd Div"
    else:
        return "Fail"

def input_marks():
    marks = []
    print("Enter marks for 6 subjects: ")
    for i in range(6):
        subject_mark = float(input(f"Enter marks for subjects {i+1}: "))
        marks.append(subject_mark)
    return marks

ram_marks = input_marks()

ram_division = calculate_division(ram_marks)

print("Ram's divison is: ", ram_division)