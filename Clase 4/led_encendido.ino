#include <Arduino.h>

// Definir el pin del LED
const int ledPin = 2;  // GPIO2 es el LED integrado en muchas placas ESP32
                       // Puedes cambiar este número según tu conexión

// Variable para almacenar los datos recibidos
String inputString = "";
bool stringComplete = false;

void setup() {
  // Inicializar el pin del LED como salida
  pinMode(ledPin, OUTPUT);

  // Iniciar la comunicación serial
  Serial.begin(115200);
  
  // Esperar a que el puerto serial esté disponible (útil cuando usas el monitor serial)
  while (!Serial) {
    ; // Esperar a que el puerto serial se conecte
  }

  // Reservar memoria para la cadena
  inputString.reserve(200);
}

void loop() {
  // Verificar si hay datos disponibles en el puerto serial
  while (Serial.available()) {
    // Leer el carácter entrante
    char inChar = (char)Serial.read();

    // Añadirlo a la cadena de entrada
    inputString += inChar;

    // Verificar si el carácter es el de nueva línea
    if (inChar == '\n') {
      stringComplete = true;
    }
  }

  // Procesar el comando cuando se ha recibido una línea completa
  if (stringComplete) {
    processCommand();
    // Limpiar la cadena y la bandera
    inputString = "";
    stringComplete = false;
  }
}

// Función para procesar el comando recibido
void processCommand() {
  // Eliminar espacios en blanco al inicio y final
  inputString.trim();
  
  if (inputString == "encender") {
    // Encender el LED
    digitalWrite(ledPin, HIGH);
    Serial.println("LED encendido");
  } 
  else if (inputString == "apagar") {
    // Apagar el LED
    digitalWrite(ledPin, LOW);
    Serial.println("LED apagado");
  } 
  else {
    // Comando no reconocido
    Serial.println("Comando no reconocido");
  }
}