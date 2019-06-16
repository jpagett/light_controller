#include <RCSwitch.h>
RCSwitch mySwitch = RCSwitch();

int transmitter_pin = 10;

int pulse_length = 394;

int protocol = 1;

void setup() {
  Serial.begin(9600);

  mySwitch.enableTransmit(transmitter_pin);

  mySwitch.setPulseLength(pulse_length);

  mySwitch.setProtocol(protocol);

  mySwitch.setRepeatTransmit(2);
}
   
void loop() {
  if (Serial.available() > 0) {
    
    String c = "";
    c += Serial.readString();
    
    if (c.equals("lightOff")) {
      mySwitch.send(5056769, 24);
      Serial.println(F("Sent signal.")); 
      }

    if (c.equals("lightOn")) {
      mySwitch.send(5056771, 24);
      Serial.println(F("Sent signal.")); 
      }
    
    if (c.equals("dim")) {
      mySwitch.send(5056772, 24);
      Serial.println(F("Sent signal.")); 
      }
    
    if (c.equals("bright")) {
      mySwitch.send(5056774, 24);
      Serial.println(F("Sent signal.")); 
      }
    
    if (c.equals("prevColor")) {
      mySwitch.send(5056775, 24);
      Serial.println(F("Sent signal.")); 
      }
     
    if (c.equals("nextColor")) {
      mySwitch.send(5056777, 24);
      Serial.println(F("Sent signal.")); 
      }
    
    if (c.equals("slowCycle")) {
      mySwitch.send(5056778, 24);
      Serial.println(F("Sent signal.")); 
      }
    
    if (c.equals("modeSwitch")) {
      mySwitch.send(5056779, 24);
      Serial.println(F("Sent signal.")); 
      }
     
    if (c.equals("fastCycle")) {
      mySwitch.send(5056780, 24);
      Serial.println(F("Sent signal.")); 
      }
       
    if (c.equals("rgbWhite")) {
      mySwitch.send(5056784, 24);
      Serial.println(F("Sent signal.")); 
      }
     
    if (c.equals("trueWhite")) {
      mySwitch.send(5056785, 24);
      Serial.println(F("Sent signal.")); 
      }
    
    if (c.equals("warmWhite")) {
      mySwitch.send(5056786, 24);
      Serial.println(F("Sent signal.")); 
      }
     
    if (c.equals("red")) {
      mySwitch.send(5056787, 24);
      Serial.println(F("Sent signal.")); 
      }
    
    if (c.equals("blue")) {
      mySwitch.send(5056788, 24);
      Serial.println(F("Sent signal.")); 
      }
     
    if (c.equals("green")) {
      mySwitch.send(5056789, 24);
      Serial.println(F("Sent signal."));
      }
  }
}

