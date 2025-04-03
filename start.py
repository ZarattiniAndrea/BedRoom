import subprocess
import os

def avvia_script(scripts): 
    processi = []
    
    lettura_seriale = scripts[0]
    print(f"Avvio {lettura_seriale} come script in python")
    p = subprocess.Popen(["python", lettura_seriale])
    processi.append(p)
    
    hello = scripts[1]
    print(f"Avvio {hello} come comando")
    p = subprocess.Popen(["flask","--app","hello","run"], cwd=os.path.join(os.getcwd(), "Temp_project"))
    processi.append(p)
    
#punto di inizio 
if __name__ == "__main__":
    lista_script = ["lettura_seriale.py", r"C:\Users\zarat\Documents\Arduino\Temperaturadht11\Temp_project\hello.py"]
 #lista di programmi da avviare
    avvia_script(lista_script)