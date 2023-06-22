def add_students_data(roll_number,name, student_class, file="student_data.txt"):
    try:
        f=open("f.txt","a+t")
        data= [f"Roll Number: {roll_number}\n", f"Name: {name}\n", f"Class: {student_class}\n"]
        data.writelines(add_students_data)
        with open(file, "r") as f:
             lines=f.readlines()
             for lines in lines:
                  print(lines.strip())
    except FileNotFoundError:
        print(f"Error:file '{f}' not found.")
    except ArithmeticError:
        print("this is arithmetic class")
    except Exception:
        print("this is exception class")
    finally:
        print("this is finally block")
print("this is outside the try-except block")
