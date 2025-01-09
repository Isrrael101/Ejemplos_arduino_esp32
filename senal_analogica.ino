#include <Arduino.h>

const int analogPin = 36; // Pin de entrada analógica en el ESP32 (A0 es equivalente al pin 36)

void setup() {
    Serial.begin(115200); // Iniciar comunicación serial a 115200 baudios
    pinMode(analogPin, INPUT); // Configurar el pin de entrada analógica como entrada
}

void loop() {
    int analogValue = analogRead(analogPin); // Leer el valor analógico
    Serial.println(analogValue); // Enviar el valor al monitor serial
    delay(100); // Esperar 100 ms antes de leer nuevamente
}