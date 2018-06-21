int ledPin[] = {6,5,4,0};

void setup()
{
  for (int i =0;i<4;i++)
  {
    pinMode(ledPin[i], OUTPUT);
  }
}

void loop() 
{
  byte nums[] = {0, 1, 3, 6, 4, 12, 8, 12, 4, 6, 3, 1, 0};
  for (byte i = 0; i<13;i++)
  {
    displayBinary(nums[i]);
    delay(1000);
  } 
}

void displayBinary( byte numToShow)
{
  for (int i =0;i<4;i++)
  {
    if (bitRead(numToShow, i)==1)//bitRead(x,n)---: x-byte from which bit has to be read  n-the bit to read
    {
      digitalWrite(ledPin[i], HIGH); 
    }
    else
    {
      digitalWrite(ledPin[i], LOW); 
    }
  }
}

// 0-0000,1-0001,3-0011,6-0110,12-1100,8-1000,4-0100,6-0110,3-0011,1-0001,0-0000
//Inside displaybinary function each byte can execute
//Ex. numToShow=3---bitRead(0011,0),bitRead(0011,1),bitRead(0011,2),bitRead(0011,3)
//0th bit=1 then 6th pin high ;1st bit=1 then 5th pin high ; 2nd bit=0 then 4th pin low;
//3rd bit=0 then 0th pin low;
//then delay(1000) after that it go to displayNumber function
//OUTPUT= {(6,5),(5,4),(4,0),(0,4),(4,5),(5,0)} pins are high
//Each set execute after a delay
