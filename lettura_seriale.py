import serial
import pymysql



### GESTIONE DEL DATABASE ###

DB_NAME="bedroom" #nome del database

def create_database():
    conn = pymysql.connect(host="127.0.0.1",user="root",password="admin")
    conn.cursor().execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
    conn.close()
    
def create_table():
    conn = pymysql.connect(host="127.0.0.1",user="root",password="admin",database=DB_NAME)
    conn.cursor().execute("""
    CREATE TABLE IF NOT EXISTS temperature(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        temperatura INT, 
        umidità INT, 
        ora TIMESTAMP)
    """)


try:
    create_database() # Crea il database se non esiste già
    print("Database created successfully (if needed)")
    create_table()
    print("Table created successfully (if needed)")
    #Posts.create_table() # Crea la tabella "posts" se non esiste già
    #print("Table created successfully (if needed)")
except Exception as e:
    print(f"Error creating table or database: {e}")
    
#connessione al database
try:
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="admin",
        database=DB_NAME
    )
    print("Connessione al database riuscita")
except Exception as e:
     print(f"Setup failed: {e}")
     


# Modifica la porta COM in base al tuo sistema (Es. COM3 su Windows, /dev/ttyUSB0 su Linux)
porta_seriale = "COM13"
baudrate = 9600

# Apri la connessione seriale
ser = serial.Serial(porta_seriale, baudrate)
print("Connessione a", porta_seriale)

with open("dati.txt", "a") as file: #Apro il file in modalità append (con sottointeso try-catch)
    while True: 
        if ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8').strip()
            c = linea.split(",") #separo in c la linea letta sul seriale per ottenere i valori di temperatura e umidità 
            temperatura = int(float(c[0])) #faccio il casting ad un numero intero partendo da un float
            umidità = int(float(c[1]))
            #print(linea) #scrivo a video
            print("Temperatura: ", temperatura , " Umidità: ", umidità)
            file.write(linea + "\n") #scrivo a file