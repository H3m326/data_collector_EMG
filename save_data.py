import csv, fileinput, itertools
import shutil, os
import serial
import time

CSV_FILE_NAME: str = "mp_z1_b8.csv" # nombre de archivo csv a utilizar
CSV_FILE_ROUTE: str = "mp/mp_z1_b/" # carpeta para guardarlo mas el nombre
INPUT_SIZE: int = 8192 # buffer de entrada en bytes
BUFFER_SIZE: int = 50000 # numero de elementos a guardar a la vez
BAUD_RATE: int = 9600 # velocidad de comunicacion serial
CSV_LIMIT: int = 600 # maximo de lineas que puede tener el csv
PORT: str = "COM3" # puerto de comunicacion con arduino
CSV_FILE: str = CSV_FILE_ROUTE + CSV_FILE_NAME # carpeta para guardarlo mas el nombre
COLUMN_NAME: str = CSV_FILE_NAME.split(".")[0] # nombre de la columna


def check_file(file_name):
    dir = os.listdir(CSV_FILE_ROUTE)

    if CSV_FILE_NAME in dir:
        if input("\n\nFile already exists, Do u want to append to it? (yes/no): ") != "yes":
            raise FileExistsError 
        


def read_from_serial(serial_port:serial.Serial )->str:

    line:bytes = serial_port.readline()
    if line:
        return line.decode().strip()
    return None


def get_csv_size(csv_file:str)->int:

    num_lines = 0
    try:
        for line in fileinput.input(csv_file):
            num_lines += 1
    except FileNotFoundError:
        pass

    return num_lines - 1 if num_lines != 0 else 0 


def limit_csv_lines(original_file:str, limit:int)->None:
        
        limit = limit + 1

        print(f"limiting csv size to {CSV_LIMIT}...")
        with open(original_file, 'r') as initial_file:
            with open(f'{original_file}_temp.csv', 'w') as temp_file:
                for linea in itertools.islice(initial_file, limit):
                    temp_file.write(linea)

        shutil.move(f'{original_file}_temp.csv', original_file)


def write_buffer_to_csv(buffer:list)->None:

    if buffer:
        with open(CSV_FILE, mode='a', newline='') as csv_file:
            csv_append = csv.writer(csv_file, delimiter=' ', lineterminator="\n")
            csv_append.writerows(buffer)
        buffer.clear()


def cleanup(buffer:list)->None:
    print(f"adding last rows...")
    write_buffer_to_csv(buffer)
    limit_csv_lines(CSV_FILE,CSV_LIMIT)


def add_column_name(column_name:str, csv_file:str)->None:

    print("adding column name...")

    n_lines = get_csv_size(csv_file)

    if n_lines == 0:
        with open(csv_file, mode='a', newline='') as csv_file:
            csv_append = csv.writer(csv_file, delimiter=' ', lineterminator="\n")
            csv_append.writerow([COLUMN_NAME])

    else:

        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            lines = list(reader)

        if lines[0][0] != column_name:
            lines[0][0] = column_name

            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)
    

    print("column name added...")


def main()->None:

    buffer: list = list()
    size:int = get_csv_size(CSV_FILE)
    exception_raised = False

    try:
        check_file(CSV_FILE_NAME)

        print("\nstarting...")

        inicial_time = time.time()

        with serial.Serial(port = PORT, baudrate = BAUD_RATE, timeout = 0.5) as serial_port:

            serial_port.set_buffer_size( rx_size=INPUT_SIZE, tx_size = INPUT_SIZE) 

            add_column_name(COLUMN_NAME,CSV_FILE)

            print("reading serial port...")

            add_time = time.time()

            while True:

                val_sensor = read_from_serial(serial_port)

                if val_sensor:
                    buffer.append([val_sensor])
                    size += 1

                    if len(buffer) >= BUFFER_SIZE:
                        write_buffer_to_csv(buffer)
                        print(f"'{BUFFER_SIZE}' rows added, in: {round(time.time()-add_time,2)} seconds.")
                        add_time = time.time()
                    
                    if size > CSV_LIMIT+1:
                        print(f"csv size limit reached...")
                        break

                        
    except serial.SerialException:
        print(f"Comunication with serial port has failed.")

    except FileExistsError:
        pass

    except Exception as e:
        print(f"Something went wrong: {e}")

    finally:
        cleanup(buffer)
        print(f"Process ended, lasted: {round(time.time()-inicial_time,2)} seconds\n\n")


if __name__ == "__main__":
    main()