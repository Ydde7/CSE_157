#include <LSM6DS3.h>
#include <Wire.h>

// See datalogger ex under SD to write to CSV

//Create a instance of class LSM6DS3
LSM6DS3 myIMU(I2C_MODE, 0x6A);    //I2C device address 0x6A
float aZ;
const int numSamples = 119;
int samplesRead = numSamples;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (!Serial);

  pinMode(PD5,OUTPUT);
  digitalWrite(PD5,HIGH);
  //Call .begin() to configure the IMUs
  if (myIMU.begin() != 0) {
    Serial.println("Device error");
  } else {
    Serial.println("aZ");
  }
}

// Note the example uploads data in chunks separated  by motion events.
  // The trigger is a comparison between samples taken due to a motion event (decided by threshold value)
  // Our code should sample at regular 10ms intervals reguardless of motion.
void loop() {
  
  aZ = myIMU.readFloatAccelZ();
  Serial.println(aZ);

  // Comment / Uncomment to add delay
  delay(10);


}