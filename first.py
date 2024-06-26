def fullname(first_name, last_name):
    return first_name + " " + last_name

def string_alternative(full_name):
    result = ""
    for i in range(0, len(full_name), 2):
        result += full_name[i]
    return result

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    full_name = fullname(first_name, last_name)
    print("Full Name:", full_name)

    alt = string_alternative(full_name)
    print("Every other character:", alt)
main()
