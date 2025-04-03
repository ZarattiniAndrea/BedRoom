import serial

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
            print(linea) #scrivo a video
            file.write(linea + "\n") #scrivo a file