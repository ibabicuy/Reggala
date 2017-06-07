
byte humidity_sensor_pin = A1;
byte humidity_sensor_vcc = 6;
int humidityValue=0;
int VALVE_OPEN_TIME=5000; // The time the valve will be open, when dry is detected. 
String request="";


void setup() {
  // Init the humidity sensor board
  pinMode(humidity_sensor_vcc, OUTPUT);
  digitalWrite(humidity_sensor_vcc, LOW);

  pinMode(13,OUTPUT);

  // Setup Serial
  while (!Serial);
  delay(1000);
  Serial.begin(9600);
}

int readHumiditySensor() {
  digitalWrite(humidity_sensor_vcc, HIGH);
  delay(500);
  int value = analogRead(humidity_sensor_pin);
  digitalWrite(humidity_sensor_vcc, LOW);
  return 1023 - value;
}


// Opens the valve so the water drops, and then waits.
void openValve(){
  
  digitalWrite(13,HIGH);

  // Notify Open valve
  Serial.print("watered");
  
  delay(VALVE_OPEN_TIME);  // The time the valve will be opened.
  digitalWrite(13,LOW);

  
    
}

void loop() {
  

  if (Serial.available() > 0) {
    
    // read the incoming byte:
    request = Serial.readString();
    

    // checks which commands
    if(request == "humidity"){
      humidityValue = readHumiditySensor();
      Serial.print('h');
      Serial.print(humidityValue);
    }else if (request == "water"){
      openValve();
    } 


  }

}

