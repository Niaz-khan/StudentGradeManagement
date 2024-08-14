from student import Student


def main():
    print("\nWelcome to grade management System\n".upper())
    student = Student()
    while True:
        user_input = input("1 -> Add grades\t\t2 -> find average\nq -> exit\n:) ".title())
        match user_input:
            case "1":
                student.add_grades()
            case "2":
                student.calculate_average()
            case 'q':
                break
            case 'Q':
                break
            case _:
                print("\nchose from the above\n".upper())