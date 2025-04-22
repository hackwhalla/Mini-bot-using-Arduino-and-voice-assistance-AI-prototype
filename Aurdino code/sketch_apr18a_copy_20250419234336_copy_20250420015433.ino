#include<Servo.h>

Servo head;
Servo l_hand;
Servo r_hand;

byte val = "";

void setup() {
  // put your setup code here, to run once:
  head.attach(9);
  l_hand.attach(11);
  r_hand.attach(10);
  pinMode(13, OUTPUT);  // Set LED pin as output
  digitalWrite(13, LOW); // Turn off LED by default


  Serial.begin(9600); // for communicating via serial port with Python
}

void standby(){
  // all motors to these positions
  head.write(90);
  int r_pos = 20;
  int l_pos = map(r_pos, 0, 180, 180, 0);
  
  l_hand.write(l_pos);
  r_hand.write(r_pos);
}

void stretch() {
  head.write(130);
  r_hand.write(100);
  delay(100);
  l_hand.write(100);
  delay(2000);
  head.write(50);
  delay(1000);
  standby();
}
void dance(){
  for(int i = 0; i < 5; i++){
    // Move hands alternately
    head.write(30);  // Look left
    delay(200);
    r_hand.write(170);
    delay(400); // Right hand up
    l_hand.write(30);  // Left hand down
    delay(300);
    head.write(150); // Look right
    delay(300);
    r_hand.write(30); 
    delay(400); // Right hand down
    l_hand.write(170); // Left hand up
    delay(400);
  }
  standby(); // Return to neutral position at the end
}

void no(){
  for(int i = 0; i < 5; i++){
    // Move head left and right
    head.write(0);  // Look left
    delay(300);
    head.write(180); // Look right
    delay(300);
  }
  standby(); // Return to neutral position at the end
}
void salute(){
    l_hand.write(180);
    delay(5);
    delay(600);
    l_hand.write(20);
    delay(5);
} // Return to neutral position at the end



void hi(){
  // all motors to these positions
  head.write(90);

  int i = 0;
  for(i=20; i<= 180; i++){
    r_hand.write(i);
    delay(5);
  }

  for(i=180; i>= 90; i--){
    r_hand.write(i);
    delay(5);
  }

  for(i=90; i<= 180; i++){
    r_hand.write(i);
    delay(5);
  }

  for(i=180; i>= 20; i--){
    r_hand.write(i);
    delay(5);
  }

  standby();
}

void hands_up(){  
  int i = 0;
  for(i=0; i<= 180; i++){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }

  delay(600);

  for(i=180; i>= 0; i--){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }
  
}

void weight_lift(){
  for(int i = 0; i < 5; i++){
    // Move hands alternately
    r_hand.write(180); // Right hand up
    l_hand.write(30);  // Left hand down
    delay(400);

    r_hand.write(30);  // Right hand down
    l_hand.write(180); // Left hand up
    delay(400);
  }
  standby();
}
void look_left(){
  // rotate hed to left
  head.write(180);
}
void look_right(){
  // rotate hed to left
  head.write(0);
}

void r_upper_cut(){
  // make right upper-cut
  int i = 0;
  for(i=20; i<= 180; i++){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }

  for(int count=0; count<=4; count++){
    int i = 0;
    for(i=180; i>= 50; i--){
      r_hand.write(i);
      delay(1);
      }

    for(i=50; i<= 180; i++){
      r_hand.write(i);
      delay(1);
      }
    }
   standby();
   delay(100);
}

void smash(){
  // smash things
  int i = 0;
  for(i=10; i<= 180; i++){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }
  delay(2000);
  for(i=180; i>= 0; i--){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(1);
  }
  delay(300);
  int r_pos = 180;
  int l_pos = map(r_pos, 0, 180, 180, 0);
  
  l_hand.write(l_pos);
  r_hand.write(r_pos);
  delay(1000);
  standby();
}

void loop() {
  // put your main code here, to run repeatedly:
  standby();

  if (Serial.available()>0) {
  digitalWrite(13, HIGH); // Turn ON LED to indicate connection
  } 
  else {
  digitalWrite(13, LOW); // Turn OFF LED if disconnected
  }


  while(Serial.available() > 0)  //look for serial data available or not
  {
    val = Serial.read();        //read the serial value

    if(val == 'h'){
      // do hi
       hi();
    }
    if(val == 'H'){
      hands_up();
      delay(3000);
    }
    if(val == 'l'){
      standby();
      look_left();
      delay(2000);
    }
    if(val == 'u'){
      // uppercut
      r_upper_cut();
      delay(2000);
    }
    if(val == 's'){
      smash();
      delay(2000);
    }
    if(val == 'S'){
      standby();
      delay(2000);
    }
    if(val == 'd'){
      dance();
      delay(2000);
    }
    if(val == 'n'){
      no();
      delay(2000);
    }
    if(val == 'w'){
      weight_lift();
      delay(2000);
    }
    if(val == 'p'){
      salute();
      delay(2000);
    }
    if(val == 'r'){
      look_right();
      delay(2000);
    }
    if(val == 'R'){
      stretch();
      delay(2000);
    }
  }
  delay(100);
}