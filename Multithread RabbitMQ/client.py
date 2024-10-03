import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'  # localhost
port = 3000

s.connect((host, port))

while True:
   
    employee_id = input("Enter employee ID: ").upper()
    s.send(employee_id.encode('utf-8'))

    response = s.recv(1024).decode('utf-8')
    if response == 'True':
        print("Employee ID recognized.")

        first_option = input("Salary (S) or Annual Leave (L) Query?: ").upper()
        while first_option not in ('S', 'L'):
            first_option = input("Salary (S) or Annual Leave (L) Query?: ").upper()
        
        s.sendall(first_option.encode('utf-8'))







        if first_option == 'S':
            second_option = input("Current salary (C) or total salary (T) for year?: ").upper()
            while second_option not in ('C', 'T'):
                second_option = input("Current salary (C) or total salary (T) for year?: ").upper()
            s.sendall(second_option.encode('utf-8'))




            if second_option == 'T':
                year = input("What year?: ")
                year = str(year)
                s.sendall(year.encode('utf-8'))

                salary_response = s.recv(1024).decode('utf-8')
                overtime_response = s.recv(1024).decode('utf-8')
                print(f"Total salary for {year}: Basic Pay: {salary_response}")

                print(f"Total salary for {year}: Overtime: {overtime_response}")





            elif second_option == 'C':
                salary_response = s.recv(1024).decode('utf-8')
                print(f"Current salary for {employee_id}: {salary_response}")






        elif first_option == 'L':
            second_option = input("Current Entitlement (C) or Leave taken for year (Y)?: ").upper()
            while second_option not in ('C', 'Y'):
                second_option = input("Current Entitlement (C) or Leave taken for year (Y)?: ").upper()
            s.sendall(second_option.encode('utf-8'))





            if second_option == 'C':
                annual_leave_response = s.recv(1024).decode('utf-8')
                print(f"Current annual leave entitlement: {annual_leave_response}")





            elif second_option == 'Y':
                year = input("What year?: ")
                
                s.sendall(year.encode('utf-8'))

                leave_taken_response = s.recv(1024).decode('utf-8')
                print(f"Leave taken in {year}: {leave_taken_response}")
        
        
        
        
        
        else:
            print("Input not recognized, please enter S or L")
            continue       

    else:
        print("Employee ID not recognized.")
        continue

    exit_option = input("Continue? (C) or Exit (X): ").upper()
    
    while exit_option not in ('C', 'X'):
        print("Incorrect option. Please enter 'C' to continue or 'X' to exit.")
        exit_option = input("Continue? (C) or Exit (X): ").upper()

    if exit_option == 'X':
        s.sendall(exit_option.encode('utf-8 '))
        s.close()
        break
    elif exit_option == 'C':
        continue

