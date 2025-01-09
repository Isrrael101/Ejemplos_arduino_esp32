// Definir el pin del LED
const int ledPin = 2;

// Variable para almacenar los datos recibidos
String inputString = "";

void setup() {
  // Inicializar el pin del LED como salida
  pinMode(ledPin, OUTPUT);

  // Iniciar la comunicación serial
  Serial.begin(9600);

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
      // Procesar el comando recibido
      processCommand();

      // Limpiar la cadena de entrada
      inputString = "";
    }
  }
}

// Función para procesar el comando recibido
void processCommand() {
  if (inputString.equals("encender\n")) {
    // Encender el LED
    digitalWrite(ledPin, HIGH);
    Serial.println("LED encendido");
  } else if (inputString.equals("apagar\n")) {
    // Apagar el LED
    digitalWrite(ledPin, LOW);
    Serial.println("LED apagado");
  } else {
    // Comando no reconocido
    Serial.println("Comando no reconocido");
  }
}