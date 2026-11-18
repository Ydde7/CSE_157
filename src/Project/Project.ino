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

// Update with batching 
void loop() {
  
  aZ = myIMU.readFloatAccelZ();
  Serial.println(aZ);

  // Comment / Uncomment to add delay (in millisecond (1 x 10^-3 )
    // Every 10 ms, take a sample -> Samples at a frequency of 100 hz

  delay(10);

    // 200 hz sample rate
  // delay (5);

// 


}