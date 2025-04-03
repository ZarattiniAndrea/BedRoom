// Libreria DHT
#include "DHT.h"
#include "LiquidCrystal.h"

// Pin digitale di arduino connesso al DHT
#define DHTPIN 2

// tipo del sensore: DHT 11
#define DHTTYPE DHT11

// inizializzo l'interfaccia del display LCD
LiquidCrystal lcd(7,8,9,10,11,12); 

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  lcd.begin(16,2);
  Serial.begin(9600);
  lcd.print("Benvenuto");
  dht.begin();
  delay(2000);
  lcd.clear();
}

void loop() {
  // Attesa di 2 secondi prima di fornire la misura.
  delay(2000);

  // Lettura dell'umidità
  float h = dht.readHumidity();
  // Lettura della temperatura in gradi Celsius
  float t = dht.readTemperature();

  // Verifica se le si presenta un errore di lettura (e riprova nuovamente)
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Impossibile leggere dal sensore DHT!"));
    return;
  }

  lcd.setCursor(0, 0);
  lcd.print(F("Temp:       "));
  lcd.write(223);
  lcd.print(F(" C"));
  lcd.setCursor(8,0);
  lcd.print(t);
  lcd.setCursor(0,1);
  lcd.print(F("Umid:         %"));
  lcd.setCursor(8,1);
  lcd.print(h);
  Serial.print(F("Temp: "));
  Serial.print(t);
  Serial.print(",");
  Serial.print(F(" Umid: "));
  Serial.print(h);
  Serial.println();
}

