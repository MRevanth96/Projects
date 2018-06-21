#include <DHT.h>

#define DHTPIN 5                            //Pin D1
#define DHTTYPE DHT11
#define TRIGGER 11 // defining trigger pin
#define ECHO 12 // defining echo pin


DHT dht(DHTPIN, DHTTYPE);
int TouchSensor = 9; //connected to Digital pin D3
int led = 2;

void setup()
{
  Serial.begin(9600); // Communication speed
  pinMode(led, OUTPUT);
  pinMode(TouchSensor, INPUT);
  pinMode(TRIGGER, OUTPUT); //initializing trigger as output
  pinMode(ECHO, INPUT); //initialing trigger as input
  
}
void loop(){
  if(digitalRead(TouchSensor)==HIGH)       //Read Touch sensor signal
   { 
    digitalWrite(led, HIGH);   // if Touch sensor is HIGH, then turn on
    Serial.println("Pressing");
   Temp:   Serial.println("Collecting temperature data.");
  float h = dht.readHumidity();                       // Reading humidity

  float t = dht.readTemperature();                    // Read temperature as Celsius

  if (isnan(h) || isnan(t))                           // Check if any reads failed and exit early (to try again).
  {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.println("Temperature :");
  Serial.println(t);

  Serial.println("Humidity :");
  Serial.println(h);
  void ultrasonic();
  delay(1000);
   }
  else
   {
    digitalWrite(led, LOW);    // if Touch sensor is LOW, then turn off the led
    Serial.println("Press the button");
   }
  delay(1000); // Slow down the output for easier reading
}
void ultrasonic()
{  int duration1, dist1;
  digitalWrite(TRIGGER, LOW); // make trigger low
  delayMicroseconds(2);
  digitalWrite(TRIGGER, HIGH); // make trigger high
  delayMicroseconds(10); //give 10 microsec delay
  digitalWrite(TRIGGER, LOW);
  duration1 = pulseIn(ECHO, HIGH);// It gives the duration of on time in echo
  dist1 = (duration1 / 2) / 29.1; // calibrate the distance using pulse
  // Soundwave travel in 343m/sec it can be converted into 29.155 microsecond/cm.
  Serial.print(dist1); // Print the distance value
  Serial.println("distance");
  delay(500);
  if (dist1<10){
    goto Temp;
    }
    
  
}
