int throttle  = 0;
int yaw       = 255/2; // 3.3v / 2
int pitch     = 255/2; // 3.3v / 2
int roll      = 255/2; // 3.3v / 2

int throttlePin   = 2; // PWM
int yawPin        = 3; // PWM
int pitchPin      = 4; // PWM
int rollPin       = 5; // PWM


void setup() {

  // Begin Serial communication at 115200 baud
  Serial.begin( 115200 );

  // Set pinModes
  pinMode( throttlePin,  OUTPUT );
  pinMode( yawPin,       OUTPUT );
  pinMode( pitchPin,     OUTPUT );
  pinMode( rollPin,      OUTPUT );
}

void loop() {
  // When there is an Serial connection available, get the values
  if ( Serial.available() > 0 ) {
    throttle    = Serial.parseInt();    // Store first interger value from Serial buffer
    yaw         = Serial.parseInt();    // Store second interger value from Serial buffer
    pitch       = Serial.parseInt();    // Store third interger value from Serial buffer
    roll        = Serial.parseInt();    // Store fourth interger value from Serial buffer
  }

  // Write values to the drone controller
  // Use a low pass filter or DAC (digital to analog converter) to convert PWM to an analog voltage
  analogWrite( throttlePin,  throttle );
  analogWrite( yawPin,       yaw      );
  analogWrite( pitchPin,     pitch    );
  analogWrite( rollPin,      roll     );
}








