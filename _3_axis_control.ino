void setup() {
  Serial.begin(57600);
}
void loop() {
  int Value1 = analogRead(A0);
  int Value2 = analogRead(A0);
  int Value3 = analogRead(A0);
  int Value4 = analogRead(A0);
  int Value5 = analogRead(A0);
  int Value6 = analogRead(A0);
  int Value7 = analogRead(A0);
  int Value8 = analogRead(A0);
  int Value_final=Value1+Value2+Value3+Value4+Value5+Value6+Value7+Value8;
  Value_final=Value_final/8;
  if (Value_final>100){
    Value_final=Value_final/5;
  Serial.println("UD");  
  Serial.println(Value_final);
  }
  else 
  {
    Serial.println("UD");
    Serial.println(Value_final);
  } 
  int Value10 = analogRead(A1);
  int Value20 = analogRead(A1);
  int Value30 = analogRead(A1);
  int Value40 = analogRead(A1);
  int Value50 = analogRead(A1);
  int Value60 = analogRead(A1);
  int Value70 = analogRead(A1);
  int Value80 = analogRead(A1);
  int Value_final_fb=Value10+Value20+Value30+Value40+Value50+Value60+Value70+Value80;
  Value_final_fb=Value_final/8;
  if (Value_final_fb>100){
    Value_final_fb=Value_final_fb/5;
  Serial.println("FB");  
  Serial.println(Value_final_fb);
  }
  else
  {
   Serial.println("FB");  
    Serial.println(Value_final_fb);
  }
  int Value11 = analogRead(A2);
  int Value21 = analogRead(A2);
  int Value31 = analogRead(A2);
  int Value41 = analogRead(A2);
  int Value51 = analogRead(A2);
  int Value61 = analogRead(A2);
  int Value71 = analogRead(A2);
  int Value81 = analogRead(A2);
  int Value_final_rl=Value11+Value21+Value31+Value41+Value51+Value61+Value71+Value81;
  Value_final_rl=Value_final_rl/8;
  if (Value_final>100){
    Value_final_rl=Value_final_rl/5;
  Serial.println("RL"); 
  Serial.println(Value_final_rl);
  }
  else
  {
 Serial.println("RL"); 
  Serial.println(Value_final_rl);
  }
  delay(500);
}
