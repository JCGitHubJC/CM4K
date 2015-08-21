int ryan = 7;
int oz = 8;
int jerry = 6;

void blinkLed(int ryan, int del)

{
  pinMode(ryan, OUTPUT);
  digitalWrite(ryan, HIGH);
  delay(del);
  digitalWrite(ryan, LOW);
  delay(del);
    pinMode(oz, OUTPUT);
  digitalWrite(oz, HIGH);
  delay(del);
  digitalWrite(oz, LOW);
  delay(del);
}
void setup()
{
  pinMode(jerry,INPUT);
}
void loop()
{
  boolean buttonPressed= digitalRead(jerry);
  if (buttonPressed)
  {
  blinkLed(ryan, 50) ;
 blinkLed(oz, 50) ;
}
}
