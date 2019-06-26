import processing.serial.*;
int throttle   = 0;
int yaw        = 127;
int pitch      = 127;
int roll       = 127;
import cc.arduino.*;

Arduino arduino;
int Pin = 8;
void setup() {
  arduino = new Arduino(this,"COM18", 57600);
  arduino.pinMode(Pin, Arduino.OUTPUT);
  size(150, 500);
  //mindSet = new MindSet(this, "COM5");
  smooth();
  strokeWeight(5);
  stroke(255);
  strokeCap(SQUARE);
 fill(255);
  
}
void draw()
{
  background(0);
  line( 0, height*0.60, width, height*.60);
  line( width*.5, height, width*.5, height*map( float( attentionLevel ) / 100, 0, 1, 1, 0 ) );
  throttle = int( map( attentionLevel, 40, 100, 30, 255 ) );
  throttle    = constrain( throttle,  0, 255);
  pitch       = constrain( pitch,     0, 255);
  roll        = constrain( roll,      0, 255);
  yaw         = constrain( yaw,       0, 255);
    println( "attentionLevel: "+attentionLevel+" throttle: "+throttle+" yaw: "+yaw+" pitch: "+pitch+" roll: "+roll );
    
    throttle=255;
    arduino.analogWrite( Pin,throttle );
    delay(1000);
       throttle=0;
    arduino.analogWrite( Pin,throttle );
    delay(1000);
  
} 
int signalStrenght = 0;
int attentionLevel = 0;

public void attentionEvent( int attentionLevel_val ) 
{
  attentionLevel = attentionLevel_val;
}
public void poorSignalEvent( int signalNoise ) 
{
  // MindSet is adjusting
  if ( signalNoise == 200 ) {
    println( "Mindset is not touching your skin!" );
  }
  signalStrenght = int( map( ( 200-signalNoise ), 200, 0, 100, 0 ) );
  println( "Signal strength: " + signalStrenght + "%" );
}
