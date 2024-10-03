import socket
import threading
import pika


rabbitmq_host = 'localhost'
rabbitmq_port = 5672
rabbitmq_exchange = 'activity_logs'

def publish_activity_log(employee_id, first_option, second_option, ip_address):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
    channel = connection.channel()
    channel.exchange_declare(exchange=rabbitmq_exchange, exchange_type='fanout')
    
    activity_log = f"Employee ID: {employee_id}, FirstOption: {first_option}, SecondOption: {second_option}, IP Address: {ip_address}"
    channel.basic_publish(exchange=rabbitmq_exchange, routing_key='', body=activity_log)
    
    connection.close()

employee_data = {
    "E00123": {
        "name": "John Smith",
        "current_salary": 41000,
        "current_leave": 20,
        "years": {
            2016: {"basic_salary": 25000, "overtime": 3000, "leave_taken": 8},
            2017: {"basic_salary": 28000, "overtime": 3500, "leave_taken": 10},
            2018: {"basic_salary": 30000, "overtime": 4000, "leave_taken": 12},
            2019: {"basic_salary": 32000, "overtime": 4500, "leave_taken": 15},
            2020: {"basic_salary": 35000, "overtime": 5000, "leave_taken": 18},
        },
    },
    "W34562": {
        "name": "Rob Korse",
        "current_salary": 42000,
        "current_leave": 10,
        "years": {
            2016: {"basic_salary": 22000, "overtime": 2500, "leave_taken": 5},
            2017: {"basic_salary": 24000, "overtime": 2800, "leave_taken": 7},
            2018: {"basic_salary": 26000, "overtime": 3000, "leave_taken": 8},
            2019: {"basic_salary": 28000, "overtime": 3500, "leave_taken": 10},
            2020: {"basic_salary": 30000, "overtime": 4000, "leave_taken": 12},
        },
    },
    "R28412": {
        "name": "Barry Toben",
        "current_salary": 40000,
        "current_leave": 15,
        "years": {
            2016: {"basic_salary": 28000, "overtime": 3500, "leave_taken": 10},
            2017: {"basic_salary": 30000, "overtime": 4000, "leave_taken": 12},
            2018: {"basic_salary": 32000, "overtime": 4500, "leave_taken": 15},
            2019: {"basic_salary": 35000, "overtime": 5000, "leave_taken": 18},
            2020: {"basic_salary": 38000, "overtime": 5500, "leave_taken": 20},
        },
    },
}

data_lock = threading.Lock()

def handle_client(client_socket, employee_data):
    while True:
        
        data = client_socket.recv(1024).decode('utf-8')

        employee_id = data.strip()
        if not employee_id:
            break  

        with data_lock:
            if employee_id in employee_data:
                client_socket.send(b'True')
            else:
                client_socket.send(b'False')
                continue  

            
            first_option = client_socket.recv(1024).decode('utf-8')
            second_option = client_socket.recv(1024).decode('utf-8')

            if first_option == 'X':
                client_socket.close()
                publish_activity_log(employee_id, first_option, second_option, client_address[0])
                break  

            if first_option == 'S' and second_option == 'C':
                
                current_salary = str(employee_data[employee_id].get("current_salary", "N/A"))
                client_socket.sendall(current_salary.encode('utf-8'))


            elif first_option == 'S' and second_option == 'T':
                year = client_socket.recv(1024).decode('utf-8')
                year = int(year)
                
                if year in employee_data[employee_id]["years"]:
                    basic_salary = str(employee_data[employee_id]["years"][year]["basic_salary"])
                    overtime = str(employee_data[employee_id]["years"][year]["overtime"])
                    client_socket.sendall(basic_salary.encode('utf-8'))
                    client_socket.sendall(overtime.encode('utf-8'))
                else:
                    client_socket.sendall(b"No such year present in the db")

            elif first_option == 'L' and second_option == 'C':
                
                annual_leave = str(employee_data[employee_id].get("current_leave", "N/A"))
                client_socket.sendall(annual_leave.encode('utf-8'))

            elif first_option == 'L' and second_option == 'Y':
                year = client_socket.recv(1024).decode('utf-8')
                year = int(year)
                
                if year in employee_data[employee_id]["years"]:
                    leave_taken = str(employee_data[employee_id]["years"][year]["leave_taken"])
                    client_socket.sendall(leave_taken.encode('utf-8'))
                else:
                    client_socket.sendall(b"No such year present in the db")
                    continue
                
            publish_activity_log(employee_id, first_option, second_option, client_address[0])            
   
    client_socket.close()






s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'  # localhost
port = 3000

s.bind((host, port))

s.listen()

print(f"Server listening on {host}:{port}")

while True:
    
    client_socket, client_address = s.accept()
    print(f"Connection from {client_address}")

    client_thread = threading.Thread(target=handle_client, args=(client_socket, employee_data))
    client_thread.start()