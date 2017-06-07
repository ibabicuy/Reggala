
byte humidity_sensor_pin = A1;
byte humidity_sensor_vcc = 6;
int humidityValue=0;
int VALVE_OPEN_TIME=5000; // The time the valve will be open, when dry is detected. 
String request="";
unsigned long last_watering = 0;
unsigned long eight_hs_millis = 28800000;

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
  if (shallWater()) {
    digitalWrite(13,HIGH);
  
    // Notify Open valve
    Serial.print("watered");
    
    delay(VALVE_OPEN_TIME);  // The time the valve will be opened.
    digitalWrite(13,LOW);
    last_watering = millis(); 
  } 
}

boolean shallWater(){
  unsigned long time = millis();
  unsigned long diff;
  if (time < last_watering) {
    diff = 4294967295 - time + last_watering;
  }else{
    diff = time - last_watering;
  }
  boolean res = true;
  if (diff < eight_hs_millis){
    res = false;
  }
  return res;
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

